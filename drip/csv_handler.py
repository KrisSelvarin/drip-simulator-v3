# for writing csv per run

import csv

class CSVWriter:
    
    @staticmethod
    def open(filename, header):
        """Opens csv file"""
        CSVWriter.file = open(filename, 'w', newline="")
        CSVWriter.writer = csv.DictWriter(CSVWriter.file, fieldnames=header)
        CSVWriter.writer.writeheader()

    @staticmethod
    def write_row(row_dict):
        """Streams data"""
        CSVWriter.writer.writerow(row_dict)

    @staticmethod
    def close():
        """Closes csv file"""
        CSVWriter.file.close()
            