import random
from operator import itemgetter
from collections import deque
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
		slope = float((point_b[1]-point_a[1])/(point_b[0]-point_a[0]))
		#calculate the point where line between points a and b intersects with vertical line
		y_coord_of_intersection = float(point_a[1]+((x_coord_of_line - point_a[0])*slope))
		#return float y_coord_of_intersection
		return y_coord_of_intersection

	except ZeroDivisionError:
		print ("After 7.5 million years....",
		"The Answer to the Ultimate Question of Life, The Universe, and Everything is 42.")

def get_tangents(left_hell, right_hell):
	# points are named a1,a2... clockwise for left convex
	# points are named b1,b2,... clockwise for right convex
	# for left convex a1 is the right most point
	# for right convex b1 is the left most point
	# Y is the vertical line between them
	#here starts get upper tangent

	#somehow shift the points in array so left_convex on index 0 has
	#the right most point. Do the same with right_convex[0] has the left most point
	# also create a vertical line between these points.


	left_hell_most_right_point = itemgetter()
	right_hell_most_right_point = itemgetter()
	left_convex = deque(left_hell)
	right_convex = deque(right_hell)



	num_of_left_points = len(left_convex)
	num_of_right_points = len(left_convex)
	x_of_line = (point_a[0]+point_b[0])/2
	i = 0	# the most right point on X
	j = 0	#the most left point on X
	while (get_y_intersection(left_convex[i],right_convex[j+1], x_of_line) >
			get_y_intersection(left_convex[i],right_convex[j], x_of_line)
			or get_y_intersection(left_convex[i-1],right_convex[j], x_of_line) >
			get_y_intersection(left_convex[i],right_convex[j], x_of_line)):

		if (get_y_intersection(left_convex[i],right_convex[j+1], x_of_line) >
			get_y_intersection(left_convex[i],right_convex[j], x_of_line)):
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
	i = 0	# reset the most right point on X
	j = 0	# reset the most left point on X
	while (get_y_intersection(left_convex[i],right_convex[j-1], x_of_line) >
			get_y_intersection(left_convex[i],right_convex[j], x_of_line)
			or get_y_intersection(left_convex[i+1],right_convex[j], x_of_line) >
			get_y_intersection(left_convex[i],right_convex[j], x_of_line)):

		if (get_y_intersection(left_convex[i],right_convex[j-1], x_of_line) >
			get_y_intersection(left_convex[i],right_convex[j], x_of_line)):
			j = (j-1)%num_of_right_points		#move right
			# mod is there because after iterate to the last point in array
			# we want to return to the 0 index, so the last point is connected with the first
		else:
			i = (i+1)%num_of_left_points		#move left
			# mod is there because after iterate to the last point in array
			# we want to return to the 0 index, so the last point is connected with the first
		pass
	lower_tangent = [i,j]	#array of two arrays which represent points coords.
	tangents = [upper_tangent,lower_tangent]
	return tangents

def merge_convex_hells(tangents, left_convex, right_convex):
	upper_tangent = tangents[0]	#extract lower tangent
	lower_tangent = tangents[1]	#extract upper tangent
	num_of_left_points = len(left_convex)
	num_of_right_points = len(right_convex)
	#start with upper_tangent
	new_convex = [left_convex[upper_tangent[0]],right_convex[upper_tangent[1]]]
	# this loop is for right_convex
	for i in range(upper_tangent[1]+1, num_of_right_points + upper_tangent[1]):
		#first if takes care if the i should return to the start of the array
		if i >= num_of_right_points:
			j = i%num_of_right_points
		# this if is necessary for discarting inner points
		if j == lower_tangent[1]:
			new_convex.append(right_convex[j])
			break
		else:
			new_convex.append(right_convex[j])
	# this loop is for left_convex
	for i in range(lower_tangent[0], num_of_left_points + lower_tangent[0]):
		#first if takes care if the i should return to the start of the array
		if i >= num_of_left_points:
			j = i%num_of_right_points
		# this if is necessary for discarting inner points
		if j == upper_tangent[0]:
			new_convex.append(left_convex[j])
			break
		else:
			new_convex.append(left_convex[i])
	return new_convex	#this is new convex hell without inner points




def make_convex_hell(array):
	#array comes already sorted based on X coordinates
	try:
		if len(array) < 4:
			return array	#this is base case when 3 points are convex hell
		else:
			length = len(array)
			left_convex = make_convex_hell(array[0:length // 2])
			right_convex = make_convex_hell(array[length // 2:])
			tangents = get_tangents(left_convex, right_convex)
			new_convex_hell = merge_convex_hells(tangents, left_convex, right_convex)
		return new_convex_hell

	except ValueError:
		print("The convex hull function takes array of arrays with two integer inside.")

try:
	#generate random, but uniq points no x and y coordinates are same
	uniq_points = gen_rand_uniq_points(10,10,6)
	#sort based on x coordinate
	uniq_points = sorted(uniq_points, key=itemgetter(0))
	convex_hell = make_convex_hell(uniq_points)
	print (convex_hell)

except KeyboardInterrupt:
	print ("  Quit")
