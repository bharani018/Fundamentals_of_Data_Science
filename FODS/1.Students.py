''' You are working on a project that involves analysing students  performance data for class of 40 students.
The data is stored in numpy array named as students course where each row represent a student and each column represent a different subject
#The subjects are arranged in following order Maths sience english and history.
Your task is to calculate the average score for each subject and identify the subjet with highest score.
#Assume 4x4 matrix that stores marks of each student in the given order.  '''


import numpy as np
import pandas as pd


a = pd.read_csv("students.csv")
b = a.select_dtypes(include=[np.number])
x = b.mean()

h = np.argmax(x)

su = ['Maths','Science','English','History']

print("Mean: ",x)
print("Max sub: ",su[h])
