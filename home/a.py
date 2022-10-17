# # str1 = input("Please Enter your String : ")
# # str2 = ''

# # for i in range(len(str1)):
# #     if(str1[i] == 'p'):
# #         str2 = str2 + 'm'
# #     elif(str1[i] == 'i'):
# #         str2 = str2 + 'k'
# #     else:
# #         str2 = str2 + str1[i]

# # print("\nOriginal String :  ", str1)
# # print("Modified String :  ", str2)


# # i = 1
# # flag = 0
# # while(i <= 4):
# #     username = input("username: ")
# #     password = input("password: ")
# #     if(username == 'admin123' and password == 'pass123'):
# #         flag = 1
# #         break
# #     # i = i+1
# # if(flag == 1):
# #     print('valid')
# # else:
# #     print('in')

# # a = "I love Python programming"
# # print(a[-12:-18])

# # a_string = "Hello. Hello everyone. I am saying Hello"
# # for index in range(len(a_string)):
# #     if a_string.startswith('Hello', index):
# #         print("Position at :", index)

# # a = [2, 13, 'hello', 23, 2, 'hello', 34, 13]
# # b = set(a)
# # print(b)

# # a = [4.23, 65, 78, 5.24]
# # a.reverse()
# # a.sort(reverse=True)
# # print(a)

# # def findtriplet(list, n):
# #     found = False
# #     for i in range(0, n-2):
# #         for j in range(i+1, n-1):
# #             for k in range(j+1, n):
# #                 if (list[i]+list[i]+list[k] == 0):
# #                     print(list[i], list[j], list[k])
# #                     found = True
# #     if (found == False):
# #         print("not exist")


# # def __len__(self):
# #     return len(self.findtriplet)


# # with open('C:\\Users\\acer\\minor_project\\home\\file.csv', 'r') as file:
# #     s = file.read().splitlines()
# #     r = s[1:]
# #     d = {}
# #     for i in range(len(r)):
# #         k, v = r[i].split(',')
# #         d[k] = d.get(k, 0)+int(v)
# #     print(d)


# # import csv
# # reader = csv.reader(
# #     open('C:\\Users\\acer\\minor_project\\home\\file.csv', 'r'))
# # d = {}
# # next(reader)
# # for row in reader:
# #     k, v = row
# #     d[k] = d.get(k, 0) + int(v)
# # print("Name: Ayush Bajpai, UID: 20BCS4468")
# # print(d)

# # import pandas as pd
# # a = pd.read_csv('Book1.csv')
# # print(a)
# # d = {}
# # for i in a.index:
# #     if a['player'][i] in d:
# #         d[a['player'][i]] += a['century'][i]
# #     else:
# #         d[a['player'][i]] = a['century'][i]
# # print(d)


# import csv

# # field names
# fields = ['Name', 'Salary']

# # data rows of csv file

# lst = input("Enter name and salary seperated by comma: ").split(',')
# # rows = [['Nikhil', 'COE', '2', '9.0'],
# #         ['Sanchit', 'COE', '2', '9.1'],
# #         ['Aditya', 'IT', '2', '9.3'],
# #         ['Sagar', 'SE', '1', '9.5'],
# #         ['Prateek', 'MCE', '3', '7.8'],
# #         ['Sahil', 'EP', '2', '9.1']]


# # writing to csv file
# with open("C:\\Users\\acer\\minor_project\\home\\data.csv", 'w+') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)

#     # writing the fields
#     csvwriter.writerow(fields)

#     # writing the data rows
#     csvwriter.writerows(lst)


d = {'m': 1, 'a': 2, 't': 1, 'h': 3}
k = d.get('2', 3)+2
print(k)
