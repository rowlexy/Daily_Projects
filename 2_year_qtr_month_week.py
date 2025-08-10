from pathlib import Path
from pprint import pprint

# Path.mkdir('2024', exist_ok=True)
# Path.mkdir('2025', exist_ok=True)

current_dir = Path.cwd()

dir_2024 = current_dir/'2024'
dir_2025 = current_dir/'2025'

months_by_quarter = {
    'Q1': ['Jan', 'Feb', 'Mar'],
    'Q2': ['Apr', 'May', 'Jun'],
    'Q3': ['Jul', 'Aug', 'Sep'],
    'Q4': ['Oct', 'Nov', 'Dec']
}


def createWeekFiles():
    quarters = {} # => final dictionary
    week_count = 1
    for qrtr, months in months_by_quarter.items():
        quarters[qrtr] = {} # => Jan, Feb.....
        
        for month in months:
            weeks = [f'WK-{week_count + i}' for i in range(4)] # => ['WK-1', .....]
            quarters[qrtr][month] = weeks
            week_count += 4
    return quarters


def createSubDirectory():
    quarters = createWeekFiles()
    pprint(quarters)
    
    for qrtr, months in months_by_quarter.items():
        qtr_dir_2024 = dir_2024/qrtr
        qtr_dir_2025 = dir_2025/qrtr
        qtr_dir_2024.mkdir(parents=True, exist_ok=True)
        qtr_dir_2025.mkdir(parents=True, exist_ok=True)
        
        for month in months:
            month_2024 = qtr_dir_2024/month
            month_2025 = qtr_dir_2025/month
            month_2024.mkdir(exist_ok=True)
            month_2025.mkdir(exist_ok=True)
            
            for week in quarters[qrtr][month]:
                week_2024_csv = month_2024/f'{week}.csv'
                week_2025_csv = month_2025/f'{week}.csv'
                week_2024_csv.touch(exist_ok=True)
                week_2025_csv.touch(exist_ok=True)
                
createSubDirectory()