Stock Price Analysis Project
import streamlit as st
import pandas as pd
import timeit
import time

print("Hello everyone! Testing my Github.")
print("This code is written by Waiee Zainol.")
print("Test third commmit.")

#Menu

print("noob")
print("ANjing")
print("dah dah ah tu")


















# #Python Execution Time
#
# #Test repeat biasa, while loop & for loop
# print("Example of Python execution time: \n")
# print("Repeat, while loop, and for loop comparison: ")
# print("1.", timeit.timeit(stmt='x=0', setup='', number=1000000))
# print("2.",timeit.timeit(stmt='while x < 1000000: x += 1', setup='x=0', number=1))
# print("3.",timeit.timeit(stmt='for x in range(1000000): pass', setup='', number=1))
#
# # print(timeit.timeit(stmt='x-=0; y=0', setup='', number=1000000))
# # print(timeit.timeit(stmt='while x < 1000000: x += 1; y += 1', setup='x=0; y=0', number=1))
#
# ########################################################
#
# # #Repeat 6 times
# # print("")
# # print("Repeat 6 times: ")
# # print(timeit.timeit(stmt='while x < 1000000: x += 1', setup='x=0', number=1))
# # print(timeit.timeit(stmt='while x < 1000000: x += 1', setup='x=0', number=1))
# # print(timeit.timeit(stmt='while x < 1000000: x += 1', setup='x=0', number=1))
# # print(timeit.timeit(stmt='while x < 1000000: x += 1', setup='x=0', number=1))
# # print(timeit.timeit(stmt='while x < 1000000: x += 1', setup='x=0', number=1))
#
# # print(timeit.repeat(stmt='while x < 1000000: x += 1', setup='x=0', repeat=5, number=1))
#
# ########################################################
#
# #Function for long pieces of code
#
# #build function
# def test_function():
#     for x  in range(1000000):
#         pass
#
# #handle exception - SyntaxError
# print("")
# print("Long code comparison: ")
# try:
#     print("1.",timeit.timeit(stmt='test_function()', setup='from __main__ import test_function', number=1))
#     print("2.",timeit.timeit(stmt='test_function()', setup='', number=1, globals=globals()))
# except SyntaxError:
#     print("SyntaxError occured.")
