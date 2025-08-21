# for writing csv per run

import csv

class CSVWriter:
    
    @staticmethod
    def csv_filename(stock, year, monthly_investment):
        """Names csv file"""
        return f"data/{stock.ticker.upper()}_{year}Y_{str(monthly_investment).replace('.', '_')}.csv"

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
            