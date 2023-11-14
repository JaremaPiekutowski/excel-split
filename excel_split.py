import os
import pandas as pd


ROW_LIMIT = 1000

INPUT_FILE_PATH = "input/" + os.listdir("input")[0]
OUTPUT_FILE_PATH = "output/"


def split_excel_file(input_file_path, output_folder, row_limit=1000):
    data = pd.read_excel(input_file_path)

    # Calculate the number of splits needed
    num_splits = len(data) // row_limit + (1 if len(data) % row_limit else 0)

    # Split the file and save each part
    for i in range(num_splits):
        start_row = i * row_limit
        end_row = start_row + row_limit
        split_data = data.iloc[start_row:end_row]

        split_file_name = f"{output_folder}/output_part_{i+1}.xlsx"
        split_data.to_excel(split_file_name, index=False)

    print(
        f"Split completed for {input_file_path}."
        f"Files are saved in the '{output_folder}' directory."
        )


if __name__ == "__main__":
    split_excel_file(INPUT_FILE_PATH, OUTPUT_FILE_PATH, ROW_LIMIT)
