import pypdf as pdf
from pathlib import Path


def get_defined_page(input_file, start_page: int, end_page: int):
    destination_dir = Path.cwd()/'single_pdf'
    Path.mkdir(destination_dir, exist_ok=True)
    
    reader = pdf.PdfReader(input_file)
    writer = pdf.PdfWriter()
    pdf_pages = reader.pages
    try:
        if not Path(input_file).exists():
            raise FileNotFoundError(f'Error {input_file} not found')
        if '.pdf' not in Path(input_file).suffix:
            print('File must be a pdf format')
        original_file_name = Path(input_file).stem
        for i in range(start_page, end_page):
            selected_page = pdf_pages[i]
            writer.add_page(selected_page)
            file_name = destination_dir/f'{original_file_name}_page_{i}.pdf'
            with open(file_name, 'wb') as file:
                writer.write(file)
        print('Files successfully extracted')
    except Exception as e:
        print(f'Error, something went wrong {e}')
    
get_defined_page('TestpdfFile.pdf', 0, 2)