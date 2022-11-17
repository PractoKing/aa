from IPython.lib.display import isdir #BCT 3
print(" Student Information ")
D = dict()
n = int(input('Number of the student '))
id=1
for i in range(0,n):
 x, y = input("Name of Students (First and Last name) ").split()
 z = input("Enter contact number of Student: ")
 m = input('Enter Marks Of Student: ')
 D[id] = (x,y,z, m)
 id+=1
print(D)
def sort():
 ls = list()
 for id,details in D.items():
 tup = (details)
 print(tup)
 ls.append(tup)
 ls = sorted(ls)
 for i in ls:
 print(i[0],i[1])
 return
def minmarks():
 ls = list()
 for id,details in D.items():
 ls.append(details[3])
 ls = sorted(ls)
 print("Minimum marks out of all Students: ", min(ls))
 return
def searchdetail(n):
 for id,details in D.items():
 if(int(id)==n):
 print(id,details)
 break
 return
def fallback():
 print("Error!!!Please provide proper input!!")
def option():
 choice = input('''Enter the operation detail: \n \
 1: Sorting using first name \n \
 2: Finding Minimum marks \n \
 3: Search contact number using id: \n \
 4: Exit\n \
 Option: ''')
 if int(choice) == 1:
 sort()
 print('Want to perform some other operation??? Y or N: ')
 inp=input()
 if(inp == 'Y'or inp=='y'):
 option()
 elif(inp=='N' or inp=='n'):
 exit()
 else:
 fallback()
 exit()
 elif int(choice) == 2:
 minmarks()
 print('Want to perform some other operation??? Y or N: ')
 inp = input()
 if(inp == 'Y'or inp=='y'):
 option()
 elif(inp=='N' or inp=='n'):
 exit()
 else:
 fallback()
 exit()
 elif int(choice) == 3:
 id = int(input('Enter id of student: '))
 searchdetail(id)
 print('Want to perform some other operation??? Y or N: ')
 inp = input()
 if(inp == 'Y'or inp=='y'):
 option()
 elif(inp=='N' or inp=='n'):
 exit()
 else:
 fallback()
 exit()
 elif int(choice)==4:
 print('Thanks You ! ')
 exit()
 else:
 fallback()
option()
