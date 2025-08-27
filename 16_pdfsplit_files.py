import pypdf as pdf
from pathlib import Path

def split_pdf_files(input_pdf_file):
    destination_dir = Path.cwd()/'pdf_files'
    Path.mkdir(destination_dir, exist_ok=True)
    try:
        if not Path(input_pdf_file).exists():
            raise FileNotFoundError(f'Error: {input_pdf_file} does not exist')
        reader = pdf.PdfReader(input_pdf_file)
        pdf_pages = reader.pages
        num_pages = len(pdf_pages)
        
        original_file_name = Path(input_pdf_file).stem
        for i in range(num_pages):
            page = pdf_pages[i]
            writer = pdf.PdfWriter()
            writer.add_page(page)
            file_name = destination_dir/f'{original_file_name}_{i+1}.pdf'
            with open(file_name, 'wb') as file:
                writer.write(file)
        print(f'{input_pdf_file} successfully separated into separate files')
    
    except Exception as e:
        print(f'Error, something went wrong {e}')
        return False
    
split_pdf_files('TestpdfFile.pdf')