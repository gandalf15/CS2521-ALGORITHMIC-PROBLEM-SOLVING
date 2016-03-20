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
	left_indices = left_hell.pop()	#get indices from the list
	right_indices = right_hell.pop()
	left_hell_most_right_index = left_indices[1]
	right_hell_most_left_index = right_indices[0]

	num_of_left_points = len(left_hell)
	num_of_right_points = len(right_hell)
	x_of_line = float((left_hell[left_hell_most_right_index][0] +\
	 			right_hell[right_hell_most_left_index][0])/2)


	# if base case then order the points clockwise and deque
	if num_of_left_points < 4:
		for i in left_hell:
			if num_of_left_points > 2:
				if left_hell[num_of_left_points-2][1] < left_hell[num_of_left_points-3][1]:
					left_hell = [left_hell[2],left_hell[1],left_hell[0]]
					left_hell = deque(left_hell)
				else:
					left_hell = [left_hell[2],left_hell[0],left_hell[1]]
					left_hell = deque(left_hell)
			else:
				left_hell = deque(left_hell)
				left_hell.rotate(1)
	if num_of_right_points < 4:
		for i in right_hell:
			if num_of_right_points > 2:
				if right_hell[num_of_right_points-2][1] < right_hell[num_of_right_points-3][1]:
					right_hell = [right_hell[2],right_hell[1],right_hell[0]]
					right_hell = deque(right_hell)
				else:
					right_hell = [right_hell[2],right_hell[0],right_hell[1]]
					right_hell = deque(right_hell)
			else:
				right_hell = deque(right_hell)
				right_hell.rotate(1)
	#hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm


	i = left_hell_most_right_index	# the most right point on X in left hell
	j = right_hell_most_left_index	#the most left point on X in right hell
	print(left_hell[i])
	print (left_hell)
	print(right_hell[j])
	print (right_hell)
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
	while (get_y_intersection(left_hell[i],right_hell[(j-1)%num_of_right_points], x_of_line) >
			get_y_intersection(left_hell[i],right_hell[j], x_of_line)
			or get_y_intersection(left_hell[(i+1)%num_of_left_points],right_hell[j], x_of_line) >
			get_y_intersection(left_hell[i],right_hell[j], x_of_line)):

		if (get_y_intersection(left_hell[i],right_hell[(j-1)%num_of_right_points], x_of_line) >
			get_y_intersection(left_hell[i],right_hell[j], x_of_line)):
			j = (j-1)%num_of_right_points		#move right
			# mod is there because after iterate to the last point in array
			# we want to return to the 0 index, so the last point is connected with the first
		else:
			i = (i+1)%num_of_left_points		#move left
			# mod is there because after iterate to the last point in array
			# we want to return to the 0 index, so the last point is connected with the first
		pass
	lower_tangent = [i,j]	#array of two indices which represent points coords.
	tangents = [upper_tangent,lower_tangent]
	indices = [left_indices[0], right_indices[1]]	# send further left, right points
	tangents.append(indices)
	return tangents

def merge_convex_hells(tangents, left_convex, right_convex):
	upper_tangent = tangents[0]	#extract upper tangent
	lower_tangent = tangents[1]	#extract lower tangent
	indices = tangents[2]	#extract indices of left and right
	num_of_left_points = len(left_convex)
	num_of_right_points = len(right_convex)


	#start with upper_tangent
	new_convex = [left_convex[upper_tangent[0]],right_convex[upper_tangent[1]]]





	'''
	# this loop is for right_convex
	for i in range(upper_tangent[1]+1, num_of_right_points + upper_tangent[1]):
		#it takes care if the i should return to the start of the array
		j = i%num_of_right_points
		# this if is necessary for discarting inner points
		if j == lower_tangent[1]:
			new_convex.append(right_convex[j])
			break
		else:
			new_convex.append(right_convex[j])
	# this loop is for left_convex
	for i in range(lower_tangent[0], num_of_left_points + lower_tangent[0]):
		#it takes care if the i should return to the start of the array
		j = i%num_of_right_points
		# this if is necessary for discarting inner points
		if j == upper_tangent[0]:
			new_convex.append(left_convex[j])
			break
		else:
			new_convex.append(left_convex[i])
	'''
	new_convex.append(indices)
	return new_convex	#this is new convex hell without inner points




def make_convex_hell(array):
	#array comes already sorted based on X coordinates
	try:
		if len(array) < 4:
			most_left = 0	#initialize with some index, cannot be 0
			most_right = len(array)-1	#initialize with some index, cannot be 0
			'''
			index = 0
			for i in array:
				if i[0] < array[most_left][0]:
					most_left = index
				elif i[0] > array[most_right][0]:
					most_right = index
				else:
					pass
				index = index + 1	#increment the index of the point in array
			'''
			indices = [most_left, most_right]
			array.append(indices)	#at the end append indices of the left and right points
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
	convex_hell.pop()
	print (convex_hell)

except KeyboardInterrupt:
	print ("  Quit")
