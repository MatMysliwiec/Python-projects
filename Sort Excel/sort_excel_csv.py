import pandas as pd


def sort_csv(file_path, sort_column, sort_order="asc"):
    df = pd.read_csv(file_path)
    df.sort_values(by=sort_column, inplace=True, ascending=(sort_order.lower() == "asc"))
    df.to_csv(file_path, index=False)


if __name__ == "__main__":
    file_path = input("Enter the path of the CSV file: ")
    sort_column = input("Enter the column to sort by: ")
    sort_order = input("Enter the sort order (asc/desc): ")

    while sort_order.lower() not in ['asc', 'desc']:
        print("Invalid sort order. Please enter 'asc' or 'desc'.")
        sort_order = input("Enter the sort order (asc/desc): ")

    sort_csv(file_path, sort_column, sort_order)

    print(f"File '{file_path}' has been sorted based on column '{sort_column}' in {sort_order}ending order.")
