from sys import argv
import sys
import re #regex
import os
import csv
import pandas as pd


def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]


new_file_name = "clean_data.csv"

if (len(argv))==1:
    print("Error! No params! Usage: script.py <filename> <filename> <filename> ")
    sys.exit()

sentences = []
languages = []

for argument in argv:
    try:
        if (argument==argv[0]):
            print("Cleaning started . . . ")
            continue

        try:
            file = open(argument+".txt", "r", encoding="utf8")
        except FileNotFoundError:
            print("Error! No file with the name: "+argument +" (Provide filename without extenstion eg: german instead of german.txt) ")
            sys.exit()

        file.seek(0)
        lines = file.readlines()

        #new file
        #new_file = open(new_file_name, "a+", encoding="utf8")

        for line in lines:
            new_line = re.split(r'\t+', line)[1]
            new_line = new_line[0:len(new_line)-1]
            sentences.append(new_line)
            languages.append(argument)
            #new_file.write(new_line)
        file.close()
    except EnvironmentError:
        print("Error! file in wrong format!")
        sys.exit()

df = pd.DataFrame(data={"sentence":sentences, "language":languages})
df.to_csv(new_file_name , sep=",", index=False, columns=["sentence", "language"])
print("Cleaning completed successfully. New file created: "+os.getcwd()+"\\"+new_file_name)




