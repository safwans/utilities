'''
Created on Nov 28, 2017

@author: safwans
'''
import csv
input_file = open("../../../../Downloads/NetworkCodeServes_357278_20171104_00.csv","r+")
reader_file = csv.reader(input_file)
value = len(list(reader_file))
print(value)