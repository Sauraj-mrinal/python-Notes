# to take input we will use : -  input 
# to take output we will use : - output


a = input()
b = input()

print ('type(a)' , type(a)) # str
print ('type(b)', type(b)) # str

# to convert input which is in string format by default 
# string to int 

a = int(input());
b = int(input());

print (type(a))
print(type(b))  

# // output -> 
# 4
# 2
# type(a) <class 'str'>
# type(b) <class 'str'>
# 3
# 2
# <class 'int'>
# <class 'int'>

# take marks of student in English , Science , Math  as a input and print the average of it 

# inout part 
English  = int( input(' please enter the marks of english'))
Science  = int (input('Please enter the marks of science'))
Math = int (input('Please enter the marks of math'))

# use the formula to calculate the average of students

avg =   English + Science + Math
print(' the average marks of student is ' , avg//3);













