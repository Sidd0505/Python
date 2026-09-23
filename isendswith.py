'''
File = 'Name.csv'

if(File.endswith(".csv")):
    print("CSV FIle")
else:
    print("Not")
'''

# String to list conversion
s = "I am sid"
my_list = s.split(" ")
print(my_list)

#Lists are mutable
for i in range(0, len(my_list)):
    print(i)

for i in my_list:
    print(i)

# Reverse a string
print(my_list[::-1])

my_list.reverse()
print(my_list)

for i in reversed(my_list):
    print(i)


#Insert elements in list:
my_list.append("now")
print(my_list)

my_list.insert(3, "?")
print(my_list)

my_list.pop()
print(my_list)

#List Comprhension
list1 = [1,2,3,4,5,6]
new_list = [i*i for i in list1 if(i>2) if(i!=6)]
print(new_list)