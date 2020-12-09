#!/usr/bin/env python3
with open ("C:/Users/raturia/Desktop/inputPS18.txt", 'rt') as fo:  
    print("Extracted Student Ids and their respected cgpa score are")
    for line in fo:
        print line.split('/')[0]
        print line.split('/')[1]
