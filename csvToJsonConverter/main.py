import converter


file_path = input("Enter the CSV file name: ")
file_path = f'./data/csv/{file_path}'
converter.csv_to_json(file_path)

