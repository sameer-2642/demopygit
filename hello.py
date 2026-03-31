# print("hello world  from python")
# a=2
# b=4
# print(a+b)
# from scipy._lib.decorator import __init__


# name = """sameer"""
# print(name)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[-1])
# print(name[0:3])
# print(name[:3])
# length = len(name)
# print(length)

# list are mutable

# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums)

# for num in nums:
#  if num%2==0:
#     print(num)


# print(nums[3:])

# valeues = [1,"sameer",3.14,True]
# print(valeues)

# listofLists = [nums,valeues]
# print(listofLists)

# nums.append(11)
# print(nums)

# nums.insert(2,88)
# print(nums)

# nums.pop(2)
# print(nums)

# del nums[2:]
# print(nums)

# sum=0
# for num in nums:
#     sum = sum+num
# print(sum)

# nums2 = [1,4,5,9,0]

# length = len(nums2)

# for i in range(length):
#     for j in range(i+1,length):
#         if nums2[i]>nums2[j]:
#             nums2[i],nums2[j] = nums2[j],nums2[i]
# print(nums2)

# tuple and set are immutable

# tup = (1,2,3,4,5)
# print(tup)

# tup.index(3)
# print(tup.index(3)) 

# s = {1,3,8,0,7,3,1}
# print(s)

# s.update({9,10,11})
# print(s)


# Dictonary

# data = {
#     "name" : "sameer",
#     "age" : 25,
#     "city" : "kalaburagi"
# }


# print(data.get("name"))

# combine two lists into a dictionary

# names = ["sameer","pavan","sachin","aman"]
# ages = [25,85,69,80]

# dictonary = dict(zip(names,ages))
# print(dictonary)

# # adding new key value pair to the dictonary
# dictonary["prajwal"] = 92
# print(dictonary)

# # deleting a key value pair from the dictonary
# del dictonary["sameer"]
# print(dictonary)

# putting a dictonary inside a list as a value and accessing it
# programming_languages = {"js":"vs code","python":"sublime","java":{'jse':'eclipse' , 'javaee':'intellij'},"c++":"clion"}
# print(programming_languages)

# print(programming_languages["js"])
# print(programming_languages["python"])
# # print with indexing of the value which is a list
# print(programming_languages["python"][1])
# print(programming_languages["java"]["javaee"])


# id is a built in function in python used to know the memory address of a variable
# num = 5
# print(id(num))

# a=10
# print(id(a))
# b=a
# print(id(b))


# pi = 3.14
# print(type(pi))

# complex numbers in python
# c = 2 + 3j
# print(c)
# print(type(c))

# a = 10.6
# b = int(a)
# print(type(b))

# k = float(b)
# print(type(k))
# print(k)

# x = complex(k,b)
# print(x)

# bool = b<k
# print(bool)

# print(type(bool))

# print(int(True))
# print(int(False))

# repeatation not allowed in set
# s = {1,"sameer",3.14,True}
# print(s)

# t = (1,"sameer",3.14,True,1,"sameer",3.14,True)
# print(t)

# range is a built in function in python used to generate a sequence of numbers
# print(range(10))

# print(list(range(10)))

# dic = {
#     "name" : "sameer",
#     "age" : 25,
#     "city" : "kalaburagi"
# }

# keys = dic.keys()
# print(keys)

# value = dic.values()
# print(value)

# fetchValue = dic["age"]
# print(fetchValue)

# nameValue = dic.get("name")
# print(nameValue)

# a,b = 1,3
# print(a)

# a=5
# b=6

# print(a<8 and b>5)

# binary representation of a number
# print(bin(10))

# octal representation of a number
# print(oct(10))

# # hexadecimal representation of a number
# print(hex(10))

# bitwise operators in python
# print(~12)

# import math as m
# from math import sqrt,pow


# print(sqrt(16))
# print(pow(2,3))

# print(help(m))


# swap two  numbers

# a=6
# b=5

# temp = a
# a = b
# b = temp

# print(a)
# print(b)

# swapping without using a third variable

# a=6
# b=5

# a = a+b  11
# b = a-b  6
# a = a-b  5

# # print(a)
# # print(b)

# a,b = b,a

# print(a)
# print(b)

# x=int(input("enter the first number "))
# y=int(input("enter the second number "))
# print("the sum of two numbers is ",x+y)

# ch = input("enter a character ")[0]
# print(ch)

# to get command line arguments in python we can use sys module
# import sys

# x = int(sys.argv[1])
# y = int(sys.argv[2])
# z = x+y
# print("the sum of two numbers is ",z)

# if True:
#     print("hello world")

# if False:
#     print("hello world")

# x = 10
# if x%2==0:
#     print("x is even")
#     if x>5:
#         print("x is greater than 5")
        
# else:
#     print("x is odd")

# x=10

# if(x==1):
#     print("one")

# elif(x==2):
#     print("two")

# elif(x==3):
#     print("three")
# else:
#     print("x is greater than 3")

# loops

# i=1

# while i<=5:
#     print("sameer",end=" ")
#     j=1
#     while j<=4:
#         print("pavan",end=" ")
#         j=j+1
#     i=i+1
#     print()

# x = ["sameer",2,3.14]
# for i in x:
#     print(i)

# x = "sameer"
# for i in x:
#     print(i)

# for i in [2,4,"sameer"]:
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(20,10,-1):
#     if i%5!=0:
#      print(i)

# x = int(input("how many candys do you want? "))

# for i in range(x):
#     print("candy")

# avc = 10

# x = int(input("how many candys do you want?"))

# i=1

# while i<=x:
#     if i>avc:
#         print("sorry we are out of stock")
#         break
#     print("candy")
#     i=i+1

# print("candys are over")

# x = int(input("enter a number "))

# for i in range(1, x):
#     if i % 2!=0:
#         pass
#     print(i)
    
#     else:
#         print("even number")

# for i in range(5):
#     if i==3:
#         continue
#     print(i)

# x = int(input("enter a number "))

# for i in range(x):
#     for j in range(x-i):
#         print("*",end=" ")
#     print()

# nums = list(map(int, input("Enter numbers separated by space: ").split()))

# for num in nums:
#     if num % 2 == 0:
#         print(num, end=" ")
        
# else:
#     print("odd", end=" ")

# x = int(input("enter a number "))

# prime number is a number which is divisible by only 1 and itself
# if x>1:
#     for i in range (2,x):
#         if x%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")

# Array

# import array as arr
# from array import *

# a = arr.array('i',[1,2,3,4,5,6])
# print(a)

# a = arr.array('I',[1,2,3,4,5,6]) # unsigned integer array 'I' means cannot store negative numbers
# print(a.buffer_info()) # returns a tuple containing the memory address of the first element and the number of elements in the array

# rev = a[::-1] # reverse the array
# print(rev)

# a = arr.array('i',[1,2,3,4,5,6])
# for i in range(6):
#     print(a[i],end=" ")

# a = arr.array('i',[1,2,3,4,5,6])
# for i in range(len(a)):
#     print(a[i],end=" ")

# a = arr.array('u',['s','a','m','e','e','r'])
# for i in range(len(a)):
#     print(a[i],end=" ")

# a = arr.array('i',[1,2,3,4,5,6])
# newArr = array(a.typecode,(e*e for e in a))

# # for i in range(len(newArr)):
# #     print(newArr[i],end=" ")

# i=0

# while i<len(newArr):
#     print(newArr[i],end=" ")
#     i=i+1

# taking the values from user in array

# from array import *

# size = int(input("enter the size of the array "))
# arr = array('i',[])

# for i in range(size):
#     x = int (input("enter the element "))
#     arr.append(x)

# print(arr)

# val = int(input("enter the value to search "))
# for i in range(len(arr)):
#     if arr[i]==val:
#         print("value found at index ",i)
#         break
# else:
#     print("value not found in the array")

# size = int(input("enter the size of the array "))
# arr = array('i',[])

# for i in range(size):
#     x = int (input("enter your element "))
#     arr.append(x)
# print(arr)

# val = int(input("enter the value to search "))
# for i in range(len(arr)):
#     if arr[i]==val:
#         print("value found at index ",i)
#         break
# else:
#     print("value not found in the array")

# # deleting an element from the array
# val = int(input("enter the value to delete "))
# for i in range(len(arr)):
#     if arr[i]==val:
#         arr.pop(i)
#         print("value deleted")
#         break
# else:    print("value not found in the array")

# # inserting an element in the array
# val = int(input("enter the value to insert "))
# for i in range(len(arr)):
#         arr.insert(i, val)
#         print("value inserted")
#         break

# print(arr)


# numpy is a library in python used for scientific computing and data analysis
# import numpy as np
# from numpy import *

# arr = array([[1,2,3,4,5],[6,7,8,9,10]],int)
# print(arr)

# array() ,linspace() ,arange() are the functions used to create arrays in numpy

# from numpy import *

# arr = array([1,2,3,4,5.4]) # if we try to create an array with different data types then it will convert all the elements to the same data type which is the highest data type in the hierarchy (float in this case)
# print(arr)
# print(arr.dtype)

# linspace() function is used to create an array of evenly spaced numbers over a specified interval
# arr = linspace(0,15,16) # it will create an array of 5 evenly spaced numbers between 0 and 10
# print(arr)

# arrange() function is used to create an array of evenly spaced numbers over a specified interval with a specified step size
# arr = arange(1,10,2) # it will create an array of numbers from 1 to 10 with a step of 2
# print(arr)

# arr = logspace(1,10,10) # it will create an array of 10 evenly spaced numbers between 1 and 10 on a logarithmic scale
# print(arr)

# zero()    # it will create an array of zeros with the specified shape
# arr = zeros(5)
# print(arr)

# ones()     # it will create an array of ones with the specified shape
# arr = ones(5,int)
# print(arr)

# from numpy import *

# arr = array([1,2,3,4,5])
# arr = arr + 5 # it will add 5 to each element of the array
# print(arr)

# vectorized operations in numpy
# arr1 = array([1,2,3,4,5])
# arr2 = array([6,7,8,9,10])

# arr3 = arr1 + arr2 # it will add the corresponding elements of the two arrays
# print(arr3)

# arr = array([1,2,3,4,5])
# print(sort(arr)) # it will print the first element of the array

# arr1 = array([1,2,3,4,5])
# arr2 = array([6,7,8,9,10])

# print(concatenate([arr1,arr2])) # it will concatenate the two arrays

# copying an array in numpy
# arr1 = array([1,2,3,4,5])
# arr2 = arr1.view() #it will create a new array which is a view of the original array, it will not create a new array in memory
# print(arr1)
# print(arr2)

# print(id(arr1))
# print(id(arr2))

# shallow copy means if we change the value of one array then it will change the value of the other
# array because both the arrays are pointing to the same memory location

# arr1 = array([1,2,3,4,5])
# arr2 = arr1.view()
# arr2[1] = 10
# print(arr1)
# print(arr2)



# arr1 = array ([
#             [1,2,3,5,6,8],
#             [4,5,6,1,2,3,]
#         ])

# arr2 = reshape(arr1,(2,2,3)) # it will reshape the array into a 3x4 matrix
# print(arr2)

# arr2 = arr1.flatten() # it will flatten the array into a 1D array
# print(arr2)

# print(arr1.ndim) # it will print the number of dimensions of the array
# print(arr1.shape) # it will print the shape of the array rows and columns
# print(arr1.size) # it will print the total number of elements in the array

# matrix

# arr = array([[1,2,3],[4,5,6],[7,8,9]])
# # matrix is a subclass of array in numpy which is used to represent a 2D array
# m = matrix(arr)
# print(m)

# m1 = matrix('1 2 3; 4 5 6; 7 8 9') # it will create a matrix from a string

# print(m1.diagonal())

# m1 = matrix('1 2 3; 4 5 6; 7 8 9')
# m2 = matrix('9 8 7; 6 5 4; 3 2 1')

# m3 = m1*m2
# print(m3)

# functions in python
# a function is a block of code which is used to perform a specific task, it is reusable and it can be called multiple times in a program

# def greet():
#     print("hello")
#     print("good morning")

# greet()

# addition of two numbers using functions
# def add_sub(a,b):
#     sum = a+b
#     sub = a-b
#     return sum, sub

# result1,result2 = add_sub(int(input("enter the first number ")),int(input("enter the second number ")))
# print(result1,result2)

# function arguments


# def update(x):
#     x = 8
#     print(x)

# update(10) # it will print 8 because we are changing the value of x inside the function but it will not change the value of x outside the function because we are passing a copy of the value to the function

# def update(x):
#     x = 8
#     print(x)
#     x[0] = 8
#     print(x)
    

# a = 10 
# update(a)

# lst = [1,2,3,4,5]
# update(lst)
# print(a) # it will print 10 because we are passing a copy of the value to the function and we are changing the value of x inside the function but it will not change the value of a outside the function because we are passing a copy of the value to the function

# types of arguments in python
# variable length arguments
# * indicates that the function can take any number of arguments and it will be stored in a tuple *b is tuple
# def add(a,*b): 
#     sum = a
#     for i in b:
#         sum = sum + i
#     return sum
# print(add(2,3,4,5,6))

# kwargs is used to pass a variable number of keyword arguments to a function and it will be stored in a dictionary

# keyword variable arguments
# example of kwargs
# ** indicates that the function can take any number of keyword arguments and it will be stored in a dictionary **data is a dictionary
# def person(name,**data):
#     print(name)
#     for key,value in data.items():
#         print(key,value)

# person("sameer",age=25,city="kalaburagi",phone=1234567890)

# global and local variables in python
# global variable is a variable which is declared outside the function and it can be accessed inside the function
# local variable is a variable which is declared inside the function and it can only be accessed inside the function

# scope of variables in python is the region of the program where the variable can be accessed

# a = 10 # global variable

# def func():
#     a=11 # local variable
#     print(a) 

# print(a) # it will print 10 because we are accessing the global variable a

# a= 10
# def func():
#     global a # it will tell the function that we are using the global variable a
#     a=11 # it will change the value of a to 11
#     print("in function",a)

# func()
# print("outside function",a) # it will print 11 because we have changed the value

# a = 10
# print(a) # it will print 10 because we are accessing the global variable a
# print(id(a)) # it will print the memory address of the variable a

# def func():
#     a = 11
    
#     x = globals()['a'] # it will return the value of the global variable a
#     print("in function",a)
#     print(id(a)) # it will print the memory address of the local variable a
#     print(id(x)) # it will print the memory address of the global variable a
#     globals()['a'] = 15 # it will change the value of the global variable a to 15
    
    
# result = func()
# print("outside function",a) # it will print 15 because we have changed the value of the global variable a inside the function

# pass a list to a function

# lst = int(input("enter the size of the list "))
# lst1 = []
# for i in range(lst):
#     x = int(input("enter the element "))
#     lst1.append(x)
    
# def count(lst):
#     even = 0
#     odd = 0
#     for i in lst:
#         if i%2==0:
#             even = even+1
#         else:
#             odd = odd+1
#     return even,odd


# even,odd = count(lst1)
# print("number of even numbers in the list is ",even)
# print("number of odd numbers in the list is ",odd)


# fibonacci sesquence
# def fib(n):
#     if n<=0:
#         print("please enter a positive integer")
        
#     else:
#         a=0
#         b=1
#         for i in range(n):
#             c = a+b
#             print(c)
#             a=b
#             b=c
        

# fib(int(input("enter the number of terms in the fibonacci sequence ")))

# fibonacci series last number less than 100

# a=0
# b=1

# while a<100:
#     print(a)
#     a,b = b,a+b

# factorial of a number

# def factorial(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i
#     return f

# fact = factorial(int(input("enter a number to find its factorial ")))
# print(fact)


# recursion in python
# def greet():
#     print("hello")
#     greet()

# print(greet())

# factorial of a number using recursion
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# fact = factorial(int(input("enter a number to find its factorial ")))
# print(fact)

# anonymous functions in python is known a function without a name
# lambda function is a small anonymous function which can take any number of arguments but can only have one expression
# functions are objects in python which means we can assign them to a variable and we can pass them as arguments to other functions

# f = lambda x,y: x+y

# result = f(5,6)

# print(result)

# def evenNum(n):
    
#     return n%2==0

# nums = [1,2,3,4,5,6,7,8,9,10]

# even = list(filter(evenNum,nums))

# print(even)

# using lambda function with filter function to find even numbers in a list

# nums = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda x: x%2==0,nums))

# # map function is used to apply a function to all the elements of a list and it returns a map object which is an iterator

# doubles = list(map(lambda x:x*2,even))

# from functools import reduce
# # def add_all(a,b):
# #     return a+b
# sum = reduce(lambda a,b: a+b, doubles)
# print(even)
# print(doubles)
# print(sum)

# decorsators in python are used to modify the behavior of a function without changing its code.
# It is a higher order function which takes a function as an argument and returns a modified version of the function.

# def div(a,b):
#     return a/b

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner

# div1 = smart_div(div)
# print(div1(2,4))

# Modules in python are files which contain functions and variables which can be used in other python files by importing them.
# It is a way to organize the code and make it reusable.

# from calc import *

# a = 10
# b = 20

# c= add(a,b)
# print("the sum of a and b is ",c)

# d = subtract(a,b)
# print("the difference of a and b is ",d)

# e = multiply(a,b)
# print("the product of a and b is ",e)

# f = divide(a,b)
# print("the division of a and b is ",f)

# special variables in python
# __name__ is a special variable in python which is used to check whether the python file
# is being run directly or being imported as a module in another file. 
# If the file is being run directly then the value of __name__ will be "__main__" and if the file is being imported as a module then the value of __name__ will be the name of the file.

# from calc import *
# print(__name__)

# def main():
#     print("hello")
#     print("welcome User")

# if __name__ == "__main__":
#     main()

# from calc import *

# def fun():
#     add()
#     print("from fun1")

# def fun2():
#     sub()
#     print("from fun2")

# # main function is the entry point of the program. It is the first function that is called when the program is run. 
# # It is used to call other functions and to execute the main logic of the program.
# def main():
#     fun()
#     fun2()

# calling the main function
# main()

# object oriented programming in python
# class is a blueprint for creating objects.
# It is a user defined data type which contains variables and functions which are used to represent the properties and behavior of an object.

# class computer:
#
#     def config(self):
#         print("i5, 8gb, 512")
#
# com1 = computer()
# com2 = computer()
# com1.config()
# com2.config()

# special method init

# class computer:
    
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram
    
#     def config(self):
#         print("config is",self.cpu, self.ram)

# com1 = computer('i5', 12)
# com2 = computer('ryzen', 16)
# com1.config()
# com2.config()

# Constructor, Self and Comparing Objects

# class computer:
#     pass

# com = computer()

# print(id(com))

# class computer:
    
#     def __init__(self):
#         self.name = 'sameer'
#         self.age = 28
    
#     def update(self):
#         self.age = 12
    
    
#     # self is c1
#     def compare(self,com2):
#         if self.age == com2.age:
#             return True
#         else:
#             return False

# com1 = computer()
# com1.age = 30
# com2 = computer()

# # com1.update()

# com1.name = 'pavan'

# if com1.compare(com2):
#     print("same age")

# else:
#     print("different age")

# print(com1.age)
# print(com1.name)
# print(com2.name)

# Types of Variables

# class Car:
    
#      wheel = 4 # class variable
    
#     def __init__(self):
#         self.mil = 10 #instance variable
#         self.name = 'BMW'  #instance variable

# c1 = Car()
# c2 = Car()

# c1.name = 'audi'
# c1.mil = 100
# Car.wheel = 2
# print(c1.mil,c1.name,c1.wheel)
# print(c2.mil,c2.name,c2.wheel)

# types of methods

# instance methods
# class methods
# static methods

# class Student:
    
#     school = 'sameer'
    
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     # -> to work with instance we use self key word
#     def avg(self):
#         return(self.m1 + self.m2 + self.m3)/3

#     def getM1(self):
#         return self.m1
    
#     def setM1(self,value):
#         self.m1 = value

#     # to work with class variables we have to use cls keyword
#     @classmethod
#     def getSchoolName(cls):
#         return cls.school
    
#     # methods with no arguements like "cls" and "self" are known as static methods
#     @staticmethod
#     def info():
#         return("this is student class.. in abc module")

# s1 = Student(34,32,84)
# s2  = Student(55,66,77)

# print(s1.avg())
# print(s2.avg())
# print(Student.getSchoolName())
# print(Student.info())

# inner class means a class inside a class

# class Student:
    
#     class Laptop:
        
#         def __init__(self):
#             self.brand = 'hp'
#             self.cpu = 'i5'
#             self.ram = 8
        
#         def show(self):
#             print(self.brand,self.cpu,self.ram)
    
#     def __init__(self,name,rollNo):
#         self.name = name
#         self.rollNo = rollNo
#         # inner classes are called in outer classes
#         # we can create object of inner class in outer class
#         self.lap = self.Laptop()
    
#     def show(self):
#         print(self.name,self.rollNo)
#         self.lap.show()

# s1 = Student('Sameer',23)
# s2 = Student('Pavan',25)

# s1.show()
# s2.show()


# decorators -> Using decorators we can add extra features to a existing functions
# def div(a,b):
#     print(a/b)

# def smart_div(func):
    
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner

# div = smart_div(div)

# div(2,4)

# inheritance
# class A:
    
#     def feature1(self):
#         print("feature 1 working")
    
#     def feature2(self):
#         print("feature 2 working")

# class B is inheriting class A
# class B(A):
#     def feature3(self):
#         print("feature 3 working")
    
#     def feature4(self):
#         print("feature 4 working")

# # multi level inheritance -> class C is inheriting class B and class B is inheriting class A
# class C(B):
#     def feature5(self):
#         print("feature 5 working")

# # multiple inheritance -> class D is inheriting class A and class B
# class D(B,A):
#     def feature6(self):
#         print("feature 6 working")

# a1 = A()
# a1.feature1()
# a1.feature2()

# b1 = B()
# b1.feature1()
# b1.feature2()

# c1 = C()

# d1 = D()
# d1.feature1()

# constructor in inheritance

# class A:
    
#     def __init__(self):
#         print("A in init")

#     def feature1(self):
#         print("feature 1 working")

#     def feature2(self):
#         print("feature 2 working")

# class B(A):

#     def __init__(self):
#         # super() is used to call the constructor of the parent class
#         super().__init__()
#         print("B in init")
    
#     def feature3(self):
#         print("feature 3 working")
    
#     def feature4(self):
#         print("feature 4 working")

# a1 = B()

# class A:
    
#     def __init__(self):
#         print("A in init")

#     def feature1(self):
#         print("feature 1 working")

#     def feature2(self):
#         print("feature 2 working")

# class B(A):

#     def __init__(self):
#         print("B-A1 in init")
    
#     def feature3(self):
#         print("feature 3A-1 working")
    
#     def feature4(self):
#         print("feature 4 working")

# class C(B,A):
#     def __init__(self):
#         # its always from left to right in case of multiple inheritance means 
#         # it will call the constructor of the class which is on the left side first
#         # in this case it will call the constructor of B first and then A
#         super().__init__()
#         print("C in init")
    
#     def feat(self):
#         super().feature2()
    

# a1 = C()
# a1.feat()

# Polymorphism
# poly -> many
# morph -> form

# Duck Typing 
# Duck Typing is a concept in Python that is used to implement polymorphism.

# class vsCode:

#     def execute(self):
#         print("compiling")
#         print("running")

# class Laptop:

#     def code(self,ide):
#         ide.execute()

# ide = vsCode()

# lap = Laptop()
# lap.code(ide)

# class vsCode:

#     def execute(self):
#         print("compiling")
#         print("running")

# class PyCharm:

#     def execute(self):
#         print("compiling")
#         print("running")
#         print("executing")

# class Laptop:

#     def code(self,ide):
#         ide.execute()

# ide = PyCharm()

# lap = Laptop()
# lap.code(ide)

# Operator overloading
 
# class Student:
    
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
    
#     # in the place of + we are using __add__ method
#     # and self refers to s1 and other refers to s2
#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)
#         return s3
    
#     # operator overloading is a concept in python that is used to implement polymorphism by 
#     # overloading the operators and methods
#     # > operator is overloaded using __gt__ method
#     def __gt__(self,other):
#         r1 = self.m1 + self.m2
#         r2 = other.m1 + other.m2
#         if r1 > r2:
#             return True
#         else:
#             return False

#     def __str__(self):
#         # format is used to format the string
#         # it is used to print the object in a readable format
#         return "{} {}".format(self.m1,self.m2)


# s1 = Student(10,20)
# s2 = Student(20,40)

# s3 = s1 + s2

# print(s3.m1)
# print(s3.m2)

# if s1 > s2:
#     print("s1 wins")
# else:
#     print("s2 wins")

# print(s1)
# print(s2)

# Method Overloading and Method Overriding
# method overloading
# class Student:
    
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             s = a+b+c
#         elif a!=None and b!=None:
#             s = a+b
#         elif a!=None:
#             s = a
#         return s

# print(Student().sum(3))

# Method Overriding
# class A:
#     def show(self):
#         print("in A")

# class B(A):
#     def show(self):
#         print("in B")

# a=A()
# a.show()
# a=B()
# a.show()
# b=B()
# b.show()

# Abstract class And Abstract Methods
# abstract class is a class that is not instantiated 
# abstract method is a method that is not implemented
# we use abc(abstract base class) module to create abstract class and abstract method
# abstract class will have atleast one abstract method
# abstract methods are the methods which dont have body

# from abc import ABC,abstractmethod

# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass

# class whiteboard:
#     def write(self):
#         print("its writing")

# class Laptop(Computer):
#     def process(self):
#         print("Its working")
        
# class Programmer:
#     def work(self,com):
#         print("coding")
#         com.process()

# # c = Computer()
# # c.process()

# w = whiteboard()
# l = Laptop()
# # l.process()

# p = Programmer()
# p.work(l)
# p.work(w)

# iterator

# nums = [1,2,3,4,5]

# it = iter(nums)
# print(it.__next__())

# class TopTen:
#     def __init__(self):
#         self.num = 1
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):

#         if self.num <= 10:
#            val = self.num
#            self.num += 1
#            return val
#         else:
#             raise StopIteration
           
       

# values = TopTen()
# print(next(values))

# for i in values:
#     print(i)

# Generator
# generator is a function that returns an iterator
# yield is special function which maks a function a generator
# yield is used to return a value from a function

# def topten():
#     n=1
#     while n <= 10:
#         sq = n*n
#         yield sq
#         n += 1

# values = topten()

# for i in values:
#     print(i)

# Exception Handling
# Exception is an error that occurs during the execution of a program 
# a=1
# b=2

# try:
#     print("resource opened")
#     print(a/b)
#     k = int(input("enter a number"))
#     print(k)

# except Exception as e:
#     print("you cannot divide by zero")
#     print(e)

# finally:
#     print("resource closed")

# Multithreading 
# Multithreading is known as concurrency execution of multiple threads at the same time
# thread is a single sequence of execution in a program
# process is a program that is executing
# the process execution is done main thread
# from threading import *
# import time


# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("hello")
#             time.sleep(1)
            


# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("hi")
#             time.sleep(1)
            

# t1 = Hello()
# t2 = Hi()

# t1.start()
# time.sleep(0.2) # it will give chance to the other thread to run and avoid collision
# t2.start()
# t1.join()
# t2.join()
# print("bye")
# start() method is used to start the thread
# run() method is used to run the thread
# join() method is used to wait for the thread to complete

# File Handling
# r -> read file


# f = open("mydata.txt","r")
# print(f.read()) # it will read only one line
# # w -> write file
# # a -> append file

# f2 = open("mydata.txt","a")
# f2.write("iam 23 years old")
# print(f2)

# file = open("something.txt","r")
# print(file.read())
# rb -> read binary

# f = open("mydata.txt","r")

# f1 = open("something.txt","w")

# for i in f:
#     print(i)

# f = open("goku.jpg","rb")

# for i in f:
#     print(i)

# f = open("goku.jpg","wb")

# for i in f:
#     f.write(i)

# comments
# python is a single line comment language
# is Python Compiled or Interpreted Language?
# Python is both compiled and interpreted language
# because it is compiled first and then interpreted in machine language(code)

# Linear Search Using Python

# from array import *

# def search(lst,n):
#     i=0

#     while i<len(lst):
#         if lst[i]==n:
#             print("found at index",i)
#             return True
#         i+=1
#     return False

# size = int(input("enter the size of the array "))
# a = array('i',[])
# for i in range(size):
#     x = int(input("enter the element "))
#     a.append(x)

# n=int(input("enter the element to search "))

# if search(a,n):
#     print("found")
# else:
#     print("not found")

# Using for loop

# from array import *

# def search(lst,n):
#     for i in range(len(lst)):
#         if lst[i]==n:
#             print("found at index",i)
#             return True
#     return False

# size = int(input("enter the size of the array "))
# a = array('i',[])
# for i in range(size):
#     x = int(input("enter the element "))
#     a.append(x)

# n=int(input("enter the element to search "))

# if search(a,n):
#     print("found")
# else:
#     print("not found")

# Binary Search

# from array import *

# def search(lst,n):
#     l=0
#     u = len(lst)-1

#     while l<=u:
#         mid = (l+u)//2
#         if lst[mid]==n:
#             print("found at index",mid)
#             return True
#         elif lst[mid]<n:
#             l = mid+1
#         else:
#             u = mid-1
#     return False

# size = int(input("enter the size of the array "))
# a = array('i',[])
# for i in range(size):
#     x = int(input("enter the element "))
#     a.append(x)

# n=int(input("enter the element to search "))

# if search(a,n):
#     print("found")
# else:
#     print("not found")

# Bubble Sort

# from array import *

# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
#     return nums

# x = int(input("enter the size of the array "))
# nums = array('i',[])
# for i in range(x):
#     a = int(input("enter the element "))
#     nums.append(a)

# sort(nums)
# print(nums)


# Selection Sort

from array import *

def sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
    return nums


x = int(input("enter the size of the array "))
nums = array('i',[])
for i in range(x):
    a = int(input("enter the element "))
    nums.append(a)

sorted_nums = sort(nums)
print(sorted_nums)


