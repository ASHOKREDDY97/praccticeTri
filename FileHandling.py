# # read mode
# f = open('practice.txt','r')
# c = f.read()
# print(c)
# f.close()


# # write mode 
# f = open('practice.txt','a')
# c = f.write('this is write mode in file handling')
# print(c)
# f.close()
# f = open('practice.txt','r')
# c = f.read()
# print(c)
# f.close()


# # readlines
# f = open('practice.txt','r')
# c = f.readlines(1)
# print(c)
# f.close()


# # delete file 
# import os
# os.remove("practice.txt")


# # Check if File exist:
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")  


# # file is taken from user
# import csv
# user_input = input('enter the file name you want to read:')
# try:
#   myfile = open(user_input)
#   info = myfile.read()
# # Remove the leading spaces and newline character
#   line = info.strip()
# # lowercase to avoid case mismatch
#   line = info.lower()
#   data=info.split()
#   print(data)
# # counting how many words repeated in a file
#   count={}
#   for i in data:
#       if i in count:
#           count[i]+=1
#       else:
#           count[i]=1
# # opening csv file
#   with open('practice.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["word", "count"])
# # To get all the distinct words
#     for key in list(count.keys()):
#       print(key, ":", count[key])
#       writer.writerow([key, count[key]])
# except FileNotFoundError:
#   print('File does not exist')



# file is taken from user
import xlsxwriter
user_input = input('enter the file name you want to read:')
try:
  myfile = open(user_input)
  info = myfile.read()
# Remove the leading spaces and newline character
  line = info.strip()
# lowercase to avoid case mismatch
  line = info.lower()
  data=info.split()
  print(data)
# counting how many words repeated in a file
  count={}
  for i in data:
      if i in count:
          count[i]+=1
      else:
          count[i]=1
  workbook = xlsxwriter.Workbook('C:\\TriNet Python\\data.xlsx')
  worksheet = workbook.add_worksheet()
  for key in list(count.keys()):
      print(key, ":", count[key])
except FileNotFoundError:
  print('File does not exist')
