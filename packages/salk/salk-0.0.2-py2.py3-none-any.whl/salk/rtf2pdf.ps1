# Original source:
# https://github.com/dougfernando/utility-scripts/blob/master/doc2pdf.ps1

param (
    [string]$src = $(Throw "You have to specify a source path."),
    [string]$dst = $(Throw "You have to specify a destination path.")
)

function Write-PDF {
    param (
        $source,
        $destination
    )
    
    echo "IN:  $source"
    
    $formatPDF = [ref] 17

    $word = new-object -ComObject "word.application"
    $doc = $word.documents.open($source)
    $doc.SaveAs($destination, $formatPDF)
    $doc.Close()

    echo "OUT: $destination"
    echo ""
    
    ps winword | kill
}


foreach ($file in (Get-ChildItem $src\* -Include ('*.rtf'))) {
    $outName = $file.name.Substring(0, $file.name.Length - 3) + "pdf"
    Write-PDF $file.fullName "$dst\$outName"
}
