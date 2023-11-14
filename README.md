# Excel Splitter Tool

The Excel Splitter tool is a simple Python script that divides Excel files into smaller files, each containing a maximum of 1000 rows. This README provides instructions on setting up and using this tool.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Python](https://www.python.org/downloads/) (version 3.x)
- [Pip](https://pip.pypa.io/en/stable/installation/) (usually installed with Python)

## Setup

1. **Clone or Download the Repository**
   - If you're familiar with Git, clone this repository.
   - Otherwise, download the ZIP file of this project and extract it to a folder on your computer.

2. **Navigate to the Project Directory**
   - Open your command line or terminal.
   - Change directory (`cd`) to the folder where you extracted or cloned the project.

3. **Install Pipenv**
   - Run the following command to install Pipenv, which is used for creating a virtual environment:

     ```bash
     pip install pipenv
     ```

4. **Create a Virtual Environment and Install Dependencies**
   - In your project directory, run:

     ```bash
     pipenv install
     ```

     This command will create a virtual environment and install the necessary libraries (`pandas` and `openpyxl`) as specified in the `Pipfile`.

## Usage

1. **Place Your Excel File in the `input` folder**
   - Place the Excel file you want to split in the `input` folder within the project directory. Make sure the folder exists and the Excel file is in `.xlsx` format. Only one file should be there at a time.

2. **Activate the Virtual Environment**
   - In the project directory, run:

     ```bash
     pipenv shell
     ```

     This command activates the virtual environment.

3. **Run the Script**
   - Execute the script by running:

     ```bash
     python excel_split.py
     ```

4. **Check the Output**
   - After running the script, check the `output` folder. You will find the split Excel files there, each named `output_part_x.xlsx`, where `x` is the part number.

## Notes

- The script currently processes the first file it finds in the `input` directory.
- Each output file will have a maximum of 1000 rows, as set by the `ROW_LIMIT` variable in the script. You can change this according to your preferences.
- The output files are saved in the `output` directory; make sure this directory exists in your project folder before running the script.

## Contribution

- Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
