from sys import argv
import sys
import re #regex
import os

new_file_name = "clean_data.csv"

if (len(argv))==1:
    print("Error! No params! Usage: script.py <filename> <filename> <filename> ")
    sys.exit()


for argument in argv:
    try:
        if (argument==argv[0]):
            print("Cleaning started . . . ")
            continue

        try:
            file = open(argument+".txt", "r", encoding="utf8")
        except FileNotFoundError:
            print("Error! No file with the name: "+argument +" (Provide filename without extenstion eg: german insted of german.txt) ")
            sys.exit()

        file.seek(0)
        lines = file.readlines()

        #new file
        new_file = open(new_file_name, "a+", encoding="utf8")

        for line in lines:
            new_line = re.split(r'\t+', line)[1]
            new_line = new_line.replace( ".", ".,"+argument)
            new_file.write(new_line)
        file.close()
    except:
        print("Error! file in wrong format!")
        sys.exit()
    print("Cleaning completed successfully. New file created: "+os.getcwd()+"\\"+new_file_name)




