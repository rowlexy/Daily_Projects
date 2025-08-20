# Remove duplicate sheets from excel
# Save to a new file
# handle the error as appropriate

import openpyxl, os

def filterSheet(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError('File not found')
        
        wb = openpyxl.load_workbook(input_file)
        sheetname = wb.sheetnames
        if len(sheetname) > 1:
            remove_sheets = sheetname[1:]
            for sheet in remove_sheets:
                wb.remove(wb[sheet])
        else:
            print('Sheets not more than 1')
        
        wb.save(output_file)
        return True
        
    except Exception as e:
        print(f'Error: {e}')
        return False
    
if filterSheet('taxes.xlsx', 'taxes_edit.xlsx'):
    print('File successfully filtered and created')
