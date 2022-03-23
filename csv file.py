import csv 
df = "C:\\TriNet Python\\info.csv"
fo = open(df,"r")
content = fo.readlines()
fo.close()

for each in content:
    print(each.strip("\n").split(","))


# ###
import csv 
df = "C:\\TriNet Python\\info.csv"
fo = open(df,"r")
data = csv.reader(fo)
for each in data:
    print(each)
fo.close()

# ###
import csv
with open("C:\\TriNet Python\\info.csv") as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=",") 
    column_data = next(csv_reader) 
    print (f"Column names are {', '.join(column_data)}")

    for row in csv_reader: 
        print (f"s_no {row[0]} student name {row[1]}")

# ###
import csv
with open("C:\\TriNet Python\\info.csv") as csv_file: 
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader: 
         print (f"s_no {row[0]} student name {row[1]}")


# ###
import csv
file = open("C:\\TriNet Python\\info.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()

###
import csv
with open('sample.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)


###
import csv
file = open("C:\\TriNet Python\\sample.csv","r")
csv_reader = csv.reader(file)
for line in csv_reader:
    print(line)