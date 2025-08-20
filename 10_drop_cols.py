# Remove columns not needed using pandas df
# Save in a new file
# Create new colums and rows
# Calculate difference, average and percentage difference.
# Populate values in the columns
# Save into a new sheet

import pandas as pd
import openpyxl, os
from pathlib import Path

def dropColumn(input_file, output_file):
    try:
        if not Path(input_file).exists():
            raise FileNotFoundError(f'{input_file} not found')
        
        taxes = pd.read_excel(input_file)
        taxes = taxes.drop(labels='Order', axis=1)
        taxes.to_excel(output_file, index=False)
    except Exception as e:
        print(f'Error: {e}')

if dropColumn('taxes_edit.xlsx', 'fuel.xlsx'):
    print('Column dropped, file successfully created')

def handleNewRows(input_file, output_file):
    
    try:
        
        if not os.path.exists(input_file):
            raise FileNotFoundError(f'{input_file} not found')
        
        wb = openpyxl.load_workbook(input_file)
        sheetname = wb['Sheet1']
        
        # Header name
        sheetname['D1'] = 'Difference (Gas & Diesel)'
        sheetname['E1'] = 'Average (Gas & Diesel)'
        sheetname['F1'] = 'Percentage Difference (Gas & Diesel)'
        
        # Dictionary to hold values 
        diff_values = {}
        percent_values = {}
        average_values = {}
        
        for row in range(2, sheetname.max_row + 1):
            gas = sheetname['B' + str(row)].value
            diesel = sheetname['C' + str(row)].value
            if gas is not None and diesel is not None:
                difference = gas - diesel
                diff_values[row] = difference
                sheetname['D' + str(row)] = difference # populate directly to the cells in excel
                
                average = (gas + diesel) / 2
                average_values[row] = average
                sheetname['E' + str(row)] = average # populate directly to the cells in excel
                
                percentage = (difference / average) * 100
                percent_values[row] = percentage
                sheetname['F' + str(row)] = percentage # populate directly to the cells in excel
                
            else:
                diff_values[row] = None
                average_values[row] = None
                percent_values[row] = None
        
        wb.save(output_file)
        return True
    
    except Exception as e:
        print(f'Error: {e}')
        return False

if handleNewRows('fuel.xlsx', 'fuel_edit.xlsx'):
    print('New fields added with values')