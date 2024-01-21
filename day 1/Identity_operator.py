# let you are creatong two  variable and both having same data type 
# so what will happen

# so both the boject will point the same value 
# or we cN SAY THAT BOTH THE OBJECT WILL BE POINT 
# same memory location 

a=10;
b=10;

print(a is b );  #TRUE (MEMORY location IS SAME )
print (a==b);# TRUE (MEMORY location IS SAME)
print ( id(a))# 140730985757400: it will return the address of a
print ( id(b))# 140730985757400 it will return the address of B


l1 = [1,2,3,4, 5];
l2 = [1,2,3,4, 5];

print (l1 is l2); #false (MEMORY location IS not SAME)

#----------------------------------------------------------------
#- Membership operator -> it is use to check membership of charactor in the string 
#  wether a character / a string / a number / is present in the string
#----------------------------------------------------------------
# there are two ways to check membership of
# 1) in 
# 2) not in


str = "mrinal";

# checkin

print( 'n'in str )# True

print( "v"  in str )# false

print("--------------------------")
# checking using "not in"

print( 'n'not in str )# false
print( 'v' not in str )# true
print("--------------------------")
l =[1,2 ,3,4,5,6]
print( ' 2' in l )#
print( ' 3' not in l )# false
print("24 " in l)
# False
# True
# False
print("--------------------------")




























