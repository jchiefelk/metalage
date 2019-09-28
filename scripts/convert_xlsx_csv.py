import csv
import xlrd
import sys
import pdb
import os
import pdb

def run(*args):
    dirname = args[0]
    for root,dirs,files in os.walk(dirname):
        for file in files:
            if file.endswith('.xlsx'):
                wb = xlrd.open_workbook(root + '/' + file)
                sh = wb.sheet_by_name('Sheet1')
                csv_file = open(root + '/csv/' + file.strip('.xlsx') + '.csv', 'w')
                wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                for rownum in range(sh.nrows):
                    wr.writerow(sh.row_values(rownum))

                csv_file.close()
