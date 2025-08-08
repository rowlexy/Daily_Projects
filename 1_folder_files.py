from pathlib import Path
import json

current_dir = Path.cwd()
folder_path = current_dir/'folders'

year_folders = ['2024', '2025']
q2_folders = ['April', 'May', 'June']
week_files = ['WEEK-1.txt', 'WEEK-2.txt', 'WEEK-3.txt', 'WEEK-4.txt']


for year in year_folders:
    year_dir = folder_path/year
    year_dir.mkdir(exist_ok=True)
    for month in q2_folders:
        month_dir = year_dir/month
        month_dir.mkdir(exist_ok=True)
        for file in week_files:
            file_name = month_dir/file
            file_name.touch(exist_ok=True)

folders_dir = folder_path.glob('**/*')

for file in folders_dir:
    if file.is_file():
        parent_folder = file.parts[-3]
        child_folder = file.parts[-2]
        new_filename = f'{parent_folder}_{child_folder}_{file.name}'
        output_filename = file.with_name(new_filename)
        file.rename(output_filename)


print('-- Checking Alternative nested loop --')

folder_structure = {}
    
for file in folder_path.iterdir():
    if file.is_dir():
        year = file.name
        folder_structure[year] = {}
        for path in file.iterdir():
            if path.is_dir():
                month = path.name
                folder_structure[year][month] = []
                for file_name in path.iterdir():
                    if file_name.is_file():
                        parent_folder = file_name.parts[-3]
                        child_folder = file_name.parts[-2]
                        
                        if not file_name.stem.startswith(f'{parent_folder}_{child_folder}'):
                            output_file = f'copy_{parent_folder}_{child_folder}_{file_name.name}'
                            output_filename = file_name.with_name(output_file)
                            file_name.rename(output_filename)
                        folder_structure[year][month].append(output_filename.name)
                    

# Saving dictionary as JSON

json_path = current_dir/'folder_structure.json'

with open(json_path, 'w') as json_file:
    json.dump(folder_structure, json_file, indent=4)
    print(f"JSON saved to {json_path}")




