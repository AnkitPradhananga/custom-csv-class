import csv
import os
import shutil


class CustomCSV:

    def __init__(self, file_path):
        self.file_path = file_path
        self.headers = []
        self.rows = []

    def read_data(self):
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                all_data = list(reader)

                if len(all_data) > 0:
                    self.headers = all_data[0]
                    self.rows = all_data[1:]
                else:
                    self.headers = []
                    self.rows = []
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found!")
            raise

    def get_headers(self):
        return self.headers

    def get_rows(self):
        return self.rows

    def delete_row(self, row_number):
        if row_number < 1 or row_number > len(self.rows):
            print(f"Error: Row {row_number} doesn't exist!")
            return False

        del self.rows[row_number - 1]
        self._write_to_file()
        return True

    def replace_row(self, row_number, new_data):
        if row_number < 1 or row_number > len(self.rows):
            print(f"Error: Row {row_number} doesn't exist!")
            return False

        if len(new_data) != len(self.headers):
            print(f"Error: New data needs {len(self.headers)} columns!")
            return False

        self.rows[row_number - 1] = new_data
        self._write_to_file()
        return True

    def copy_file(self, new_path):
        try:
            shutil.copyfile(self.file_path, new_path)
            print(f"File copied to: {new_path}")
            return True
        except Exception as e:
            print(f"Error copying file: {e}")
            return False

    def clear_file(self):
        self.rows = []
        self._write_to_file()
        print("File cleared! Headers kept.")
        return True

    def _write_to_file(self):
        try:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
                for row in self.rows:
                    writer.writerow(row)
        except Exception as e:
            print(f"Error saving file: {e}")

    def show_data(self):
        print(f"\n=== File: {self.file_path} ===")
        print(f"Headers: {self.headers}")
        print(f"Total rows: {len(self.rows)}")
        print("\nData:")
        for i, row in enumerate(self.rows, 1):
            print(f"Row {i}: {row}")
