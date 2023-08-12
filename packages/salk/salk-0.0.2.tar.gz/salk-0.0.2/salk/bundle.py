import sys, io, re, toml, collections, itertools
from pathlib import Path
from fpdf import FPDF, Align, XPos
from pypdf import PdfReader, PdfWriter

# Driver / Big Ol' Function
def main():
    conf = toml.load(Path.cwd() / 'conf.toml')['title-info']

    # Total ordering on all 
    doc_order = toml.load(conf['doc-order'])
    docroot = Path(conf['doc-root'])

    # assign each document to the most specific stem
    pdf_paths = set((docroot / 'pdf').glob('*.pdf'))
    best_match = list(sorted(
        itertools.chain([x for sect in doc_order.values() for x in sect['order']]), # throw all doc stems together
        key = lambda x: -len(x) # longest first
    ))

    # Check that no document is specified twice
    for k, v in collections.Counter(best_match).items():
        if v > 1: raise Exception(f'{k} appears more than once in the document order.')

    order_children = collections.defaultdict(list)

    total_pages = len(doc_order)
    for p in sorted(pdf_paths): # alphabetical order within each doc stem

        for m in best_match:
            if p.stem.startswith(m):
                order_children[m].append(p)
                total_pages += len(PdfReader(p).pages)
                break

        else: print(f'{p.stem} not found in document order, ignoring.')

    # TEST CONTENT
    #reader = PdfReader(docroot / 'pdf' / 'FILE GOES HERE')
    #print(reader.pages[0].extract_text())
    #return

    # TODO: Replace with structured content metadata:
    # 1) Sections included, with page number of separator
    # 2) Source documents included
    #    - title
    #    - start page, accounting for section start pages
    # 3) Compute length of ToC itself based on number of entries and their
    #    heights
    # 4) Render ToC using the source starting page numbers, offset by the
    #    computed length of the ToC
    print(f'Total content pages: {total_pages}')

    cur_page = 1
    cur_section = 0
    output = PdfWriter()

    # Do title page
    output.append(PdfReader(io.BytesIO( make_title(conf) )))
    output.add_outline_item('Title', 0)
    # uncomment to print title and exit
    #output.write(docroot / 'title.pdf'); output.close(); return

    # TODO: Do table of contents here


    for section, section_info in doc_order.items():

        cur_section += 1
        output.append(PdfReader(io.BytesIO( section_page(cur_section, section.replace('_', ' ')) )))
        section_bookmark = output.add_outline_item(f'Part {cur_section} - ' + section.replace('_', ' '), cur_page) # outline pages are 0-indexed but we add one for the title page
        cur_page += 1

        # uncomment to skip actual content
        #continue

        for source_doc in section_info['order']:

            # do all paths that start with the doc order stem in alphabetical order
            for path in order_children[source_doc]:
                
                source = PdfReader(path)
                print(f'{path.name}: {len(source.pages)}')

                content = PdfReader(io.BytesIO( make_content(cur_page, total_pages, source, conf) ))
                for content_page, source_page in zip(content.pages, source.pages):
                    source_page.merge_page(page2 = content_page)
                
                title_lines = get_title_lines(source, conf['protocol'])
                bkmk_title = '\n    '.join(title_lines)

                output.append(source)
                output.add_outline_item(f"p{cur_page}: {bkmk_title}",
                    cur_page, # add one for title page again
                    parent = section_bookmark
                )
                cur_page += len(source.pages)
                pdf_paths.remove(path)

            #if cur_page > 20: break

    print('Writing final document...')
    output.write(docroot / 'merged.pdf')
    output.close()


"""
Constructs and returns a title page.
"""
def make_title(context):
    dim = (612, 792) # 8.5" by 11"
    i = 72
    h = 36
    q = 18
    st = 3*i

    study_body = [
        context['study-title'],
        '',
        f"({context['study-acronym']})"
    ]

    pdf = FPDF(unit = 'pt', format = dim)
    pdf.set_margins(72, 72, 72) # 1" for left, top, and right
    pdf.set_line_width(6)
    pdf.set_draw_color(0, 0, 0)
    pdf.add_page()

    pdf.line(2*i, st-h, 7*i+h, st-h)

    pdf.set_font('Helvetica', 'B', 24)
    pdf.set_y(st)
    pdf.cell(w = 0, txt = context['preparer'], align = Align.R)
    
    pdf.set_font('Helvetica', 'B', 18)
    pdf.set_y(st+h)
    pdf.cell(w = 0, txt = context['meeting-title'], align = Align.R)

    pdf.set_font('Helvetica', '', 12)
    pdf.set_y(st+h+q+9)
    pdf.cell(w = 0, txt = context['meeting-date'], align = Align.R)

    pdf.set_font('Helvetica', 'B', 12)
    pdf.set_xy(2*i+h, st+i+q)
    pdf.multi_cell(w = 0, h = 16, txt = '\n'.join(study_body), align = Align.R)
    
    pdf.line(2*i, pdf.get_y()+h, 7*i+h, pdf.get_y()+h)

    pdf.set_line_width(1)
    pdf.line(i, 9*i+q, 7*i+h, 9*i+q)
    
    pdf.image(Path(context['logo-path']),
        x = i,
        y = 9*i+h,
        h = h+q
    )

    return pdf.output()


"""
Constructs and returns a section separator page.
"""
def section_page(k, name):
    dim = (612, 792) # 8.5" by 11"

    pdf = FPDF(unit = 'pt', format = dim)
    pdf.set_margins(72, 72, 72) # 1" for left, top, and right
    pdf.set_line_width(6)
    pdf.set_draw_color(0, 0, 0)
    pdf.add_page()

    pdf.set_font('Helvetica', 'B', 18)
    pdf.set_y(324)
    pdf.cell(w = 0, txt = f'Part {k}', align = Align.C)

    pdf.set_font('Helvetica', 'B', 24)
    pdf.set_y(360)
    pdf.cell(w = 0, txt = name, align = Align.C)

    return pdf.output()


"""
Constructs content to merge into every page of the output.
Includes:
    - Page numbers at center-bottom
    - Watermark text 'BLINDED'
    - ...
"""
def make_content(k, n, doc, context):

    sz = (doc.pages[0].mediabox.width, doc.pages[0].mediabox.height)
    count = len(doc.pages)

    font_size = 11

    pdf = FPDF(unit = 'pt', format = sz)
    pdf.set_font('Courier', '', font_size)

    pos = 0/8
    extend = 8/8
    img_box = sz[0]*pos, sz[1]*pos, sz[0]*extend, sz[1]*extend

    for i in range(count):
        pdf.add_page()
        txt = f'Page {k+i} of {n}'
        x_disp = len(txt) * font_size * 0.3 # width is about 60% of height for Courier

        # watermark
        if 'watermark' in context:
            with pdf.local_context(fill_opacity = 0.35):
                pdf.image(Path(context['watermark']), *img_box, keep_aspect_ratio = True)

        # page number footer
        pdf.text(sz[0] // 2 - x_disp, sz[1]-36, txt)
        #pdf.set_y(sz[1] - 36)
        #pdf.cell(w = 0, txt = txt, align = Align.C)

    return pdf.output()


"""
Retrieve the title information from the actual pdf.
"""
def get_title_lines(reader, terminate):
    titles = []
    for line in reader.pages[0].extract_text().split('\n'):

        if re.search(r'[a-zA-Z\d]', line) and not re.search(terminate, line):
            m = re.search(r'    ', line) # cut off line at first quadruple space
            if m: line = line[:m.start()]

            line = re.sub(r'\s*-\s*', '-', re.sub(r'\s+', ' ', line)) # eliminate some types of extra space
            titles.append(line)

        elif titles: break

    return titles


if __name__ == '__main__':
    main()
