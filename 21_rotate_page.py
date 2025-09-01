# rotate the first two pages to its default state
# rotate all pages in the rotate.pdf to their default state

import pypdf as pdf
from pathlib import Path

def rotate_pdf_pages(input_file, output_file):
    
    if Path(input_file).suffix != '.pdf':
        print('Only pdf extensions are allowed')
    
    if not Path(input_file).exists():
        raise FileNotFoundError('File not found')

    try:
        reader = pdf.PdfReader(input_file)
        pdf_pages = reader.pages
        page_length = len(pdf_pages)
        writer =  pdf.PdfWriter()
        
        for page in range(page_length):
            file_pages = pdf_pages[page].rotate(270)
            writer.add_page(file_pages)
            with open(output_file, 'wb') as file:
                writer.write(file)
    except Exception as e:
        print(f'Error, something went wrong {e}')
    
    print(f'{output_file} successfully rotated')
    
rotate_pdf_pages('rotated.pdf', 'rotated_edit.pdf')