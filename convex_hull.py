import random
import time
import matplotlib.pyplot as plt
from operator import itemgetter
def gen_rand_uniq_points(x_range, y_range, n):
	try:
		x_points = random.sample(range(0, x_range), n)
		y_points = random.sample(range(0, y_range), n)
		points = []
		for i in range(0,n):
			points.append([x_points[i],y_points[i]])
		return points

	except ValueError:
		print('Sample size exceeded population size.')

def get_y_intersection(point_a, point_b, x_of_line):
	try:
		#define where is the vertical line
		x_coord_of_line = x_of_line
		# calculate the slope between two points
		slope = float((point_b[1]-point_a[1]))/float((point_b[0]-point_a[0]))
		#calculate the point where line between points a and b intersects with vertical line
		y_coord_of_intersection = point_a[1]+((x_coord_of_line - point_a[0])*slope)
		#return float y_coord_of_intersection
		return y_coord_of_intersection

	except ZeroDivisionError:
		print ("After 7.5 million years....",
		"The Answer to the Ultimate Question of Life, The Universe, and Everything is 42.")

def get_tangents(left_hell, right_hell):
	#here starts get upper tangent
	left_indices = left_hell.pop()	#get indices from the list
	right_indices = right_hell.pop()
	left_proces_mark = left_hell.pop()
	right_proces_mark = right_hell.pop()
	left_hell_most_right_index = left_indices[1]
	right_hell_most_left_index = right_indices[0]
	num_of_left_points = len(left_hell)
	num_of_right_points = len(right_hell)
	x_of_line = float((left_hell[left_hell_most_right_index][0] +\
	 			right_hell[right_hell_most_left_index][0])/2.0)
	# if base case then order the points clockwise
	if num_of_left_points < 4 and left_proces_mark == 0:
		if num_of_left_points > 2:	#exactly 3 points then - do some magic please
			if (get_y_intersection(left_hell[0],left_hell[2],left_hell[1][0]) < left_hell[1][1]):
				left_hell = [left_hell[2],left_hell[0],left_hell[1]]
				left_indices = [1,0]
				left_hell_most_right_index = 0
				left_proces_mark == 1
				#this created clockwise order from right, bottom and up
			else:
				left_hell = [left_hell[2],left_hell[1],left_hell[0]]
				left_indices = [2,0]
				left_hell_most_right_index = 0
				left_proces_mark == 1
		else:	#exactly 2 points
			left_hell = [left_hell[1],left_hell[0]]
			left_indices = [1,0]
			left_hell_most_right_index = 0
			left_proces_mark == 1
	if num_of_right_points < 4 and right_proces_mark == 0:
		if num_of_right_points > 2:	# here must be different num for same clockwise
			if (get_y_intersection(right_hell[0],right_hell[2],right_hell[1][0]) < right_hell[1][1]):
				right_hell = [right_hell[0],right_hell[1],right_hell[2]]
				right_indices = [0,2]
				right_hell_most_left_index = 0
				right_proces_mark = 1
			else:
				right_hell = [right_hell[0],right_hell[2],right_hell[1]]
				right_indices = [0,1]
				right_hell_most_left_index = 0
				right_proces_mark = 1
		else:
			right_indices = [0,1]
			right_hell_most_left_index = 0
			right_proces_mark = 1
	#now the arrays are ordered clockwise form the middle line
	i = left_hell_most_right_index	# the most right point on X in left hell
	j = right_hell_most_left_index	#the most left point on X in right hell
	while (get_y_intersection(left_hell[i],right_hell[(j+1)%num_of_right_points], x_of_line) >
			get_y_intersection(left_hell[i],right_hell[j], x_of_line)
			or get_y_intersection(left_hell[(i-1)%num_of_left_points],right_hell[j], x_of_line) >
			get_y_intersection(left_hell[i],right_hell[j], x_of_line)):

		if (get_y_intersection(left_hell[i],right_hell[(j+1)%num_of_right_points], x_of_line) >
			get_y_intersection(left_hell[i],right_hell[j], x_of_line)):
			j = (j+1)%num_of_right_points		#move right
			# mod is there because after iterate to the last point in array
			# we want to return to the 0 index, so the last point is connected with the first
		else:
			i = (i-1)%num_of_left_points		#move left
			# mod is there because after iterate to the last point in array
			# we want to return to the 0 index, so the last point is connected with the first
		pass
	upper_tangent = [i,j]	#array of indices which represent points coords.
	#here starts get lower tangent
	i = left_hell_most_right_index	# reset the most right point on X
	j = right_hell_most_left_index	# reset the most left point on X
	while (get_y_intersection(left_hell[i],right_hell[(j-1)%num_of_right_points], x_of_line) <
			get_y_intersection(left_hell[i],right_hell[j], x_of_line)
			or get_y_intersection(left_hell[(i+1)%num_of_left_points],right_hell[j], x_of_line) <
			get_y_intersection(left_hell[i],right_hell[j], x_of_line)):

		if (get_y_intersection(left_hell[i],right_hell[(j-1)%num_of_right_points], x_of_line) <
			get_y_intersection(left_hell[i],right_hell[j], x_of_line)):
			j = (j-1)%num_of_right_points		#move right
			# mod is there because after iterate to the last point in array
			# we want to return to the 0 index, so the last point is connected with the first
		else:
			i = (i+1)%num_of_left_points		#move left

	lower_tangent = [i,j]	#array of two indices which represent points coords.
	tangents = [upper_tangent,lower_tangent]
	indices = [left_indices[0], right_indices[1]]	# send further left, right points
	right_hell.append(right_proces_mark)
	left_hell.append(left_proces_mark)
	result = [left_hell,right_hell,tangents,indices]
	return result

def merge_convex_hells(left_convex, right_convex, tangents, indices):
	upper_tangent = tangents[0]	#extract upper tangent
	lower_tangent = tangents[1]	#extract lower tangent
	left_proces_mark = left_convex.pop()
	right_proces_mark = right_convex.pop()
	num_of_left_points = len(left_convex)
	num_of_right_points = len(right_convex)
	most_left = indices[0]
	most_right = indices[1]

	if most_left == upper_tangent[0]:	# if the upper tangent is most left point
		new_convex = [left_convex[upper_tangent[0]]]
		most_left = 0
	else:
		new_convex = [left_convex[upper_tangent[0]]]

	next_point = upper_tangent[1]
	if indices[1] == next_point:	# if the upper tangent is most right point
		most_right = 1

	if next_point != lower_tangent[1]:
		new_convex.append(right_convex[upper_tangent[1]])
		next_point = (upper_tangent[1]+1)%num_of_right_points
		if indices[1] == next_point:
			most_right = 2
		while next_point != lower_tangent[1]:
			new_convex.append(right_convex[next_point])
			if indices[1] == next_point:
				most_right = len(new_convex)-1
			next_point = (next_point + 1)%num_of_right_points

	new_convex.append(right_convex[next_point])	# if ther is only one point for upper and lower tangents
	if indices[1] == next_point:
		most_right = len(new_convex)-1

		#then append the right lower bound
	next_point = lower_tangent[0]

	if next_point != upper_tangent[0]:
		new_convex.append(left_convex[lower_tangent[0]])
		if indices[0] == next_point:
			most_left = len(new_convex)-1
		next_point = (lower_tangent[0] + 1)%num_of_left_points
		while next_point != upper_tangent[0]:
			new_convex.append(left_convex[next_point])
			if indices[0] == next_point:
				most_left = len(new_convex)-1
			next_point = (next_point + 1)%num_of_left_points

	new_convex.append(1)
	new_convex.append([most_left, most_right])
	return new_convex	#this is new convex hell without inner points

def make_convex_hell(array):
	#array comes already sorted based on X coordinates
	try:
		if len(array) < 4:
			most_left = 0	#initialize with some index, cannot be 0
			most_right = len(array)-1	#initialize with some index, cannot be 0
			indices = [most_left, most_right]
			array.append(0)	#mark it that it will be processed
			array.append(indices)	#at the end append indices of the left and right points
			return array	#this is base case when 3 points are convex hell
		else:
			length = len(array)
			left_convex = make_convex_hell(array[0:length // 2])
			right_convex = make_convex_hell(array[length // 2:])
			result = get_tangents(left_convex, right_convex)
			indices = result.pop()
			tangents = result.pop()
			right_hell = result.pop()
			left_hell = result.pop()
			new_convex_hell = merge_convex_hells(left_hell, right_hell, tangents, indices)
		return new_convex_hell

	except ValueError:
		print("The convex hull function takes array of arrays with two integer inside.")

def benchmark():
	n = 1000000
	x = n+1
	y = n+1
	j = 0
	f = open('output.txt', 'w')
	while n > 0:
		uniq_points = gen_rand_uniq_points(x,y,n)
		uniq_points = sorted(uniq_points, key=itemgetter(0))
		time.sleep(0.2)
		start = time.clock()
		make_convex_hell(uniq_points)
		elapsed = time.clock()
		f.write('{} = {}\n'.format(n, elapsed-start))
		j += 1
		if j == 5:
			n = 500000
		elif j== 10:
			n = 100000

		elif j == 15:
			n = 10000

		elif j == 20:
			n = 1000
		elif j == 25:
			n = 100
		elif j == 30:
			n = 10
		elif j == 35:
			n = 0
			f.close

try:
	#benchmark()
	
	#generate random, but uniq points no x and y coordinates are same
	uniq_points = gen_rand_uniq_points(500,500,100)
	#sort based on x coordinate
	uniq_points = sorted(uniq_points, key=itemgetter(0))
	start = time.clock()
	convex_hell = make_convex_hell(uniq_points)
	elapsed = time.clock()
	print(elapsed - start)

	indices = convex_hell.pop()
	proces_mark = convex_hell.pop()
	#print("indices at the end ", indices)
	#print ("convex_hell ", convex_hell)

	x_points = []
	y_points = []
	plt.axis([-100, 1000, -100, 1000])
	for point in uniq_points:
		plt.plot(point[0],point[1], 'ro')
	for point in convex_hell:
		x_points.append(point[0])
		y_points.append(point[1])
	x_points.append(convex_hell[0][0])
	y_points.append(convex_hell[0][1])
	plt.plot(x_points,y_points)
	plt.show()
	
except KeyboardInterrupt:
	print ("  Quit")
