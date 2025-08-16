import os, shutil
from pathlib import Path


current_dir = Path.cwd()
file_dir = current_dir/'files'

documents = ['Document1.txt', 'Document2.txt', 'Document3.txt']

for file in documents:
    file_name = file_dir/file
    file_name.touch(exist_ok=True)
    
for doc in current_dir.iterdir():
    if doc.suffix == '.txt':
        destination = file_dir/doc.name
        shutil.move(doc, str(destination))