import csv
import pandas as pd


class CSVWriter:
    @staticmethod
    def write_csv(file_path, data):
        if not data:
            print("No data available to write.")
            return

        with open(
            file_path, mode="w", newline="", encoding="utf-8-sig"
        ) as file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Data written successfully.")


class XLSXWriter:
    @staticmethod
    def write_xlsx(xlsx_file_path, data):
        if not data:
            print("No data available to write.")
            return

        df = pd.DataFrame(data)
        df.to_excel(xlsx_file_path, index=False)
        print("Data written successfully.")


"""
USAGE:
    >> CSVWriter.write_csv(output_filepath, data_store) <<

    Expected Input:
        data_store = [
            {"author": "senior_developer", "filename": "csv_writer.py"},
            {"author": "developer", "filename": "readme.txt"},
            {"author": "vibe_coder", "filename": "requirements.txt"}
        ]
        output_filepath = "results\\data_stored.csv"
    Expected Output:
        Terminal: Data written successfully.
        File Manager: "data_stored.csv" created in results/ folder.


    >> XLSXWriter.write_xlsx(output_filepath, data_store) <<

    Expected Input:
        data_store = [
            {"author": "senior_developer", "filename": "csv_writer.py"},
            {"author": "developer", "filename": "readme.txt"},
            {"author": "vibe_coder", "filename": "requirements.txt"}
        ]
        output_filepath = "results\\data_stored.xlsx"
    Expected Output:
        Terminal: Data written successfully.
        File Manager: "data_stored.xlsx" created in results/ folder.
"""
