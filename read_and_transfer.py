import pandas as pd
def read_and_export(txt_file, csv_file):
    try:
        with open(txt_file, 'r') as file:
            content = file.read()

        if not content.strip():
            raise ValueError("Error: The .txt file is empty")

        data = {'Text': [content]}
        df = pd.DataFrame(data)

        df.to_csv(csv_file, index=False)

        print(f"{txt_file} has been successfully transferred to {csv_file}.")

    except FileNotFoundError:
        print(f"Error: File {txt_file} not found.")
    except IsADirectoryError:
        print(f"Error: {txt_file} is a directory")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

read_and_export('txt_file.txt', 'output.csv')
