
#Import writer class from csv module
from csv import writer
from csv import DictWriter
column_name=["Open","Time","High","low","close"]

def addRow(column_name,row):
   
   with open('sample.csv', 'a') as f_object:
      dictwriter_object = DictWriter(f_object, fieldnames=column_name)
      dictwriter_object.writerow(row)

      f_object.close()