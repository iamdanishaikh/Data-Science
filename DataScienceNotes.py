#!/usr/bin/env python
# coding: utf-8

# **Python Crash Course - Part 1**

# **Arithmetic Operations**

# In[1]:


1 #integer


# In[2]:


1.0 #float


# In[3]:


1+1 #adding


# In[4]:


1*3 #multiply


# In[5]:


1/2.0 #division


# In[6]:


2**4 #2 to the power of 4


# In[8]:


2 + 3 * 5 + 5


# In[9]:


(2+3) * (5+5)


# In[10]:


#modfunction
4 % 2


# In[11]:


5 % 2


# In[12]:


8 % 2 


# **Variable Assignments**

# In[13]:


var = 2
var


# In[14]:


x = 2
y = 3
x + y


# In[20]:


x = x + x


# In[21]:


x


# In[ ]:


12var  #inavlid variable name. Variable name cannot start with number or $!12 etc


# In[22]:


name_of_var = 12  #valid variable name


# **Strings**

# In[ ]:


'' #single quotes
"" #double quotwwa


# In[23]:


'single quotes'


# In[24]:


"double quotes"


# In[25]:


'this is a string'


# In[26]:


"I can't go"


# **Printing Strings**

# In[29]:


x = 'hello'


# In[30]:


x


# In[31]:


print(x)   #printing variable, result etc


# In[32]:


num = 12
name = 'Sam'


# In[34]:


#format method
#num and name are put in order so they can be printed in that order
#"{} {}".format(variable1, variable2)
'my number is {} and my name is {}'.format(num,name)


# In[35]:


print('my number is {} and my name is {}'.format(num,name))


# In[38]:


#direct print formating
print('my number is {one} and my name is {two}, more {one}'.format(one=num,two=name))


# **Indexing Strings**

# In[39]:


s = 'hello'


# In[ ]:


#indexing starts at 0 and from the bottom it starts with -1


# In[40]:


s[0]   


# In[41]:


s[4]


# In[42]:


s[-1]


# In[43]:


#slice notation
s='abcdefhijk'


# In[44]:


#grab a and beyond
s[0:]     #: beyond , after that etc


# In[45]:


#grab everything : , upto d
s[:4]   #here d is at index 3 but we have given index 4 because python does not consider last index.


# In[46]:


s[0:3]


# In[47]:


#grab d e f
s[3:6]


# **Lists**

# In[48]:


#Notes
#lists are sequence of elements in square brackets [] seperated by commas ,
#can take any data types eg. int, char, float etc
#adding element at the end of the list using append method
#it is also in a sequence mode i.e it has indexes 
#nesting list  inside of each other
# list is mutable, that is, items in it can be changed, updated, removed etc


# In[49]:


[1,2,3]


# In[50]:


['a','b','c']


# In[51]:


my_list = ['a', 'b', 'c']


# In[52]:


#adding element at the end of the list using append method
my_list.append('d')


# In[53]:


my_list


# In[54]:


my_list[0]


# In[55]:


my_list[1:3]


# In[57]:


my_list[0] = 'New'   #editing index value in list
my_list


# In[58]:


#nesting list  inside of each other
nest = [1,2,[3,4]]


# In[59]:


nest[2]


# In[60]:


nest[2][1]      #grabbing 4 from list which is another list. Here 4 has index value 1 as it is another list
                #and [3,4] have index value 2


# In[62]:


nest = [1,2,3,[4,5,['target']]]


# In[63]:


nest[3]


# In[64]:


nest[3][2]


# In[65]:


print(nest[3][2][0])


# **Python Crash Course - Part 2**

# **Dictionaries**

# In[ ]:


# they hold elements as key and values


# In[2]:


d = {'key1':'value', 'key2':'123'}


# In[3]:


d['key1']   #call dictionary and passing in [''] KEY to get value


# In[7]:


d['key2']


# In[8]:


d = {'k1':[1,2,3]}


# In[10]:


d['k1']


# In[11]:


d['k1'][1]


# In[12]:


my_list =  d['k1']


# In[13]:


my_list[0]


# In[14]:


d['k1'][0]


# In[15]:


d = {'k1':{'innerkey':[1,2,3]}}


# In[16]:


d['k1']


# In[17]:


d['k1']['innerkey']


# In[18]:


d['k1']['innerkey'][1]


# **Booleans**

# In[ ]:


#Notes
#True and False


# In[19]:


True   #capital T


# In[20]:


False   #capital F


# **Tuples**

# In[ ]:


#Notes
# used ( )
# values cannot be added or removed
# tuples are immutable 
# do not support item assignment


# In[21]:


t = (1,2,3)


# In[22]:


t[0]


# **Sets**

# In[ ]:


#Notes
# Collection of unique elements
# values are in {  } these brackets
# they do not have : like dictionaries
# set() function to call unique values


# In[23]:


{1,2,3}


# In[24]:


{1,1,1,1,2,2,2,3,4,4,}     #output gives only unique values, that output is a set


# In[25]:


set([1,1,1,1,12,2,2,3,3,34,4,5,5,5])              #set() function to get unique values from a list 


# In[27]:


s = {1,2,3}
s.add(5)                                   # .add(value) to add elements in a set


# In[28]:


s


# In[29]:


s.add(7)


# In[30]:


s


# **Comparison Operators**

# In[ ]:


# Notes
# Allows to compare two elements to each other
# greater than , less than, equal to
# output in boolean
# for and operator all conditions must be true for output true


# In[31]:


1 > 2


# In[32]:


1 < 2


# In[33]:


1 >=2


# In[34]:


1 <= 2


# In[35]:


1 ==2


# In[36]:


1 = 1


# In[37]:


1 != 3     #meaning 1 is not equal to 3


# In[39]:


'hi' == 'bye'


# In[40]:


'hi' != 'bye'


# In[41]:


1 < 2


# In[42]:


1 < 2 and 2 < 3


# In[43]:


(1 < 2) and (2 > 3)


# In[44]:


(1 < 2) or (2 > 3)


# In[45]:


(1 < 2) or (2 > 3) or (1 == 1)


# In[46]:


True and False


# In[47]:


True or False 


# **If, elif and else statements**

# In[52]:


#Notes
# 1. if a statement is true , execute the block of code below it 
# 2. for 'else' , come out of code indentation
# 3. elif to check for multiple conditions
# 4. for elif come out of code indentation
# 5. if there are multiple elif statements, the first elif statement which is true will be executed and thats it.


# In[48]:


if 1 < 2:
       print('yep!')


# In[49]:


if True:
    print('Perform Code')


# In[51]:


if True:
    x = 2 + 2
    print(x)


# In[53]:


if 1 == 2:
    print('First')
else:
    print('Last')              


# In[54]:


if 1 != 2:
    print('First')
else:
    print('Last') 


# In[ ]:


#elif to check for multiple conditions


# In[56]:


if 1 == 2:
    print('First')
elif 4 == 4:
    print('second')
elif 3 == 3:
    print('Middle')
else:
    print('Last') 

# if there are multiple elif statements, the first elif statement which is true will be executed and thats it.


# **Python Crash Course - Part 3**

# **for loops and while loops**

# In[ ]:


#Notes
# for loops allow you to iterate through a sequence
# while loop: Continuousy perform and action after a condition has been met


# In[57]:


seq = [1,2,3,4,5]


# In[59]:


for item in seq:
    print(item)                           
#here item is a new variable which we define. It iterates like a cursor through each value and stores those values.
#here item is a variable name which we give. It can be any name which we want


# In[60]:


for jelly in seq:
    print(jelly)


# In[61]:


for num in seq:
    print('hello')     #this line does not have to be necessariliy related to the given seq, we can out anything


# In[62]:


i = 1

while i < 5:                                 #meaning while (till the time) this condition is true
    print('i is: {}'.format(i))
    i = i + 1
    
    
    #here it means i is 1 and less than 5, it will go in print statement and then 
    #i = i + 1, i.e i = 1 + 1,  i = 2
    #now it will check again in while loop, i is 2 which is less than 5, it will go in print statement and then 
    #i = i + 1, i.e i = 2 + 1,  i = 3
    #now at some point i will become 4 and then the loop will stop because after that while statement wil be false
    #because 5 < 5 is false


# **Useful funtions in Python**

# **Range**

# In[ ]:


#Notes
# Range is a generator of numerical values
# range is a shortcut method to generate values
# range does not consider the last value. eg if range(1,5) 1 to 5, it will print only 1,2,3,4


# In[63]:


for x in seq:
    print(x)


# In[64]:


range(0,5)


# In[65]:


for x in range(0,5):
    print (x)


# In[67]:


for x in range(1,5):
    print (x)


# **Converting in List by list() function**

# In[ ]:


#Notes
# list()


# In[68]:


list(range(0,5))


# In[69]:


list(range(10))     #by default it takes 0 as starting value in range(10)


# **List Comprehension**

# In[ ]:


#Notes
# Allows us to save a bunch of writing when trying to create a for loop to create a list
# List comprehension is kind of a for loop but backwards
# for is written in last and before it, we put equation we want 


# In[2]:


x = [1,2,3,4]


# In[3]:


out = []


# In[5]:


for num in x:
    out.append(num**2)      


# In[6]:


print(out)


# In[ ]:


#for num in x:
#   out.append(num**2) 
#now we see the shortcut method for the above code of creating list


# In[7]:


[num**2 for num in x]


# In[8]:


out = [num ** 2 for num in x]   #here focus on for num in x and put that in last and before it put num ** 2 and store in out variable.


# In[9]:


out


# **Functions**

# In[ ]:


#Notes
# Allows us to basically not have to continually write code again and again
# we can just write a function and call it later on 
# it is written by->       def name_of_the_function(variable):
#                              code 
# you have to call the function by->       name_of_the_function()
# they can have documentation strings by triple enclosing quotes


# In[ ]:


#example 1


# In[10]:


def my_func(param1):
    print(param1)


# In[11]:


my_func('hello')


# In[ ]:


#example 2


# In[14]:


def my_funcky(name):
    print('hello ' + name)                        #concatenate two strings together by +


# In[15]:


my_funcky('Danish')


# In[16]:


#example 3


# In[19]:


def my_function(name='Almas'):
    print('edi goli ' + name )


# In[21]:


my_function()


# In[ ]:


#example 4


# In[22]:


def square(num):                           #function
    return num**2                          #what will the function do


# In[23]:


output = square(2)            #here we are storing the function in a variable and calling that function with a value inside


# In[24]:


output


# In[ ]:


# doucmenting in a function


# In[25]:


def square(num):
    """
    This is a docstring.
    can go multiple lines
    this function squares a number
    """
    return num**2


# In[ ]:


square    #shift + tab afer the cursor is at e of square. It will bring up the documentation


# **Python Crash Course - Part 4**

# **Map functions | 
#   Filter functions |
#   Use of lambda expressions**

# In[ ]:


#Notes
# map() is a built in function
# syntax 1->   map(funciton_you_created, variable you created)
# syntax 2(by lambda expression)->  lambda vairable:variable * 2  (here instead of *2, you can put any equation) and then
#                                                                 store it in another variable
#                                   t = lamda variable:variable * 2
#                                  then call t by t()  put value inside ()       


# In[26]:


def times2(var):
    return var**2


# In[28]:


times2(5)


# **Map function | map()**
# 

# In[36]:


seq=[1,2,3,4,5]


# In[37]:


#want to apply times2 function to seq list and output the list
#Syntax->     map(function,values_to_iterate)
map(times2,seq)


# In[38]:


list(map(times2,seq))


# **Lambda expression**

# In[33]:


t= lambda var:var*2
# (here instead of *2, you can put any equation)and then store it in another variable
#                                   t = lamda variable:variable * 2
#                                  then call t by t()  put value inside ()  


# In[34]:


t(5)


# **Using lambda with map**

# In[35]:


list(map(lambda num:num*3, seq))    #here it means map lambda function to the values of seq. Num is storing 
#                                    multiples of 3 and then mapping it to the values of seq


# **Filter Funtion**

# In[ ]:


#Notes
# similar to map
# filter out elements from a sequence
# filter(function or lambda expression) filters out and returns boolean values


# In[39]:


filter(lambda num: num%2==0,seq)


# In[40]:


list(filter(lambda num: num%2==0,seq))


# **Methods**

# In[ ]:


#Notes
# just calls you can make of an object that will affect the object or return some result
# put .(dot) after variable and press TAB, you will get all the available methods
# examples: 
# variable_name.lower(), .upper(), .split(), .keys() used for dictionaries, .items(), .values(), .pop() removes last value
#from the list, .append() adds new value in the last


# In[41]:


s = 'hello my name is Sam'


# In[42]:


s.lower()


# In[43]:


s.upper()


# In[44]:


s.split()       #splits all white spaces


# In[45]:


tweet = 'Go Sports! #Sports'


# In[46]:


tweet.split()


# In[49]:


tweet.split('#')


# In[51]:


tweet.split('#')[1]


# In[52]:


d = {'k1':1, 'k2':2}


# In[53]:


d.keys()


# In[54]:


d.items()


# In[55]:


d.values()


# In[56]:


lst = [1,2,3]


# In[57]:


lst.pop()     #removes last value from the list 


# In[58]:


lst


# In[59]:


lst = [1,2,3,4,5]


# In[60]:


item = lst.pop()


# In[61]:


item


# In[62]:


lst.pop(0)                 #here in bracket it is the index number, and in output it is the value 


# In[63]:


first = lst.pop(0)


# In[64]:


first


# In[65]:


lst.append('new')


# In[66]:


lst


# **in Operator**

# In[ ]:


#syntax
# thing_you_wana_check in [list]  
# output in boolean


# In[67]:


'x' in [1,2,3]


# In[68]:


'x' in ['x','y','z']


# **Tuple Unpacking**

# In[ ]:


#Notes
# can be unpacked via for loop


# In[69]:


x =[(1,2),(3,4),(5,6)]


# In[70]:


x[0]


# In[71]:


for item in x:
    print(item)


# In[72]:


#now tuple unpacking:
for (a,b) in x:
    print(a)


# In[73]:


for (a,b) in x:
    print(b)


# **Python for Data Analysis - NumPy**

# **NumPy**
# *Is a Linear Algebra Library for Python. |
# Used as Data Analysis library |
# you can install NumPy by typing in anaconda prompt:
#    conda install numpy
#    pip install numpy  |
# NumPy arrays are mainly used |
# They are of two types: Vectors and Matrices |
# Vectors are 1Dimension arrays
# Matrices are 2Dimension arrays*
# 

# **NumPy Arrays**

# In[ ]:


#Notes
#import numpy as np


# In[74]:


my_list = [1,2,3]


# In[75]:


my_list        #just a normal python list


# In[2]:


import numpy as np


# In[79]:


arr = np.array(my_list)    #cast my_list as an array using numpy as np | and storing it in arr variable |


# In[80]:


arr                                                #1D array


# In[81]:


my_mat = [[1,2,3],[4,5,6],[7,8,9]]


# In[82]:


np.array(my_mat)                                        #2D array


# **Built in NumPy methods to create arrays a lot faster and simpler**

# **np.arrange()**

# In[83]:


#syntax
#np.arange(start,stop)
#np.arange(start,stop,stepsize)    #here stepsize can be used to get even odd values. Step size means we jump steps of the given size
np.arange(0,10)            #similar to range function


# In[84]:


np.arange(0,11)


# In[85]:


np.arange(0,11,2)    #get even numbers using stepsize 2 


# **np.zeros()**

# In[95]:


np.zeros(3)                                               #1D array, give single value in ()


# In[87]:


np.zeros((5,5))                                   #2D array, give value in ((tuple)) with tuple inside it   5rows 5colms


# In[90]:


np.zeros((2,3))                #2rows 3colms


# **np.ones()**

# In[92]:


np.ones(4)                             #1D array, give single value in ()


# In[93]:


np.ones((3,4))                         #2D array, give value in ((tuple)) with tuple inside it  3rows 4colms


# **np.linspace()**

# In[94]:


#notes
#number of points you want
# np.linspace(start,stop,stepsize)
#one bracket [ shows its 1D
#two brackets [[ shows its 2D
np.linspace(0,5,10)


# **Identity matrix using NumPy**

# In[ ]:


#notes
#its a useful matrix when dealing with linear algebra problems
#its basically a 2D square matrix, meaning number of rows and colums are same and have diagonal of ones that everything else
#is zeros
#matrix must be square as the output
#uses np.eye()


# In[96]:


np.eye(4)


# **Arrays of random numbers**

# In[ ]:


#Notes
# np.random.rand()  put value in () according to the dimension you want
# it gives random numbers
# np.random.randint()   integers from lower to higher number


# In[97]:


np.random.rand(5)


# In[98]:


np.random.rand(5,5)


# In[99]:


np.random.randn(2)


# In[100]:


np.random.randn(4,4)


# In[101]:


np.random.randint(1,100)


# In[102]:


np.random.randint(1,100,10)


# **Useful attributes and methods of an array**

# In[13]:


arr = np.arange(25)


# In[14]:


arr


# In[5]:


ranarr = np.random.randint(0,50,10)


# In[6]:


ranarr


# **reshape() method**

# In[11]:


#notes
# .reshape() reshapes same data


# In[7]:


arr.reshape(5,5)


# **Methods to find max or min values**

# In[8]:


ranarr.max()   #.max() method


# In[9]:


ranarr.min()    #.min() method 


# In[10]:


ranarr.argmax()       #.argmax()  gives index location of max value


# In[11]:


ranarr.argmin()       #.argmin()   gives index location of min value


# In[12]:


arr.shape             #.shape to get shape 


# In[17]:


arr = arr.reshape(5,5)


# In[18]:


arr.shape


# In[19]:


arr.dtype                  #.dtype to get the data type


# **NumPy Array Indexing**

# **Numpy Indexing and Selection**

# In[20]:


import numpy as np


# In[21]:


arr = np.arange(0,11)


# In[22]:


arr


# In[23]:


arr[8]                  #arr[index_number] 


# In[24]:


arr[1:5]


# In[25]:


arr[0:5]


# In[26]:


arr[:6]


# In[27]:


arr[5:]


# In[28]:


arr[0:5] = 100           #here this will set all the first five values as 100


# In[29]:


arr


# In[30]:


arr = np.arange(0,11)


# In[31]:


arr


# In[34]:


slice_of_arr = arr[0:6]


# In[35]:


slice_of_arr


# In[36]:


slice_of_arr[:] = 99       # : means grabbing everything in slice_of_arr


# In[37]:


slice_of_arr


# In[38]:


arr


# In[39]:


arr_copy = arr.copy()                #.copy() to copy the values of one variable to another


# In[40]:


arr


# In[41]:


arr_copy[:] = 100


# In[42]:


arr_copy


# In[43]:


arr


# **Indexing a 2D array / Matrix**

# In[3]:


import numpy as np


# In[5]:


arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])


# In[6]:


arr_2d


# In[8]:


#double bracket format to get the value
#grab digit 5
arr_2d[0][0]      #[1st row][1st column]


# In[9]:


#double bracket format to get the value 
#grab digit 25
arr_2d[1][1]


# In[10]:


#double bracket format to get the value
#grab digit 40
arr_2d[2][1]         #this is called slice notation


# In[11]:


#single bracket format to get the value
#to get digit 30
arr_2d[1,2]                     #[row,column]


# In[12]:


#to get submatracies from the matrix
#use : 
arr_2d[:2,1:]  #[everything upto row 2 but not row 2, column 1 onwards]      #this is called slice notation


# In[13]:


arr_2d[1:]             #row 1 onwards


# **Conditional selection**

# In[ ]:


#Notes
# by comparing the array with a value we get boolean values
# getting the array and using a comparison operator on it will give o/p as boolean values
# here you get the result where the boolean value is only True
# here we are using the bool_arr as an index to the original arr , we get values as True boolean             
# whenever an array is compared to a value using a comparison operator, the output values as True boolean values


# In[14]:


arr = np.arange(1,11)


# In[15]:


arr


# In[16]:


arr > 5                  #by comparing the array with a value we get boolean values
                         #getting the array and using a comparison operator on it will give o/p as boolean values


# In[17]:


bool_arr = arr > 5


# In[18]:


bool_arr


# In[19]:


#Conditional Selection
arr[bool_arr]                    #here you get the result where the boolean value is only True
                                 #here we are using the bool_arr as an index to the original arr , we get values as True boolean                       


# In[20]:


arr[arr > 5]              #same result but shortcut method 


# In[21]:


arr[arr < 3]                #arr values less than 3


# In[22]:


arr_2d = np.arange(50).reshape(5,10)


# In[23]:


arr_2d


# In[25]:


arr_2d[2:4,0:6]


# In[26]:


arr_2d[1:3,3:5]


# **NumPy Operations**

# - **Array with Array**
# - **Array with Scalers**
# - **Universal Array Functions**

# In[27]:


arr = np.arange(0,11)


# In[28]:


arr


# In[29]:


#adding two arrays together with + operator
arr + arr


# In[30]:


#subtracting two arrays together with - operator
arr - arr


# In[31]:


#multiplying two arrays together with * operator
arr * arr


# **Array with Scaler**

# In[ ]:


#Notes
# Scaler means just a single number
# that number will be broadcasted to every value in that array


# In[32]:


arr


# In[33]:


arr + 100


# In[34]:


arr * 100


# In[35]:


arr - 100


# In[36]:


arr / arr      #numpy will give warning but not error. It will gives nulls


# In[37]:


1 / arr


# In[38]:


arr ** 2


# **Universal Array Functions**

# In[ ]:


#Notes
# np.sqrt(variable / array) for square root
# np.exp(variable / array) for exponental value
# np.sqrt(variable / array) for square root


# In[39]:


np.sqrt(arr)        # np.sqrt(variable / array) for square root


# In[40]:


np.exp(arr)           # np.exp(variable / array) for exponental value


# In[41]:


np.max(arr)         # np.max(variable / array) for max value


# In[42]:


np.sin(arr)           # np.sin(variable / array) for trignometric values


# In[43]:


np.log(arr)


# **Python for Data Analysis - Pandas**

# - Pandas is an open source library built on top on NumPy
# - Uses are data cleaning and preparation
# - conda install pandas
# - pip install pandas

# **Series**

# In[ ]:


#Notes
# it is a data type 
# it is similar to numpy array
# it has access to labels
# pd.Series()
# pd.Series(variable, index)   <-one of the syntax
# to grab information from the series  #Syntax->        series_variable_name[index]
# in NumPy and Pandas the integers will be converted in float so that you do not loose information 


# In[44]:


import pandas as pd
import numpy as np


# In[45]:


labels = ['a','b','c']                          #list
my_data = [10,20,30]                            #list
arr = np.array(my_data)                         #array
d= {'a':10,'b':20,'c':30}                       #dictionary


# In[46]:


labels


# In[47]:


my_data


# In[48]:


arr


# In[49]:


d


# In[50]:


pd.Series(data = my_data)       #here in output we get 0,1,2 as index and 10,20,30 as values in my_data which are stored in data


# In[51]:


pd.Series(data = my_data, index = labels)        #here we put the list labels as index with the help of pd.Series()


# In[52]:


pd.Series(my_data,labels)


# In[53]:


pd.Series(arr)


# In[54]:


pd.Series(arr,labels)


# In[55]:


pd.Series(d)    #series will automatically take the keys as index


# In[57]:


pd.Series(labels)


# In[58]:


pd.Series([sum,print,len])            #this is holding refrences for built in functions. eg 0 index is reference for sum ,etc


# In[ ]:


#how to use Index from Series
# most commonly used for fast lookups


# In[59]:


#creating series variable
ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])     #here we are creating a series. 1,2,3,4 as values and USA, 
                                                                 #Germany, USSR, Japan as indexes


# In[60]:


ser1


# In[61]:


#creating series variable
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])


# In[62]:


ser2


# In[63]:


#now grabbing information from the series
ser1['USA']                         #Syntax->        series_variable_name[index]


# In[68]:


#creating series variable
ser3 = pd.Series(labels)


# In[69]:


ser3


# In[70]:


ser3[2]


# In[72]:


ser1 + ser2     #this will try to match the values in both series_variable by the index and will add the values corresponding
                #to the index
                #if there is no match it will put a NULL


# **DataFrames - Part 1**

# In[ ]:


#Notes
# main tool for working with pandas

# syntax->    pd.DataFrame(data, row, column)

# type() to get the type of data / variable 

# A dataframe is a bunch of series that share the same index

# to grab values from rows and columns   #Syntax->        df['column_name'] 

# to get multiple columns you have to pass a list inside df[] and write the column names #Syntax->    df[['column1','column2']]

# creating a new column:
# here first we write the df['new_column_name'] and then equal it to existing columns. And add it in existing df[] like 
# df['W'] + df['Y']

# to remove columns:
# here we use .drop() and Syntax ->  df.drop('column_name', axis = 0 or 1) axis = 0 refers to rows, axis = 1 refers to columns

# When inplace is False changes are done temporary not actually, when inplace is True the changes are permanenet. 

# to remove rows:
# df.drop('row name or number', axis  = 0)

# df.shape     gives  rows (referred as 0 axis) , columns  (referred as 1 axis)

# selecting Rows:
# two ways to get rows , we have to call some methods
# 1st method based on actual row name with     df.loc[row_name]
# 2nd method based on index position with      df.iloc[index_number]


# In[6]:


import numpy as np
import pandas as pd


# In[11]:


from numpy.random import randn


# In[8]:


#seed means same random number


# In[12]:


np.random.seed(101)


# In[14]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])   #here 5,4 is     5 rows, 4 columns


# In[15]:


df                    #here W,X,Y,Z are all pandas series with shared index as (rows) A,B,C,D,E


# **To grab values from rows and columns**

# In[16]:


df['W']   #Syntax-> df['column_name']   


# In[17]:


type(df)


# In[18]:


df.W        #this works but don't use this way , use the above one to get values


# In[19]:


df[['W','Z']]           #to get multiple columns you have to pass a list inside df[] and write the column names
                        #Syntax->        df[['column1','column2']]


# **Creating a new column in DataFrame**

# In[20]:


# here first we write the df['new_column_name'] and then equal it to existing columns. And add it in existing df[] like 
# df['W'] + df['Y']
df['new'] = df['W'] + df['Y']


# In[21]:


df


# **To remove columns in DataFrame**

# In[22]:


# here we use .drop() and Syntax ->  df.drop('column_name', axis = 0 or 1) axis = 0 refers to rows, axis = 1 refers to columns
df.drop('new', axis = 1)    


# In[23]:


df     #here df still has new column because inplace is False, when inplace is True the changes are permanenet. See below now


# In[24]:


df.drop('new', axis = 1, inplace = True)


# In[25]:


df


# In[26]:


#to drop rows
df.drop('E', axis = 0)


# In[27]:


df


# In[28]:


df.shape         #5 rows , 4 columns


# **Selecting Rows in DataFrame**

# In[29]:


# two ways to get rows , we have to call some methods

# 1st method based on actual row name with df.loc[row_name]
df.loc['A']


# In[30]:


# 2nd method based on index position with df.iloc[index_number]  here 2 is nothing but row 'C'
df.iloc[2]


# **Selecting subsets of rows and columns in DataFrame**
# 

# In[ ]:


#Notes
# to select subsets of rows and columns in DataFrame we use:      df.loc[row,column]
# to get multiple values we take:  df.loc[[list of rows],[list of columns]]


# In[31]:


df.loc['B','Y']     


# In[32]:


df


# In[33]:


df.loc[['A','B'],['W','Y']]   #to get multiple values we take:  df.loc[[list of rows],[list of columns]]


# **DataFrames - Part 2**

# In[1]:


import pandas as pd
import numpy as np
from numpy.random import randn


# In[2]:


np.random.seed(101)


# In[3]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[4]:


df


# **Conditional Selection**

# In[ ]:


#Notes
# Conditional Selection using bracket notation
# we get boolean values in the result


# In[5]:


df > 0                                           #we get boolean values in the result


# In[6]:


booldf = df > 0


# In[7]:


booldf


# In[8]:


#passing booldf in original df inside square []
# here we get values in numbers which are True are NaN which are False
df[booldf]


# In[9]:


#return a subset of a dataframe based on a condition
df[df > 0]         


# In[10]:


df


# In[11]:


df['W'] > 0


# In[12]:


df['W']                 #here in above C is False and here below C is -2. Above we gave condition that df['w'] should be greater
                        #than 0. Thats why we get false because value is -2


# In[13]:


#grab all rows in dataframe where W > 0
df[df['W'] > 0]     #here you dont get null values because df['W'] > 0 is put in df[]. for W column


# In[14]:


#grab all rows in dataframe where Z < 0
df[df['Z'] < 0]


# In[15]:


resultdf = df[df['W'] > 0]


# In[16]:


resultdf            #same as df[df['W'] > 0]


# In[17]:


resultdf['X']


# In[18]:


# shortcut method for above operation
df[df['W'] > 0]['X']                         #grabbing X column with W column where rows with W column are more than 0


# In[19]:


df[df['W'] > 0][['X','Y']]       #to grab multiple columns, pass it in a list


# In[33]:


boolseries = df['W'] > 0
result = df[boolseries]


# In[34]:


boolseries


# In[35]:


result


# In[36]:


result[['X','Y']]     #now pass the columns you want in a list manner


# **Multiple Conditions**

# In[ ]:


#Notes
# And operator takes only one boolean values
# for multiple conditions use ( ) and write condition in each ( )
# to compare multiple conditions we use:       &
# for OR operator we do not use OR we use:     |


# In[37]:


df[ (df['W'] > 0) & (df['Y'] > 1) ]


# In[38]:


df[(df['W']>0) | (df['Y']>1)]


# **Resetting the index**

# In[ ]:


#Notes
# in order to reset index we use method called:       .reset_index()
# this resets the index values to numerical values
# but this does not make changes to original dataframe

# to make changes to original dataframe we use inplace = true inside .reset_index(inplace = True)


# In[39]:


df


# In[40]:


df.reset_index()         #making the index in numerical values by using:     .reset_index()   method


# In[ ]:


#setting the index
#to make a column an index
# .split() method makes the values store inside a list as result


# In[ ]:


#Notes
# to make a column an index we use:  .set_index(pass the column name here to make it index)


# In[41]:


#making a new column by passing strings and spliting the white spaces and storing it in a variable which becomes a list in output
newind = 'CA NY WY OR CO'.split()


# In[42]:


newind


# In[43]:


#maing a new column States and passing it in dataframe[] and equaling it to values present as list in newind variable
df['States'] = newind


# In[44]:


df


# In[45]:


df.set_index('States')           #to make a column an index we use:  .set_index(pass the column name here to make it index)   
                                 #                                                 this becomes the index
                                 #to make permanent changes to index we use .set_index(column_name, inplace = True)   


# In[46]:


df


# **DataFrames - Part 3**

# **Multi Index**

# In[17]:


import numpy as np
import pandas as pd
from numpy.random import randn


# In[18]:


#index levels
outside = ['G1','G1','G1','G2','G2','G3']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))    #making a list and zipping it (making it tuple) by zip function inside list function
hier_index = pd.MultiIndex.from_tuples(hier_index) #pd.MultiIndex.from_tupples


# In[19]:


outside


# In[20]:


inside


# In[21]:


list(zip(outside,inside))


# In[22]:


hier_index


# In[23]:


df = pd.DataFrame(randn(6,2),hier_index,['A','B'])     #randn(no_of_rows, no_of_columns)


# In[24]:


df


# In[25]:


df.loc['G1']           #calling outside index with the help of:      .loc[index_name]


# In[26]:


df.loc['G1'].loc[1]     #calling inside of insde index with the help of:          .loc[index_name].loc[index_name]


# In[27]:


#to name index


# In[ ]:


#Notes
# to name indexes we use:     .index.names
# we use .index.names and pass the names what we want in a list 
# that means we:    df.index.names = ['Groups', 'Num']
# here groups and Num are self made names. Groups name is for outside index and Num name is for inside index


# In[28]:


df.index.names


# In[29]:


df.index.names = ['Groups', 'Num']


# In[30]:


df


# In[31]:


# to grab value 0.074472 in G2 , B
# syntax->                     #here it is df.loc['outsideindex'].loc[insisdeindex][columnname]
df.loc['G2']


# In[33]:


df.loc['G2'].loc[2]


# In[35]:


df.loc['G2'].loc[2]['B']     #here it is df.loc['outsideindex'].loc[insisdeindex]['columnname']


# In[36]:


#to grab value 0.432089                   #here it is df.loc['outsideindex'].loc[insisdeindex]['columnname']
df.loc['G1'].loc[3]['B']


# **Cross Section function**

# In[37]:


#notes
# cross section function:          .xs()
# used when we have multi level index

# to grab multiple values from same inside index but different outside index we use xs
# syntax->          df.xs(inside_index_number, levels = "Inside_index_name")


# In[38]:


#grab everything under G1 by cross section function
df.xs('G1')


# In[39]:


#grab inside index values of both the 1s in G1 and G2 
df.xs(1, level = 'Num')         #syntax->          df.xs(inside_index_number, levels = "Inside_index_name")


# **Missing Data**

# In[40]:


#Notes
# Missing datas are filled with Null or NaN values

# methods such as .dropna() or .fillna() are used to drop or fill those missing values

# we can also create dataframe from a dictionary as well

# np.nan to signify null or missing values


# In[41]:


import pandas as pd
import numpy as np


# In[42]:


#creating a dataframe from a dictionary
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}   #here keys will be columns 


# In[43]:


df = pd.DataFrame(d)


# In[44]:


df


# **.dropna() method**

# In[ ]:


#Notes
# .dropna() will drop any row with any single or one or more missing values
# axis = 0 means it will operate on rows and it is be default
# axis = 1 means it will operate on columns. Syntax->      .dropna(axis=1)

# thresh = 
# here thresh is nothing but it helps to keep that many Non Null values in the dataframe
# meaning that if we set thresh = 2, then the rows with 2 non null values will not be dropped


# In[45]:


df.dropna()               #here all the rows with missing values are dropped


# In[46]:


df.dropna(axis=1)        #here all the columns with missing values are dropped when we set axis = 1


# In[47]:


df.dropna(thresh = 2)   # here thresh is nothing but it helps to keep that many Non Null values in the dataframe
                        # meaning that if we set thresh = 2, then the rows with 2 non null values will not be dropped


# **.fillna() method**

# In[ ]:


#Notes
# used for replacing or filling the null nan values
# syntax->                  .fillna(value = )

# you can also fill it by mean


# In[48]:


df.fillna(value = 'FILL VALUE')


# In[ ]:


#filling the null value by mean


# In[49]:


df['A']


# In[51]:


df['A'].fillna(value = df['A'].mean()) #here df['A'].mean() gives mean of A column and that we are storing in value in .fillna()


# **Groupby**

# In[52]:


#Notes
# Groupby allows you to group together rows based off of a column and perform an aggregate function on them
# grouping the common columns and summing  the rows

# Syntax->      .groupby('columnname')
# 1. Store this in a variable example:                              company = df.groupby('Columname')
# 2. then call an aggregate function on that variable example:      company.mean()
#    this mean does not work on strings remember
# example:           df.groupby('columnname').sum()


# ![sgCn1.jpg](attachment:sgCn1.jpg)

# In[54]:


data = {'Company': ['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person': ['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350] }


# In[55]:


df = pd.DataFrame(data)


# In[56]:


df


# In[57]:


#grouping by company


# In[60]:


df.groupby('Company')           # Syntax->      .groupby('columnname')


# In[62]:


byComp = df.groupby('Company')


# In[63]:


byComp.mean()            #taking mean of sales of companies


# In[64]:


byComp.sum()            #taking sum of sales of companies


# In[65]:


byComp.std()          #taking standard deviation of sales of companies


# In[66]:


byComp.sum().loc['FB']         #taking the sum of sales of company FB and calling it 


# In[67]:


df.groupby('Company').sum().loc['FB']   #direct method shortcut method:         df.groupby('columnname').sum().loc['columname']


# In[69]:


df.groupby('Company').count()         #.count()   counts the number of instances for columns


# In[70]:


df.groupby('Company').max()          #.max() gives maximum values


# In[71]:


df.groupby('Company').min()               #.min() gives minimun values


# In[72]:


df.groupby('Company').describe()     #.describe() method gives all the information below


# **Merging, Joining and Concatenating**

# In[73]:


#Notes
# There are 3 main ways of combining DataFrames together: 
# Merging, Joining and Concatenating.


# In[74]:


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])


# In[75]:


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 


# In[76]:


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


# In[77]:


df1


# In[78]:


df2


# In[79]:


df3


# **Concatenation**

# In[80]:


#Notes
# Concatenation basically glues together DataFrames.
# Keep in mind that dimensions should match along the axis you are concatenating on. 
# You can use pd.concat and pass in a list of DataFrames to concatenate together:


# In[81]:


pd.concat([df1,df2,df3])      # passing all the dataframes in a list inside pd.concat([])   
                              # here by default the axis = 0 which means joining is done on rows


# In[82]:


pd.concat([df1,df2,df3],axis=1)  #axis = 1 means joining along the columns


# In[83]:


#example
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})  


# In[84]:


left


# In[85]:


right


# **Merging**

# In[86]:


#Notes
# The pd.merge() function allows you to merge DataFrames together using a similar logic as merging SQL Tables together.


# In[87]:


pd.merge(left,right,how='inner',on='key')   # meaning syntax->  pd.merge(df1,df2,how = 'inner', on = 'columnname')
                                            # how = 'inner' is by default. 
                                            #It means we want inner join


# In[88]:


# complicated example
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})


# In[89]:


pd.merge(left, right, on=['key1', 'key2'])      # pd.merge(df1, df2, on = ['colum1', 'colum2'])   for multiple columns with
                                                # by placing the columns in a list


# In[90]:


pd.merge(left, right, how='outer', on=['key1', 'key2'])


# In[91]:


pd.merge(left, right, how='right', on=['key1', 'key2'])


# In[92]:


pd.merge(left, right, how='left', on=['key1', 'key2'])


# **Joining**

# In[93]:


#Notes
# Joining is a convenient method for combining the columns of two potentially differently-indexed DataFrames into a
# single result DataFrame.
# here keys are at index instead in a column

# syntax->   df1.join(df2)                 this will do an inner join

# syntax->  df.join(df2, how = 'outer')    this will do outer join


# In[94]:


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])


# In[95]:


left.join(right)               # syntax->   df1.join(df2)   meaning this will do an inner join


# In[96]:


left.join(right, how='outer')    # syntax->  df.join(df2, how = 'outer')    this will do outer join


# **Operations**

# In[97]:


#Notes
# Operations on pandas and other operations


# In[98]:


df = pd.DataFrame({'col1': [1,2,3,4],
                   'col2': [444,555,666,444],
                   'col3': ['abc','def','ghi','xyz']})


# In[99]:


df.head()


# In[100]:


# finding unique values in a dataframe

#Notes
# 1)    .unique() method to find unique values
# 2)    to get number of unique value with len() function
# 3)    .nunique() method to get number of unique values
# 4)    .value_counts() method returns how many times each value occurs in a dataframe


# In[101]:


# all unique values in column 2
df['col2'].unique()                 #.unique() method to find unique values


# In[102]:


len(df['col2'].unique())         # to get number of unique value with len() function


# In[103]:


df['col2'].nunique()           # .nunique() to get number of unique values


# In[104]:


df['col2'].value_counts()           # .value_counts() method returns how many times each value occurs in a dataframe


# **Selecting Data**

# In[125]:


df


# In[106]:


df[df['col1'] > 2]


# In[108]:


df['col1'] > 2


# In[109]:


df[(df['col1'] > 2) & (df['col2'] == 444)]       # this is called conditional selection


# **.apply() method**

# In[110]:


#Notes
# .apply() is powerful when you combine it with lambda expresssion


# In[111]:


def times2(x):
    return x*2  
# here this means, a function times2 takes a value x and returns x*2


# In[112]:


df['col1'].sum()


# In[113]:


# now to apply your own custom function on dataframe by using .apply() method
df['col1'].apply(times2)            #syntax->      .apply(your_own_function)


# In[115]:


df['col3'].apply(len)      # .apply() method to get length of each string using len inside .apply()


# In[116]:


len(df['col3'])


# In[117]:


# lambda expression inside .apply()


# In[118]:


df['col2'].apply(lambda x: x*2)


# In[119]:


#removing columns


# In[120]:


df.drop('col1', axis =1)


# In[127]:


# to get columns and index names of a dataframe
df.columns


# In[128]:


# to get index of a dataframe
df.index


# **Sorting and ordering a DataFrame**

# In[ ]:


#Notes
# to sort columns in dataframe we use .sort_values() method 
# syntax->        .sort_values('columnname')

# to find null values in dataframe we use .isnull() method
# syntax->         .isnull()
# this gives the dataframe and values in boolean, false means values are there, True means value is null


# In[129]:


df


# In[130]:


# sorting by column 2 
df.sort_values('col2')  # syntax->        .sort_values('columnname')


# In[131]:


# to find null values in dataframe
df.isnull()             # syntax->         .isnull()
                        # this gives the dataframe and values in boolean, false means values are there, True means value is null


# **Pivot table method/function**

# In[ ]:


#Notes
# .pivot_tables()
# dataframe.pivot_tables(values, index, columns)    takes 3 arguments inside (values, index, columns)


# In[133]:


data = {'A': ['foo','foo','foo','bar','bar','bar'],
        'B': ['one','one','two','two','one','one'],
        'C': ['x','y','x','y','x','y'],
        'D': [1,3,2,5,4,1] }


# In[134]:


df = pd.DataFrame(data)


# In[135]:


df


# In[136]:


#creating a pivot table
# syntax->                 .pivot_tables()
#                          dataframe.pivot_tables(values, index, columns)    takes 3 arguments inside (values, index, columns)
df.pivot_table(values = 'D', index = ['A','B'], columns = ['C'])
# here we are taking values to be inside of pivot table from column D
# taking two indexes values from column A and column B
# and actuals columns values to be defined from column C


# **Data Input and Output**

# In[1]:


#  dealing with csv files , html files , excel files , sql files etc


# In[ ]:


# installing required libraries


# In[2]:


pip install sqlalchemy


# In[3]:


pip install lxml


# In[4]:


pip install html5lib


# In[5]:


pip install BeautifulSoup4


# **Read and Write files with Pandas**

# In[1]:


import pandas as pd


# In[2]:


# Notes
# files should be in the same location of Jupyter


# **Open / Read CSV files**

# In[ ]:


#Notes
# Syntax->             pd.read_csv('file and file path')


# **Open / Read any files**

# In[5]:


#Notes
# syntax->             pd.read_shift + Tab('file and file path')              when you do the shift + tab after _ you will get 
#                                                                              a dropdown of option of files to choose from.


# **To write in a csv file**

# In[6]:


#Notes
# 1. we need to store it in a dataframe first

# example:
# df = pd.read_csv('example.csv')
# df
# df.to_shift + tab                here you will get drop down of options of file types to choose from 
# df.to_csv('My_output', index = False)


# **Reading and Writing from Excel files**

# In[7]:


#Notes
# pandas can only import the data
# each sheet in excel is taken as a dataframe in python
# syntax-> pd.read_excel('file_path',sheet_name = 'Sheet1')   if the excel files has multiple sheets, choose the sheet you want
#                                                             in sheet_name to be displayed 


# In[9]:


# Reading excel file
pd.read_excel('E:/Udemy- Python for Data Science and Machine Learning/Py-DS-ML-Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/Excel_Sample.xlsx')


# In[7]:


# to access Sheet 1 in excel
df = pd.read_excel('E:/Udemy- Python for Data Science and Machine Learning/Py-DS-ML-Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/Excel_Sample.xlsx',sheet_name = 'Sheet1')


# In[17]:


df.to_excel('Excel_Sample2.xlsx', sheet_name = 'NewSheet')


# **Working with HTML**

# In[19]:


#Notes
# HTML input
# Pandas read_html function will read tables off of a webpage and return a list of DataFrame objects
# syntax->        pd.read_html('link')

# df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')


# In[3]:


#df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')


# **Working with SQL**

# **Notes**<br>
# The pandas.io.sql module provides a collection of query wrappers to both facilitate data retrieval and to reduce dependency on DB-specific API. Database abstraction is provided by SQLAlchemy if installed. In addition you will need a driver library for your database. Examples of such drivers are psycopg2 for PostgreSQL or pymysql for MySQL. For SQLite this is included in Python’s standard library by default. You can find an overview of supported drivers for each SQL dialect in the SQLAlchemy docs.
# 
# If SQLAlchemy is not installed, a fallback is only provided for sqlite (and for mysql for backwards compatibility, but this is deprecated and will be removed in a future version). This mode requires a Python database adapter which respect the Python DB-API.
# 
# See also some cookbook examples for some advanced strategies.
# 
# **The key functions are:**
# 
# **Read SQL database table into a DataFrame.**
# read_sql_table(table_name, con[, schema, ...])
# 
# **Read SQL query into a DataFrame.**
# read_sql_query(sql, con[, index_col, ...])
# 
# **Read SQL query or database table into a DataFrame.**
# read_sql(sql, con[, index_col, ...])
# 
# **Write records stored in a DataFrame to a SQL database.**
# DataFrame.to_sql(name, con[, flavor, ...])
# 

# In[4]:


from sqlalchemy import create_engine


# In[5]:


engine = create_engine('sqlite:///:memory:')      # temporary database created which is running in memory


# In[10]:


df.to_sql('my_table1', engine)


# In[11]:


sqldf = pd.read_sql('my_table1' , con=engine)


# In[12]:


sqldf


# **Python for Data Analysis - Pandas Exercises**

# **SF Salaries**

# In[13]:


import pandas as pd


# In[14]:


# Read Salaries.csv as a dataframe called sal.
sal = pd.read_csv('E:/Udemy- Python for Data Science and Machine Learning/Py-DS-ML-Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises\Salaries.csv')


# In[15]:


# Check the head of the DataFrame. 
sal.head()


# In[16]:


# Use the .info() method to find out how many entries there are.
sal.info()


# In[21]:


# What is the average BasePay ?
# average means taking .mean()
sal['BasePay'].mean()


# In[23]:


# What is the highest amount of OvertimePay in the dataset ? 
sal['OvertimePay'].max()


# In[69]:


# What is the job title of JOSEPH DRISCOLL ? 
# Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll).
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']


# In[70]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# In[76]:


#  How much does JOSEPH DRISCOLL make (including benefits)? 
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# In[78]:


# What is the name of highest paid person (including benefits)?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']


# In[83]:


sal.loc[sal['TotalPayBenefits'].argmax()]


# In[81]:


# What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']


# In[82]:


sal.loc[sal['TotalPayBenefits'].argmin()]


# In[91]:


#  What was the average (mean) BasePay of all employees per year? (2011-2014) ? 
sal.groupby('Year').mean()['BasePay']


# In[63]:


#  How many unique job titles are there? 
len(sal['JobTitle'].unique())


# In[93]:


sal['JobTitle'].nunique()     #nunque = no. of uniques


# In[94]:


#  What are the top 5 most common jobs? 
sal['JobTitle'].value_counts().head(5)     

# value_counts() function returns object containing counts of unique values.
# The resulting object will be in descending order so that the first element is the most frequently-occurring element.


# In[100]:


#  How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) 
sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)


# In[114]:


#  How many people have the word Chief in their job title? (This is pretty tricky) 
def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False 
    # watch video 12:40 of 37. SF Solutions 


# In[115]:


sum(sal['JobTitle'].apply(lambda x: chief_string(x)))


# In[117]:


# Bonus: Is there a correlation between length of the Job Title string and Salary? 
sal['title_len'] = sal['JobTitle'].apply(len)


# In[120]:


sal[['TotalPayBenefits','title_len']].corr()


# **Ecommerce Purchases**

# In[1]:


# Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom
import pandas as pd 
ecom = pd.read_csv('E:/Udemy- Python for Data Science and Machine Learning/Py-DS-ML-Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Ecommerce Purchases.csv')


# In[2]:


# Check the head of the DataFrame.
ecom.head()


# In[4]:


# How many rows and columns are there?
ecom.shape


# In[14]:


ecom.info()


# In[11]:


# What is the average Purchase Price?
ecom['Purchase Price'].mean()


# In[12]:


# What were the highest and lowest purchase prices?
ecom['Purchase Price'].max()


# In[13]:


ecom['Purchase Price'].min()


# In[19]:


# How many people have English 'en' as their Language of choice on the website?
ecom[ecom['Language'] == 'en'].count()


# In[20]:


# How many people have the job title of "Lawyer" ?
ecom[ecom['Job'] == 'Lawyer'].count()


# In[21]:


ecom[ecom['Job'] == 'Lawyer'].info()


# In[27]:


# How many people made the purchase during the AM and how many people made the purchase during PM ? 

# (Hint: Check out value_counts() )
ecom['AM or PM'].value_counts() 


# In[24]:


# What are the 5 most common Job Titles?
ecom['Job'].value_counts().head()


# In[29]:


# Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
ecom[ecom['Lot'] == '90 WT']['Purchase Price']


# In[44]:


#  What is the email of the person with the following Credit Card Number: 4926535242672853 
ecom[ecom['Credit Card'] == 4926535242672853]['Email']


# In[49]:


# How many people have American Express as their Credit Card Provider *and made a purchase above $95 ?
len(ecom[(ecom['CC Provider'] == 'American Express')    &     (ecom['Purchase Price'] > 95)])


# In[50]:


ecom[(ecom['CC Provider'] == 'American Express')    &     (ecom['Purchase Price'] > 95)].count()


# In[53]:


# Hard: How many people have a credit card that expires in 2025?
ecom[ecom['CC Exp Date'].apply(lambda x: x[3:] == '25')].count()   #watch video 39, 12:10 timestamp


# In[54]:


len(ecom[ecom['CC Exp Date'].apply(lambda x: x[3:] == '25')])


# In[66]:


# Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)

#solution
# example_email = ecom['Email'].iloc[0]
# example_email                   <- this will give output as 'abc@gmail.com'
# example_email.split('@')        <- this returns a list as ['abc', 'gmail.com']
# now here since 'gmail.com' in the list is at index[1] we split the email and take index 1 value which is gmail, see below
ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head()    #watch video 39, 13:00 timestamp


# **Python for Data Visualization - Matplotlib**

# It is a plotting library<br>
# It is similar to MatLab graphical plotting<br>
# Works very well Pandas and NumPy<br>
# <br>
# conda install matplotlib<br>
# pip install matplotlib<br>

# **Matplotlib Part 1**

# In[6]:


#Notes
# import matplotlib.pyplot as plt      # importing matplotlib pyplot module
# %matplotlib inline                  <-to see the plots inside jupyter notebook

# matplotlib commands allows to create a plot

# .plot() is a method to get the plot , '-r ' means red color

# plt.xlabel() to print x label down
# plt.ylabel() to print y label left side
# plt.title()  to print the Title on top

# plt.subplot(no_of_rows, no_ of_columns, plot_number)


# In[3]:


import matplotlib.pyplot as plt      # importing matplotlib pyplot module


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


import numpy as np


# In[7]:


x = np.linspace(0,5,11)          # which means it is going to be linearly spaced from 0 to 5 and grab 11 points


# In[8]:


y = x**2


# In[9]:


x


# In[10]:


y


# **Functional method to create a plot**

# In[21]:


plt.plot(x,y,)  # here .plot() is a method to get the plot  , '-r ' means red color
plt.xlabel('X label')          # plt.xlabel() to print x label down
plt.ylabel('Y label')          # plt.ylabel() to print y label left side
plt.title('Title')             # plt.title()  to print the Title on top


# In[ ]:


# Multiplots on same canvas


# In[22]:


plt.subplot(1,2,1)            # plt.subplot(no_of_rows, no_ of_columns, plot_number)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')


# **Matplotlib Object Oriented API Method**

# This means we will instantiate figure objects and then call methods or attributes from that object.

# **Object Oriented API Method**

# The main idea in using the more formal Object Oriented method is to create figure objects and then just call methods or attributes off of that object.<br>
# This approach is nicer when dealing with a canvas that has multiple plots on it.

# In[32]:


# 1.
# figure object. think it is a blank canvas      # Create Figure (empty canvas)
fig = plt.figure()           # storing plt.figure() method in fig variable which becomes an object

# 2.
# Add set of axes to figure
# method    .add_axes([])
axes = fig.add_axes([0.1,0.1,0.8,0.8])         # left, bottom, width, height (range 0 to 1)  takes it in a list

# 3.
# Plot on that set of axes
axes.plot(x,y)
axes.set_xlabel('X label')        # set_xlabel()  method
axes.set_ylabel('Y label')        # set_ylabel()  method
axes.set_title('Set Title')       # set_title()  method


# In[35]:


# Creates blank canvas
fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])          # all these values here must be between 0 and 1

axes1.plot(x,y)
axes1.set_title('Larger Plot')

axes2.plot(y,x)
axes2.set_title('Smaller Plot')


# **Matplotlib Part 2**

# **Subplots**

# In[ ]:


# Notes
# plt.subplots() object will act as a more automatic axis manager.
# plt.tight_layout()     this makes the plot look arranged
# fig and axes are already taken in subplots
# fig, axes = plot.subplots(nrows = , ncols = )


# axes are already added in subplots | but not in plt.figure()  here you have to manually add axes |


# In[38]:


fig, axes = plt.subplots()      # here fig is blank canvas we created above , and axes are also created above. we are calling it
                                # directly


# In[41]:


fig,axes = plt.subplots(nrows = 1, ncols =2)   #also its calling axes automatically


# In[42]:


fig, axes = plt.subplots(nrows = 3, ncols = 3)


# In[43]:


fig, axes = plt.subplots(nrows = 3, ncols = 3)
plt.tight_layout()    # this makes the plots look arranged


# In[45]:


fig, axes = plt.subplots(nrows = 1 , ncols = 2)    # here axes is nothing but array and list  , we can also iterate  through it 
for current_ax in axes:
    current_ax.plot(x,y)


# In[51]:


# we can also select any particular axes in subplots
fig, axes = plt.subplots(nrows = 1, ncols = 2)
axes[0].plot(x,y)
axes[0].set_title('First Plot ')


# In[52]:


fig, axes = plt.subplots(nrows = 1, ncols = 2)
axes[1].plot(x,y)
axes[1].set_title('Second Plot')


# **Figure Size, Aspect Ratio and DPI**

# Notes:<br>
# Matplotlib allows the aspect ratio, DPI and figure size to be specified when the Figure object is created. You can use the **figsize** and **dpi** keyword arguments.<br>
# - **figsize** is a tuple of the width and height of the figure in inches
# - **dpi** is the dots-per-inch (pixel per inch)

# In[54]:


#Notes
# figsize = (tuple), dpi = number 


# In[58]:


fig = plt.figure(figsize = (3, 2), dpi = 100)    # figsize = (tuple), dpi = number 
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x,y)


# In[63]:


fig = plt.figure(figsize = (8, 2))     # here we changed the figsize by 8
ax1  = fig.add_axes([0, 0, 1, 1])
ax1.plot(x,y)


# In[62]:


# same thing with subplots
fig, axes = plt.subplots(figsize = (8, 2))
axes.plot(x,y)


# In[64]:


fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8, 2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()


# **To save a figure**

# Matplotlib can generate high-quality output in a number formats, including PNG, JPG, EPS, SVG, PGF and PDF.<br>
# To save a figure to a file we can use the **savefig** method in the Figure class

# In[ ]:


# Notes
# to save figure in jpg, png, pdf syntax->            .savefig('filename.extention')


# In[65]:


fig


# In[67]:


# now to save fig  (our figure)
fig.savefig('my_picture.png', dpi = 100)


# **Legends, labels and titles**

# How decorate a figure with titles, axis labels, and legends.

# **Figure titles**<br>
# A title can be added to each axis instance in a figure. To set the title, use the **set_title** method in the axes instance<br>
# <br>
# **Axis labels**<br>
# Similarly, with the methods set_xlabel and set_ylabel, we can set the labels of the X and Y axes<br>
# <br>
# **Legends**<br>
# You can use the label="label text" keyword argument when plots or other objects are added to the figure, and then using the legend method without arguments to add the legend to the figure<br>
# <br>
# The legend function takes an optional keyword argument **loc** that can be used to specify where in the figure the legend is to be drawn. The allowed values of loc are numerical codes for the various places the legend can be drawn. See the documentation page for details. Some of the most common loc values are:<br>
# <br>
# **Lots of options....**<br>
# <br>
# ax.legend(loc=1) # upper right corner<br>
# ax.legend(loc=2) # upper left corner<br>
# ax.legend(loc=3) # lower left corner<br>
# ax.legend(loc=4) # lower right corner<br>
# <br>
# **Most common to choose**<br>
# ax.legend(loc=0)      # lets matplotlib decide the optimal location<br>

# In[ ]:


#Notes
# syntax to set title->             .set_title('Titlename')

# syntax to set x or y label.>      .set_xlabel('x')       .set_ylabel('Y')

# Legends
# with legends we can use label text to show what plot is what plot 
# to add a legend is a two step process
# 1st step: to call ax.legend at the bottom of your code or where your axes are
# 2nd step: for each plots you will add an argument called label which is a string


# In[70]:


fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x,y)
ax.set_title('Title')
ax.set_xlabel('x')
ax.set_ylabel('y')


# In[78]:


#see this for legend
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x,x**2, label = 'X square')
ax.plot(x,x**3, label = 'X cube')

ax.legend(loc = 0)


# **Matplotlib Part 3**

# **Setting colors, linewidths, linetypes**

# Notes<br>
# to change color:       **color = 'colorname'**         argument inside .plot()<br>
# for thicker liner:     **linewidth = sizenumber**      argument inside .plot()     linewidth can also be written as **lw**<br>
# for transperant line:  **alpha = number**              argument inside .plot()<br>
# for style of line:     **linestyle = '-.-'**           argument instde .plot()     linestyle can also be written as **ls**<br>
# <br>
# **Markers** are used when we have less data points<br>
# **marker = 'o'**    argument inside .plot()   <br>
# it marks the points between the line<br>
# we can also give **markersize = number**<br>
# also we can make the marker point in color for it we use:  **markerfacecolor = 'colorname'**<br>
# to make marker edges thicker:    **markeredgewidth = number**<br>
# marker edge color:  markeredgecolor='colorname'

# In[17]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color = 'orange', linewidth =4, alpha = 0.5, linestyle ='-.', marker = 'o', markersize = 10, markerfacecolor = 'red', markeredgewidth = '3', markeredgecolor = 'black') 
                                                # to change color:       color = 'colorname'         argument inside .plot()
                                                # for thicker liner:     linewidth = sizenumber      argument inside .plot()
                                                # for transperant line:  alpha = number              argument inside .plot()
                                                # for style of line:     linestyle = '-.-'           argument instde .plot()


# **Control over axis appearance**

# In[ ]:


#Notes
# to get the particular portion of axis we use:      .set_xlim([lowerboundnumber, upperboundnumber])  for x 
# to get the particular portion of axis we use:      .set_ylim([lowerboundnumber, upperboundnumber])  for y


# In[20]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color = 'purple', lw = 2, ls = '--')

#to show plot between 0 and 1 axis
ax.set_xlim([0,1])
ax.set_ylim([0,2])


# **Matplotlib Exercises**

# In[23]:


import numpy as np


# In[24]:


x = np.arange(0,100)


# In[26]:


y = x*2


# In[27]:


z = x**2


# ** Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook. What command do you use if you aren't using the jupyter notebook?**

# In[29]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# **Create a figure object called fig using plt.figure()**<br>
# **Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax.**<br>
# **Plot (x,y) on that axes and set the labels and titles to match the plot below:**<br>

# In[35]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Title')


# **Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively**

# In[36]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2, 0.5, .2, .2])


# **Now plot (x,y) on both axes. And call your figure object to show it.**

# In[37]:


ax1.plot(x,y)
ax2.plot(x,y)


# In[38]:


fig


# **Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**

# In[52]:


fig = plt.figure()
ax3= fig.add_axes([0,0,1,1])
ax4= fig.add_axes([0.2,0.5,.4,.4])

#large
ax3.plot(x,z)
ax3.set_xlabel('x')
ax3.set_ylabel('Y')

#Insert
ax2.plot(x,y)
ax2.set_title('zoom')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])


# **Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**

# In[53]:


fig = plt.figure()
ax3= fig.add_axes([0,0,1,1])
ax4= fig.add_axes([0.2,0.5,.4,.4])

#large
ax3.plot(x,z)
ax3.set_xlabel('x')
ax3.set_ylabel('Y')

#Insert
ax2.plot(x,y)
ax2.set_title('zoom')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])


# **Use plt.subplots(nrows=1, ncols=2) to create the plot below.**

# In[54]:


fig,axes = plt.subplots(1,2)


# **Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style**

# In[56]:


fig,axes = plt.subplots(1,2)
axes[0].plot(x,y, color='blue', ls='--')
axes[1].plot(x,z, color = 'red', lw=3)


# **See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code**

# In[57]:


fig,axes = plt.subplots(1,2, figsize = (12,2))    #figsize to be put in figure
axes[0].plot(x,y, color = 'blue', lw = 3)
axes[1].plot(x,z, color = 'red', ls = '--')


# **Python for Data Visualization - Seaborn**

# In[1]:


#Notes
# its built on top of matplotlib
# conda install seaborn   or     pip install seaborn


# **Distribution Plots**

# In[2]:


#Notes
# %matplotlib inline           # helps to see data visualization in notebook


# In[7]:


import seaborn as sns


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


tips = sns.load_dataset('tips')   # calling random dataset 'tips' as dataframe from seaborn 


# In[7]:


tips.head()


# **DIST Plot**

# In[8]:


# DIST plot is a distribution of a univariate set of observations., gives a historgram

# syntax->       sns.distplot(df['columnname'], kde = true or false, bins = number)
# for distplot we pass only one column
# Kde = False removes the line on histogram
# bins = number   gives more defenition and detail of histogram


# In[12]:


sns.distplot(tips['total_bill'], kde = False, bins = 30)    # for distplot we pass only one column    here we get histogram,
                                                 # Kde = False    removes the line on histogram
                                                # bins = number   gives more defenition and detail of histogram


# **Joint Plot**

# In[13]:


#Notes
# helps matchup two distplots for bivariate data, bivariate is two variables 

#syntax->   sns.jointplot(x variable = 'columnname', y varaiable = 'columnname',  dataset = dataframe, kind = 'name of the plot type')


# In[19]:


sns.jointplot(x='total_bill',y='tip',data=tips, kind='hex')   
#syntax-> sns.jointplot(x variable = 'columnname', y varaiable = 'columnname',  dataset = dataframe, kind = 'name of the plot type')


# In[21]:


sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')   # here reg is regression type plot


# In[23]:


# other type of kind of plot is KDE
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')


# **Pair PLot**

# In[27]:


#Notes
# plots pairwise relationships accross an entire dataframe at least for the numerical values
# pairplot does jointplots on all the numerical columns of the dataframe

# syntax-> sns.pairplot(dataframe, hue = 'categorical column', palette = 'coolwarm') 


# In[30]:


sns.pairplot(tips, hue='sex', palette = 'coolwarm')   #hue will color the categories present in the data, palette will also give color


# **Rug Plot**

# In[31]:


# Notes
# gives dashes in the plot related to a single column 

# syntax-> sns.rugplot(dataframe['columnname'])


# In[32]:


sns.rugplot(tips['total_bill'])


# **KDE PLot**

# In[33]:


#Notes
# KDE stands for Kernel Density Estimation
# it is a line on plot
# kdeplots are Kernel Density Estimation plots. 
# These KDE plots replace every single observation with a Gaussian (Normal) distribution centered around that value


# In[3]:


# Don't worry about understanding this code!
# It's just for the diagram below
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Creating dataset 
dataset = np.random.randn(25)


# In[35]:


dataset


# In[41]:


# creating rugplot
sns.rugplot(dataset)

#set up x axis 
x_min = dataset.min() -2
x_max = dataset.max() +2

# hundred equally space points from xmin to xmax
x_axis = np.linspace(x_min, x_max, 100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'
bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2

# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)


# In[43]:


# To get the kde plot we can sum these basis functions.

# Plot the sum of the basis function
sum_of_kde = np.sum(kernel_list, axis = 0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")


# In[44]:


sns.kdeplot(tips['total_bill'])


# **Categorical Plots**

# - factorplot<br>
# - boxplot<br>
# - violinplot<br>
# - stripplot<br>
# - swarmplot<br>
# - barplot<br>
# - countplot<br>

# In[ ]:


#Notes
# for Categorical plots we will mainly focus on categorical columns


# In[45]:


tips = sns.load_dataset('tips')      # sns.load_dataset('dataset_name') dataset are already present in seaborn lib
tips.head()


# **Bar Plot**

# These are very similar plots allow you to get **aggregate data off a categorical feature in your data.** barplot is a general plot that **allows you to aggregate the categorical data based off some function, by default that's the mean**

# In[ ]:


#notes
# this is a visualization of a groupby action

#syntax-> sns.barplot(x = 'categorical_column', y = 'numerical column', data = dataframe, estimator = np.statisticalfunction)


# In[6]:


import numpy as np


# In[48]:


sns.barplot(x= 'sex', y= 'total_bill', data= tips, estimator = np.std)  
# this will show average/mean of the total bill per categoical column value
# estimator is a statistical aggregae function and default it is mean/ average


# **Count Plot**

# This is essentially the same as barplot except the estimator is explicitly counting the number of occurrences. Which is why we only pass the x value

# In[49]:


#Notes

#syntax->  sns.countplot(x = 'categorical_column', data = dataframe)


# In[50]:


sns.countplot(x = 'sex', data = tips)     #same as pandas.count for gender


# **Box Plot and Violin Plot**

# Boxplots and Violinplots are used to **shown the distribution of categorical data.**<br> A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. <br>The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be “outliers” using a method that is a function of the inter-quartile range.

# In[51]:


#Notes
# Box Whisker plot
# points that are outside the T graph plot are outliers

#syntax-> sns.boxpot(x = 'categoricalcolumn, y = 'numerical_column' , data = dataframe, hue = 'categoricalcolumn')


# In[55]:


sns.boxplot(x = 'day', y = 'total_bill', data = tips, hue = 'smoker')  # points that are outside the T graph plot are outliers


# **Violin Plot**

# A violin plot plays a similar role as a box and whisker plot.<br> It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared. Unlike a box plot, in which all of the plot components correspond to actual datapoints, <br>the violin plot features a kernel density estimation of the underlying distribution.

# In[56]:


#Notes
# shows distribution of  data accross some category
# shows distribution of points on the sides

#syntax-> sns.violinplot(x= 'categoricalcolumn', y= 'numericalcolumn', data = dataframe, hue = 'categoricalcolum', split = true or false, palette = 'rainbow')


# In[57]:


sns.violinplot(x= 'day', y = 'total_bill', data =  tips)


# In[58]:


sns.violinplot(x= 'day', y = 'total_bill', data =  tips, hue = 'sex', split = True)  # here split, splits the plot in 2 halfs


# **Strip Plot**

# Strip Plot will draw a scatter plot where one variable is categorical.<br>
# Jitter argument will random noise to seperate stack points, you can see density a bit better
# hue argument will take categorical variable<br>
# Split argument will split the colors<br>
# <br>
# **Syntax->**<br> 
# **sns.stripplot(x = 'categoricalvariablecolm', y = 'Numericalveriablecolm', data = dataframe, hue = ''categoricalcolm, split = True, jitter = True )**

# In[6]:


sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', split=True)


# **Swarm Plot**

# Combination of strip plot and violin plot<br>
# Similar to strip plot<br>
# Points dont overlap here<br>
# They cannot scale very large numbers<br>
# <br>
# **Syntax->**<br>
# **sns.swarmplot(x='categoricalcolm', y='numericalcolm', data = dataframe)**

# In[7]:


sns.swarmplot(x='day', y='total_bill', data= tips)


# In[8]:


# Combining voilinplot and swarmplot together
sns.violinplot(x='day', y='total_bill', data= tips)
sns.swarmplot(x='day', y='total_bill', data= tips)


# **Factor Plot**

# Taken x and y argument , also hue and kind argument<br>
# <br>
# **Syntax->**
# **sns.factorplot(x='categoticalcolm', y='total', data=dataframe, kind='type of plot')**

# In[9]:


sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')


# **Matrix Plot**

# Matrix plots allow you to plot data as color-encoded matrices and can also be used to indicate clusters within the data

# In[10]:


tips = sns.load_dataset('tips')


# In[11]:


flights = sns.load_dataset('flights')


# In[14]:


tips.head()


# In[15]:


flights.head()


# **Heatmap**

# Shows matrix plots<br>
# Data should be in matrix form for heatmap. Variables should be in columns and in rows. We do that by dataframe.corr()<br>
# <br>
# **Syntax->**
# **sns.heatmap(correlated dataframe, annot = True, cmap ='color')  annotations shows values on grids**

# In[21]:


tips.corr()


# In[22]:


tc= tips.corr()


# In[24]:


sns.heatmap(tc, annot= True, cmap = 'coolwarm')


# In[29]:


# Now in flights table we want Column 'month' also to be as the Index for that we use .pivot_table
# syntax->    dataframe.pivot_table(index = 'Columnname', coloumns = 'columnname', values = 'columnname')

flights


# In[30]:


flights.pivot_table(index='month', columns = 'year', values = 'passengers') 
# syntax->    dataframe.pivot_table(index = 'Columnname', coloumns = 'columnname', values = 'columnname')
# this data is in matrix form now


# In[31]:


fp = flights.pivot_table(index='month', columns='year', values='passengers')


# In[34]:


sns.heatmap(fp, cmap='magma', linecolor ='white', linewidth = 2  )  # here we can see in around june to august more number of passenger took flight


# **Clustermap**

# The clustermap uses hierarchal clustering to produce a clustered version of the heatmap<br>
# <br>
# Syntax-><br>
# sns.clustermap(corelated dataframe)<br>

# In[36]:


sns.clustermap(fp, cmap='coolwarm')  # here its clusteres columns and rows that are similar to each other


# In[37]:


sns.clustermap(fp, cmap='coolwarm' ,standard_scale =1)  
# here its clusteres columns and rows that are similar to each other
# standar scale takes from 0 to 1, (i do not recommend this)


# **Grids**

# Grids are general types of plots that allow you to map plot types to rows and columns of a grid, this helps you create similar plots separated by features.
# <br>Used to automate subplots based of features of a data

# In[40]:


iris = sns.load_dataset('iris')


# In[41]:


iris.head()


# In[44]:


iris['species'].unique()


# In[45]:


sns.pairplot(iris)


# **Pair Grid**

# Pairgrid is a subplot grid for plotting pairwise relationships in a dataset
# <br>Takes all numerical columns and grids them up
# <br>You can also map different plots to the grid by: **sotringgridinvariable** and then **storedgridvarible.map(plt.plot_type)<br>
# **Syntax->**<br>
# **sns.PairGrid(dataframe)**

# In[46]:


sns.PairGrid(iris)


# In[51]:


# store PairGrid in a varible
g = sns.PairGrid(iris)
g.map(plt.scatter)   # mapping grid with a scatter plot


# In[53]:


g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# **Facet Grid**

# Creates grids of plots based off of features<br>
# <br>
# **Syntax->**<br>
# **sns.FacetGrid(data= dataframe, col=columname, row= columnname)**

# In[54]:


tips.head()


# In[55]:


sns.FacetGrid(data = tips, col = 'time' , row = 'smoker')


# In[57]:


#storing this in a varible g
g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(sns.distplot,'total_bill')  # mapping g with distplot on total_bill column 
# mapping with plot types generally need more than one argument except distplot


# In[58]:


g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(plt.scatter,'total_bill', 'tip')   # mapping with scatter plot on 2 arguments


# **Regression Plots**

# Seaborn has many built-in capabilities for regression plots<br>
# we will only cover the lmplot() function for now.<br>
# <br>
# **lm plot** allows you to display linear models<br> 
# Also allows you to split up those plots based off of features, as well as coloring the hue based off of features.

# **lm Plot**

# Linear model plot<br>
# <br>
# **Syntax->**<br>
# **sns.lmplot(x = 'feature1', y= 'feature2', data = dataframe, hue = 'categoricalfeaturecolumn')**

# In[59]:


tips.head()


# In[63]:


sns.lmplot(x='total_bill', y='tip', data=tips, hue = 'sex', markers = ['o','v'], scatter_kws= {'s':100})
# here scatter_kws resizes the points in the plot
# scatter_kws passes dictionary key and value as size
# scatter_kws = {'s':100} here 100 is size and s is key


# In[71]:


sns.lmplot(x='total_bill', y='tip', data= tips, col='day', hue='sex', aspect=0.6, size = 8)
# here col argument gives 2 seperate plots related to a same feature 
# size argument for size of plot 


# **Style and Color**

# - change background<br>
# sns.set_style('whitegrid')<br>
# <br>
# - remove lines on the sides, bottom<br>
# sns.despine(left = True, bottom = True)

# In[72]:


tips.head()


# In[79]:


sns.set_style('whitegrid')
sns.countplot(x = 'sex', data = tips)
sns.despine(left = True, bottom = True)


# **Size and Aspect**

# You can use matplotlib's **plt.figure(figsize=(width,height)** to change the size of most seaborn plots.<br>
# <br>
# You can control the size and aspect ratio of most seaborn grid plots by passing in parameters: **size, and aspect.**

# In[1]:


#Notes
# syntax->      plt.figure(figsize = (12,3)) this is to change the figure


# In[11]:


plt.figure(figsize = (12,3))    # this is to change the size of the figure
sns.countplot(x='sex', data=tips)


# **Scale and Context**

# In[12]:


#Notes
# Allows to overwrite default parameters
# syntax->      sns.set_context('', font_scale = number)


# In[39]:


sns.set_context('notebook',font_scale = 1)
sns.countplot(x='sex', data=tips)


# In[40]:


sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')


# **Python for Data Visualization - Pandas Built-in Data Visualization**

# In[43]:


import numpy as np
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[44]:


df1 = pd.read_csv('E:/Udemy- Python for Data Science and Machine Learning/Py-DS-ML-Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df1.csv', index_col = 0)


# In[45]:


df1.head()  # here index is in timeseries format


# In[46]:


df2 = pd.read_csv('E:/Udemy- Python for Data Science and Machine Learning/Py-DS-ML-Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df2.csv')


# In[47]:


df2.head()


# In[ ]:


#Notes
# histogram of df1
# syntax-1>  
# dataframe['columnname'].hist(matplotlib arguments)  
# here inside .hist() you can pass in matplotlib arguments such as bins

# syntax 2->
# dataframe['columnname'].plot(kind = 'type of plot', matplotlibargument)

# syntax3->
# dataframe['columnname'].plot.hist()

# syntax4->
# dataframe.plot.area(arguments)

# syntax5->
# dataframe.plot.bar()

# syntax6->
# dataframe.plot.line(x = dataframe.index, y = 'columnmame')

# syntax7->
# dataframe.plot.scatter(x = 'columnname', y=' columnname', c = 'columnaname', s='df1.['columnname']*100) here c is color, s is size

# syntax8->
# dataframe.plot.box()

# syntax9->
# dataframe.plot.hexbin(x='columname', y='columnname', gridsize= number)   here gridsize makes the plot larger 

# syntax10->
# dataframe.plot.density()

# syntax11->
# dataframe['columname'].plot.kde()


# **Plot Types**

# There are several plot types built-in to pandas, most of them statistical plots by nature:<br>
# <br>
# - df.plot.area<br>
# - df.plot.barh<br>
# - df.plot.density<br>
# - df.plot.hist<br>
# - df.plot.line<br>
# - df.plot.scatter<br>
# - df.plot.bar<br>
# - df.plot.box<br>
# - df.plot.hexbin<br>
# - df.plot.kde<br>
# - df.plot.pie<br>
# You can also just call df.plot(kind='hist') or replace that kind argument with any of the key terms shown in the list above (e.g. 'box','barh', etc..)<br>

# In[49]:


df1['A'].hist(bins=30)


# In[51]:


df1['A'].plot(kind = 'hist', bins = 30)


# In[52]:


df1['A'].plot.hist()


# In[53]:


df2.head()


# **Area PLot**

# In[55]:


df2.plot.area(alpha=0.4)


# **Bar Plot**

# In[57]:


df2.plot.bar(stacked = True)


# In[58]:


df1['A'].plot.hist(bins=50)


# In[63]:


df1.head()


# **Line Plot**

# In[69]:


df1.plot.line(y='B', figsize = (12,3), lw=1)


# **Scatter Plot**

# In[73]:


df1.plot.scatter(x='A',  y='B', c='C', cmap ='coolwarm', s = df1['C']*100)


# **Box Plot**

# In[74]:


df2.plot.box()


# **Hexagonal Bin Plot**

# Useful for Bivariate Data, alternative to scatterplot

# In[75]:


df = pd.DataFrame(np.random.randn(100,2), columns=['a','b'])


# In[76]:


df.head()


# In[79]:


df.plot.hexbin(x='a', y='b', gridsize=25, cmap='coolwarm')


# **Kernel Density Estimation (KDE) Plot**

# In[80]:


df2['a'].plot.kde()


# In[83]:


df2.plot.density()


# **Plotly and Cufflinks**

# - Plotly is a visualization library<br>
# - Cufflinks connects plotly with pandas<br>
# <br>
# pip install plotly<br>
# pip install cufflinks<br>

# In[ ]:


pip install plotly


# In[ ]:


pip install cufflinks


# In[14]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


from plotly import __version__


# In[16]:


print(__version__)


# In[17]:


import cufflinks as cf


# In[19]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[20]:


init_notebook_mode(connected = True)   # For Notebooks


# In[21]:


cf.go_offline()   # For offline use


# **Fake Data**

# In[29]:


df = pd.DataFrame(np.random.randn(100,4), columns = 'A B C D'.split())   # .split gives a list of columns A B C D


# In[31]:


df.head()


# In[32]:


df2 = pd.DataFrame({'Category': ['A','B','C'], 'Values': [32,43,50]})


# In[33]:


df2


# **Using Cufflinks and iplot()**<br>
# <br>
# - scatter<br>
# - bar<br>
# - box<br>
# - spread<br>
# - ratio<br>
# - heatmap<br>
# - surface<br>
# - histogram<br>
# - bubble<br>

# In[35]:


df.iplot()


# **Scatter Plot**

# In[38]:


df.iplot(kind = 'scatter', x = 'A', y = 'B', mode = 'markers', size = 15)
# syntax->
# dataframe.iplot(kind = scatter, x = column1, y = column2, mode = 'markers')


# **Bar Plot**

# In[39]:


df2.iplot(kind = 'bar', x = 'Category', y = 'Values') 
# syntax->
# dataframe.iplot(kind = 'bar', x ='column1', y='column2')


# In[40]:


df.count().iplot(kind= 'bar')


# In[41]:


df.sum().iplot(kind = 'bar')


# **Box Plot**

# In[43]:


df.iplot(kind = 'box')


# **3D Surface Plot**

# In[47]:


df3 = pd.DataFrame({'x':[1,2,3,4,5],  'y':[10,20,30,20,10], 'z':[5,4,3,2,1]})


# In[48]:


df3


# In[51]:


df3.iplot(kind = 'surface', colorscale = 'rdylbu')
# syntax->
# dataframe.iplot(kind = 'surface', colorscale = 'rdylbu')


# **Historgram**

# In[54]:


df['A'].iplot(kind='hist', bins = 40)
# syntax->
# dataframe['columnname'].iplot(kind = 'hist')


# In[55]:


df.iplot(kind = 'hist')


# **Spread**

# Used to compare stocks and stocks data

# In[56]:


df[['A','B']].iplot(kind = 'spread')
# syntax->
# dataframe[['column1', 'column2'].iplot(kind = 'spread')]


# **Bubble Plot**
# 

# In[57]:


# similar to scatter plot


# In[59]:


df.iplot(kind = 'bubble', x = 'A', y = 'B', size = 'C')
# syntax
# dataframe.iplot(kind = 'bubble', x='column1', y='column2', size = 'column3')


# **Scatter Matrix**

# Similar to sns.pairplot()   seaborn pairplot

# In[60]:


df.scatter_matrix()
# syntax->
# dataframe.scatter_matrix()


# **Python for Data Visualization - Geographical Plotting**

# Plotly for plotting and also Matplotlib for plots

# **Choropleth Maps - USA**

# **Offline Plotly Usage**

# Get imports and set everything up to be working offline.

# In[63]:


pip install chart-studio


# In[38]:


import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# Now set up everything so that the figures show up in the notebook:

# In[39]:


init_notebook_mode(connected=True)


# **Choropleth US Maps**

# In[40]:


import pandas as pd


# Now we need to begin to build our data dictionary. Easiest way to do this is to use the dict() function of the general form:<br>
# <br>
# type = 'choropleth',<br>
# locations = list of states<br>
# locationmode = 'USA-states'<br>
# colorscale=<br>
# Either a predefined string:<br>
# <br>
# 'pairs' | 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' | 'Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'<br>
# or create a custom colorscale<br>
# <br>
# text= list or array of text to display per point<br>
# z= array of values on z axis (color of state)<br>
# colorbar = {'title':'Colorbar Title'})<br>
# Here is a simple example:<br>

# In[41]:


data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['text1','text2','text3'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title'})


# Then we create the layout nested dictionary:

# In[42]:


layout = dict(geo = {'scope':'usa'})


# Then we use:<br>
# <br>
# go.Figure(data = [data],layout = layout)<br>
# to set up the object that finally gets passed into iplot()<br>

# In[43]:


choromap = go.Figure(data = [data],layout = layout)


# In[45]:


iplot(choromap)


# **Real Data US Map Choropleth**

# In[46]:


# Try putting r (raw format).

# r'D:\python_projects\templates\0.html'
df = pd.read_csv(r'E:/Udemy- Python for Data Science and Machine Learning/Py-DS-ML-Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master\09-Geographical-Plotting.csv/2011_US_AGRI_Exports.csv')
df.head()


# Now out data dictionary with some extra marker and colorbar arguments:

# In[52]:


data = dict(type='choropleth',
            colorscale = 'RdBu',
            locations = df['code'],
            z = df['total exports'],
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = {'title':"Millions USD"}
            ) 


# And our layout dictionary with some more arguments:

# In[53]:


layout = dict(title = '2011 US Agriculture Exports by State',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )


# In[54]:


choromap2 = go.Figure(data=[data],layout=layout)


# In[55]:


iplot(choromap2)


# **World Choropleth Map**

# In[56]:


df = pd.read_csv('E:/Udemy- Python for Data Science and Machine Learning/Py-DS-ML-Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/09-Geographical-Plotting.csv/2014_World_GDP.csv')
df.head()


# In[61]:


data = dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorbar = {'title' : 'GDP Billions USD'},
      ) 


# In[63]:


layout = dict(
    title = '2014 Global GDP',
    geo = dict(
        showframe = False,
        projection = {'type':'mercator'}
    )
)


# In[64]:


choromap3 = go.Figure(data = [data],layout = layout)


# In[66]:


iplot(choromap3)


# **Python Crash Course Exercise**

# **What is 7 to the power of 4?**

# In[67]:


7**4


# **Split this string:**<br>
# <br>
# s = "Hi there Sam!"<br>
# into a list. <br>

# In[69]:


s = 'Hi there Sam!'


# In[70]:


s.split()


# **Given the variables:**<br>
# <br>
# planet = "Earth"<br>
# diameter = 12742<br>
# Use .format() to print the following string:<br>
# <br>
# The diameter of Earth is 12742 kilometers.<br>

# In[71]:


planet = 'Earth'
diameter = '12742'


# In[72]:


print('The diameter of {} is {} kilometers'. format(planet, diameter))


# **Given this nested list, use indexing to grab the word "hello"**

# In[73]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[81]:


lst[3][1][2][0]


# **Given this nest dictionary grab the word "hello"**

# In[82]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[93]:


d['k1'][3]['tricky'][3]['target'][3]


# **What is the main difference between a tuple and a list?**

# In[94]:


# Tuple is immutable and list is mutable


# **Create a function that grabs the email website domain from a string in the form:**<br>
# <br>
# user@domain.com<br>
# So for example, passing "user@domain.com" would return: domain.com<br>

# In[95]:


def domainGet(email):
    return email.split('@')[1]


# In[96]:


domainGet('danish@gmail.com')


# **Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.**

# In[97]:


def findDog(statement):
    return 'dog' in statement


# In[98]:


findDog('Where is the dog')


# **Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.**

# In[101]:


def countDog(statement):
    count = 0
    for word in statement.split():
        if word == 'dog':
            count += 1
    return count


# In[102]:


countDog('my dog is better than your dog')


# **Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
# seq = ['soup','dog','salad','cat','great']
# should be filtered down to:
# 
# ['soup','salad']

# In[103]:


seq = ['soup','dog','salad','cat','great']


# In[105]:


list(filter(lambda word: word[0]=='s', seq))


# **You are driving a little too fast, and a police officer stops you.
# Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
# If your speed is 60 or less, the result is "No Ticket". 
# If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
# If speed is 81 or more, the result is "Big Ticket". 
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.**

# In[106]:


def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[107]:


caught_speeding(81,True)


# In[108]:


caught_speeding(81,False)


# **NumPy Excercises**

# **Import NumPy as np**

# In[111]:


import numpy as np


# **Create an array of 10 zeros**

# In[112]:


np.zeros(10)


# **Create an array of 10 ones**

# In[113]:


np.ones(10)


# **Create an array of 10 fives**

# In[114]:


np.ones(10) * 5


# **Create an array of the integers from 10 to 50**

# In[115]:


np.arange(10,50)


# **Create an array of all the even integers from 10 to 50**

# In[116]:


np.arange(10,51,2)


# **Create a 3x3 matrix with values ranging from 0 to 8**

# In[117]:


np.arange(9).reshape(3,3)


# **Create a 3x3 identity matrix**

# In[119]:


np.eye(3)


# **Use NumPy to generate a random number between 0 and 1**

# In[120]:


np.random.rand(1)


# **Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution**

# In[121]:


np.random.randn(25)


# **Create the following matrix:**

# In[122]:


np.arange(1,101).reshape(10,10) / 100


# **Create an array of 20 linearly spaced points between 0 and 1:**

# In[123]:


np.linspace(0,1,20)


# **Numpy Indexing and Selection**

# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[124]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[125]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[126]:


mat[2:,1:]


# In[127]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[128]:


mat[3,4]


# In[129]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[130]:


mat[:3,1:2]


# In[131]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[132]:


mat[4,:]


# In[133]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[134]:


mat[3:5,:]


# **Now do the following**<br>
# **Get the sum of all the values in mat**

# In[135]:


mat.sum()


# **Get the standard deviation of the values in mat**

# In[136]:


mat.std()


# **Get the sum of all the columns in mat**

# In[137]:


mat.sum(axis=0)


# **Seaborn Exercises**

# In[138]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[139]:


sns.set_style('whitegrid')


# In[140]:


titanic = sns.load_dataset('titanic')


# In[141]:


titanic.head()


# **Exercises**<br>
# **Recreate the plots below using the titanic dataframe. There are very few hints since most of the plots can be done with just one or two lines of code and a hint would basically give away the solution. Keep careful attention to the x and y labels for hints.**

# In[142]:


sns.jointplot(x='fare',y='age',data=titanic)


# In[143]:


sns.distplot(titanic['fare'],bins=30,kde=False,color='red')


# In[144]:


sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')


# In[145]:


sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')


# In[146]:


sns.countplot(x='sex',data=titanic)


# In[147]:


sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr()')


# In[148]:


g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')


# **Pandas Data Visualization Exercise**

# In[149]:


df3 = pd.read_csv(r'E:\Udemy- Python for Data Science and Machine Learning\Py-DS-ML-Bootcamp-master\Refactored_Py_DS_ML_Bootcamp-master\07-Pandas-Built-in-Data-Viz\df3.csv')


# In[150]:


df3.head()


# In[151]:


df3.info()


# **Recreate this scatter plot of b vs a. Note the color and size of the points. Also note the figure size. See if you can figure out how to stretch it in a similar fashion. Remeber back to your matplotlib lecture...**

# In[152]:


df3.plot.scatter(x='a',y='b',c='red',s=50,figsize=(12,3))


# **Create a histogram of the 'a' column.**

# In[153]:


df3['a'].plot.hist()


# **These plots are okay, but they don't look very polished. Use style sheets to set the style to 'ggplot' and redo the histogram from above. Also figure out how to add more bins to it.**

# In[154]:


plt.style.use('ggplot')


# In[155]:


df3['a'].plot.hist(alpha=0.5,bins=25)


# **Create a boxplot comparing the a and b columns.**

# In[156]:


df3[['a','b']].plot.box()


# **Create a kde plot of the 'd' column**

# In[157]:


df3['d'].plot.kde()


# **Figure out how to increase the linewidth and make the linestyle dashed. (Note: You would usually not dash a kde plot line)**

# In[158]:


df3['d'].plot.density(lw=5,ls='--')


# **Choropleth Exercises** 

# **Plotly Imports**

# In[161]:


import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot,plot
init_notebook_mode(connected=True)


# **Import pandas and read the csv file: 2014_World_Power_Consumption**

# In[162]:


import pandas as pd


# In[164]:


df = pd.read_csv(r'E:\Udemy- Python for Data Science and Machine Learning\Py-DS-ML-Bootcamp-master\Refactored_Py_DS_ML_Bootcamp-master\09-Geographical-Plotting.csv\2014_World_Power_Consumption.csv')


# **Check the head of the DataFrame.**

# In[165]:


df.head()


# **Create a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary**

# In[168]:


data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        reversescale = True,
        locations = df['Country'],
        locationmode = "country names",
        z = df['Power Consumption KWH'],
        text = df['Country'],
        colorbar = {'title' : 'Power Consumption KWH'},
      ) 

layout = dict(title = '2014 Power Consumption KWH',
                geo = dict(showframe = False,projection = {'type':'mercator'})
             )


# In[169]:


choromap = go.Figure(data = [data],layout = layout)
plot(choromap,validate=False)


# **Import the 2012_Election_Data csv file using pandas.**

# In[170]:


usdf = pd.read_csv(r"E:\Udemy- Python for Data Science and Machine Learning\Py-DS-ML-Bootcamp-master\Refactored_Py_DS_ML_Bootcamp-master\09-Geographical-Plotting.csv\2012_Election_Data.csv")


# In[171]:


usdf.head()


# **Create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type. VAP has already been transformed to a float for you.**

# In[172]:


data = dict(type='choropleth',
            colorscale = 'Viridis',
            reversescale = True,
            locations = usdf['State Abv'],
            z = usdf['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text = usdf['State'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':"Voting-Age Population (VAP)"}
            ) 


# In[173]:


layout = dict(title = '2012 General Election Voting Data',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )


# In[174]:


choromap = go.Figure(data = [data],layout = layout)
plot(choromap,validate=False)


# In[ ]:




