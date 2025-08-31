# copy all pdf files from the download folders and store in a sub directory in the pwd

from pathlib import Path
import shutil
import pypdf as pdf


def get_pdf_files(source_dir):
    if not Path(source_dir).exists():
        raise FileNotFoundError                ('Path does not exist')
    download_dir = Path(source_dir)
    current_dir = Path.cwd()
    destination_dir = current_dir/'pdf_folder'
    Path.mkdir(destination_dir, exist_ok=True)
    pdf_files = []
    for files in download_dir.iterdir():
        if files.suffix == '.pdf':
            file_name = files.name
            pdf_files.append(file_name)
            shutil.copy(files, str(destination_dir/file_name))
            print(f'{files.name} moved into {destination_dir}')
    return pdf_files

pdf_list = get_pdf_files('/Users/Rowland/Downloads')

print(f'Total files moved: {len(pdf_list)}')
