import openpyxl

# Load the excel workbook
workbook = openpyxl.load_workbook(
    'AI\AI_in_chem\Playground\ja1c02509_si_002.xlsx')

# Get the sheet2
sheet = workbook['Sheet2']

for x in list("ACDEFGHIKLMNPQRSTVWY"):
    # Initialize the count variable to 0
    count = 0

    # Iterate through all the cells in column F and count the number of 'D'
    for cell in sheet['F']:
        if cell.value == x:
            count += 1

    # Print the count of 'D' in column F
    print(f"Number of {x}: {count}")
