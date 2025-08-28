import pypdf as pdf
from pathlib import Path

def get_last_page(input_file):
    destination_dir = Path.cwd()/'last_page'
    Path.mkdir(destination_dir, exist_ok=True)
    try:
        if '.pdf' not in Path(input_file).suffix:
            print('Error, file extension must be .pdf')
            
        if not Path(input_file).exists():
            raise FileNotFoundError(f'Error {input_file} does not exist')
        
        reader = pdf.PdfReader(input_file)
        writer = pdf.PdfWriter()
        pdf_pages = reader.pages
        num_pages = len(pdf_pages)
        original_filename = Path(input_file).stem
        last_page = num_pages - 1
        selected_page = pdf_pages[last_page]
        writer.add_page(selected_page)
        file_name = destination_dir/f'{original_filename}_page_{last_page}.pdf'
        with open(file_name, 'wb') as file:
            writer.write(file)
        print('File successfully extracted')
    except Exception as e:
        print(f'Error: something went wrong {e}\n')
get_last_page('TestpdfFile.pdf')