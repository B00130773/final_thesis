import csv
import turtle
turtle.pensize(5)
import operator
points = []
scale = (500,500)
# print ('hellooooo')
with open('output.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:

    	# print (row,'ggg')
    	results = tuple(map(float, row))
    	points.append(results)

# Testing
# print (points)
# Drawing
turtle.penup()
for i in points:
	data = tuple(map(operator.mul, scale, i))
	print(data)
	turtle.goto(data)
	turtle.pendown()






turtle.hideturtle()
turtle.exitonclick()