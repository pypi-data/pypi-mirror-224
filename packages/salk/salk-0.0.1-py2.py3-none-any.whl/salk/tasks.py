import os, re, sys, csv
import saspy
import shutil
from pathlib import Path

"""
Does all the tasks.
"""
def exec(tasks):

    for task in tasks:
        res = task()
        if not res:
            print(f'{task} failed, terminating.')
            break

"""
Runs a SAS program using the specified SASpy configuration.
Will include any specified setup files first.
"""
def sas_exec(prog_path, sascfg, setup_paths = []):

    print(f'Running {prog_path.name}')

    setup_required = os.popen(f'grep {prog_path} -e "[rR]un.*setup"').read()

    with saspy.SASsession(
            cfgfile = sascfg,
            results = 'TEXT'
    ) as sas:

        with open('saslog.log', 'w') as log: # local log file, if problem will contain the last executed program's log

            for p in (setup_paths if setup_required else []) + [prog_path]:
                res = sas.submit(f'%include "{p}";')
                log.write(res['LOG'])

                for line in res['LOG'].split('\n'):
                    if re.match(r'^ERROR', line) \
                            and not re.match(r'.*X display server', line) \
                            and not re.match(r'.*full-screen', line) \
                            and not re.match(r'.*NEWRAP Optimization', line) \
                    :
                        print(line)
                        return False

    return True

"""
Transfers all files in the source directory to their original location,
but under the new root directory.

Reads the original file paths from a source manifest CSV and replaces
the original root with the new root. The rest of the subpaths are
preserved.

Also takes a function to apply to each line in any SAS files transferred.
"""
def export(conf, mod):
    print(f"\n<< {conf['file-source']}\n>> {conf['project-root']}")

    source_path = Path(conf['file-source'])
    manifest_paths = list(source_path.glob('*.csv'))

    print(' '.join(map(lambda x: x.name.split('.')[0], manifest_paths)))
    input('\nPress Enter to proceed.')

    def migrate(txt):
        return txt \
            .replace(conf['origin-root'], conf['project-root']) \
            .replace(conf['transfer-origin'], conf['transfer'])
    
    for p in manifest_paths:
        print(f'Opening {p}')
        with open(p) as export_manifest:
            for row in csv.DictReader(export_manifest):
                copy(
                    source_path / f"export_{p.name.split('.')[0]}" / row['FILENAME'],
                    Path( migrate(row['SOURCE PATH']) ),
                    lambda x: migrate(mod(x))
                )

    return True


def copy_files(dir_from, dir_to, mv = False):
    if os.path.exists(dir_from):
        os.system(f"{'mv' if mv else 'cp'} {dir_from}/* {dir_to}")
    return True


def copy(src, dst, mod):
    print(f'\nFrom {src}')
    print(  f'To   {dst}')

    os.makedirs(dst, exist_ok = True)

    if src.suffix == '.sas': # line by line copy
        with open(src, 'r', encoding='latin1') as fin:
            with open(dst / src.name, 'w') as fout:
                for line in fin:
                    fout.write(mod(line))
    else:
        shutil.copy(src, dst)

    return True


def ensure_dirs(dirs):
    print('\nCreating other expected directories:')
    for dir in dirs:
        print(dir)
        os.makedirs(dir, exist_ok = True)
    return True

