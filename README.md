# Custom CSV Class
This repository contains an implemenmtation of a  custom CSV handling class created for the assessment. the objective is to demonstrate file handling, data manipuilation and clean class design while working with CSV files.
No .py files are inculded in the repository.


## Method Overview
Following are the methods that will be used in the code body:

1) _init_(file_path)
   This method is responsible for initializing the CustomCSV object.It accepts the path of CSV file and stores it for later use. No       file reading or modification is performed during initialization.

2) read_data()
   This method reads the CSV file form disk.
   The first row of the file is treated as headers, while the remaining rows are treated as data records.
   Headers and data rows are stored seperatetly so they can be accessed or modified independently.

3) get_headers()
   This method returns only the header row of the CSV file.
   It allows access to column names without exposing or modifying the data rows.

4) get_rows()
   This Method returns all data rows from the csv file, excluding the header.
   Each row represents a single record in the csv file.

5) delete_row(index)
   This method removes a specific data row from the CSV file based on its index.
   The header row is not affected by this operation.
   After deletion, the updated data is written back to the original file.

6) replace_row(index, new_row)
   This method replaces an existing data row at a given index with new data provided by the user.
   The structure of the CSV file is preserved, and the change is saved permanently to the file.

7) copy_file(destination_path)
   This method creates a duplicate copy of the CSV file at the specified destination path.
   The copied file contains the same headers and data as teh original file.

8) clear_file()
   This method removs all data rows from the CSV file.
   The header row is preserved so the file structure remains intact for future use.

