import csv
# import turtle
# turtle.pensize(5)
import operator
pointA = []
pointB = []

scale = (100,100)

# Read data from csv files first pointA
with open('output.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:

    	# print (row,'ggg')
    	results = tuple(map(float, row))
    	pointA.append(results)

print ("pointA : " ,pointA)

# Read data from csv files pointB
with open('output3.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:

    	results = tuple(map(float, row))
    	pointB.append(results)


print ("pointB : " ,pointB)

# Comapre both data on list
for i,k in zip(pointA ,pointB):
    new = [a-b for a, b in zip(i, k)]
    print ('Differnce',new)
    if (new[0] > 1)|(new[1] > 1)|(new[1] < -1)|(new[1] < -1):
    	print ('1 meter above from pathA',new)