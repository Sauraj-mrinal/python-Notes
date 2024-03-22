# set is a same as list 
# but it could not accept duplicates and it will not manage order

# if we talking about tupple 
days = ( 'monday', 'tuesday', 'wednesday', 'thursday','monday')
print(days)
# PS E:\Python\python-Notes> python set.py
# ('monday', 'tuesday', 'wednesday', 'thursday','monday')


# but in case of set it will not print duplicates

my_set  = { 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday', 'monday'}
print(my_set)

#{'friday', 'tuesday', 'wednesday', 'thursday', 'monday'}



# to add new values 
my_set.add('mon')
print(my_set) # {'friday', 'tuesday', 'mon', 'wednesday', 'monday', 'thursday'}

# """"""" USER INTERACTION """"""""""""""
