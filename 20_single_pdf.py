# merge pdf files in the pdf_folder into a single pdf file

import pypdf as pdf
from pathlib import Path

def merge_pdf_files(output_filename):
    pdf_dir = Path.cwd()/'pdf_folder'
    writer = pdf.PdfWriter()
    if not pdf_dir.exists():
        print('No pdf_folder directory found!')
        return
    
    pdf_count = 0
    for file in pdf_dir.iterdir():
        if file.suffix == '.pdf':
            reader = pdf.PdfReader(file)
            pdf_pages = reader.pages
            for page in pdf_pages:
                writer.add_page(page)
            print(f'{file.name} successfully added to merger')
            pdf_count += 1
    if pdf_count > 0:
        merged_file = Path.cwd()/output_filename
        with open(merged_file, 'wb') as file:
            writer.write(file)
        print(f'Successfully merged {pdf_count} PDFs into {output_filename}')
    else:
        print('No PDF files found to merge')
        
merge_pdf_files('merged_file.pdf')