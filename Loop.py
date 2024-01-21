#-----------------------------------------------------------------------------
# l-24 / 23

height  =int( input(' enter the height in feet:') )     

if( height>3):{
    print(" you can buy the Token")
}
else:{
        print (" you can't buy the Token")
    }

if height == 6:
    print(" your height is 6 and you cand selectes  ")
else:
    print( " yes my height is not bigger than 6 and you cand select")
#-----------------------------------------------------------------------------
# l-25 
    
    # coding excrise 
    # find , is number is even number or not 

    num  = int( input('enter a number '))
    if num %2 ==0:
        print (' even number ')
    else:
        print( ' numbr is odd number ') 


#-----------------------------------------------------------------------------
# l-26 
        # Nested if  
        #  if inside if is known as nested if 
        # ----------------------------------------------------------------
# ----------------------------------------------------------------
    a =52
    if a%2==0:
        print(' even number ')
        if(a>30):
            print('number is greater than 30')
    else:
        print(' number is odd number ')

    hig  = int( input('enter the hight '))
    if hig >=3 :
        print ('can ride ')

    age = int( input(' what is your age '))
    if age <12 :
        print("please pay 250")
    elif age <=18:{
       print('please pay 250 rupees ')
    }
      
    else:
            print('please pay 500 ')
    

#-----------------------------------------------------------------------------
# l-27 
        #coding exe
             
        #  problem based on 
        #     if else 
        #     if else
        #     if else 
        # ----------------------------------------------------------------
# ----------------------------------------------------------------






#-----------------------------------------------------------------------------
# l-28 
        #coding exe
             
        # calculat year is leap year or not  
        
# ----------------------------------------------------------------
#    


#-----------------------------------------------------------------------------
# l-29 
        #multiple if statement 
             
        # calculat year is leap year or not  
        
# ----------------------------------------------------------------
#  
            


#-----------------------------------------------------------------------------
# l-30 
        #pizza bill problem 
            
             
        # calculat year is leap year or not  
        
# ----------------------------------------------------------------
# 
size  =  input( 'what size of pizza you want(S/L/M)? ')
bill =0
if size == 's' or size == 'S':
     bill +=100
     print('small  size pizza price is 100')
elif size == "M" or size == "m":
     bill += 200
     print('Large pizza price is 200')
else: 
     bill+= 300
     print('Large pizza price is 300')

add_pepperoni  = input( 'Do you want to add a pepperoni ? (yes/no)')
if add_pepperoni == 'yes' :
     if size == 's' or size == 'S':
          bill+= 30;
     else:
          bill+= 50
extera_cheese = input( 'Do you want to add cheese ? (yes/no)')
if extera_cheese == 'yes' :
     bill+= 20;

print (bill)





#----------------------------------------------------------------
# the for loop in python to iterate a sequence(list, tuple , string ) or other iterable object .
# iterating over aa sequence is calles traversal 
#----------------------------------------------------------------

# for x in range(10): 
#     print(2*x)


#0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
    
    # to print in single line we can write it like 

for y in range(5):{

       print(2*y, end =" ,") #0 ,2 ,4 ,6 ,8 , 

}
   
# # iterating over list 
print("-------")
    
a = ['radha', 'shyam', 'govind']
for name in a :{
 print (name *2)
}
   





#-------------------------------------------------------------------------------
        
        # while loop 
#-------------------------------------------------------------------------------
      # the while loop in python is used to iterate a block of code as long as the test expression (condition) is true 

        # we generally use this loop when we dont know beforehand ,  the number of time to iterate 

#----------------------------------- 
        # while test_ expression 
        # Body of while 
        #  t= 5
        

        # while n >= 0:
        #     print (n);
        #    n=-1;  
         
    # num = 5;

    # while num >= 0:
    #     print(num)
    #     num -= 1;
    # print ("my name is mrinal sauraj ")













