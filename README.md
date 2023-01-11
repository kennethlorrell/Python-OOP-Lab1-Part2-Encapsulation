# Lab #01. Part 2 (Encapsulation)

## Task #01
Create a class Rectangle with attributes length and width, each of which defaults to 1. 
Provide methods that calculate the perimeter and the area of the rectangle. 
Also, provide setter and getter for the length and width attributes. 
The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.

## Task #02
Create a class called Rational for performing arithmetic with fractions. 
Write a program to test your class. 
Use integer variables to represent the private data of the class – the numerator and the denominator.
Provide a __init__() method that enables an object of this class to be initialized when it’s declared. 
The __init__() should contain default parameter values in case no initializers are provided and should store the fraction in reduced form. 
For example, the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator. 
Provide public methods that perform each of the following tasks:
- printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
- printing Rational numbers in floating-point format.

## Task #03
Create a class that descibes a Product of online store. 
As a Product fields you can use a price, description and product' dimensions.
Create a class that describes a Customer. 
As a Customer fields you can use surname, name, patronymic, mobile phone, etc.
Create a class that describes an Order.
- the order must contain data about the customer who carried it out and products. 
Implement a method for calculating the total order value.

## Task #04
Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc. 
Determine the required attributes-data and attributes-methods in class for working with the text file.

## Task #05
The class GROUP contains a sequence of instances of the class STUDENT. 
The class STUDENT contains the student's name, surname, record book number and grades.
Determine the required attributes-data and attributes-methods in classes GROUP and STUDENT. 
Find the average score of each student. 
Output to the standard output stream the five students with the highest average score.
Assume that there can be no more than 20 students in a group, as well as students with the same name and surname.

## Task #06
Create a class BINARY TREE that contains background information of product prices (product code, price of 1 product). 
The tree is sorted by product codes. 
From the keyboard enter data on the number of products in the format: product code, number of products. 
Using a tree, find the cost of products (cost = quantity * price of one product).
