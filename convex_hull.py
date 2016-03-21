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
		#print(point_a, point_b, x_of_line)
		#define where is the vertical line
		x_coord_of_line = x_of_line
		# calculate the slope between two points
		slope = float((point_b[1]-point_a[1]))/float((point_b[0]-point_a[0]))
		#calculate the point where line between points a and b intersects with vertical line
		y_coord_of_intersection = point_a[1]+((x_coord_of_line - point_a[0])*slope)
		#return float y_coord_of_intersection
		#print(y_coord_of_intersection)
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
	 			right_hell[right_hell_most_left_index][0])/2.0)

	# if base case then order the points clockwise and deque
	if num_of_left_points < 4:
		if num_of_left_points > 2:	#exactly 3 points then - do some magic please
			if (left_hell[0][1] > left_hell[1][1] and left_hell[2][1] < left_hell[1][1]) or\
			 (left_hell[0][1] < left_hell[1][1] and left_hell[2][1] > left_hell[1][1]) or\
			 (left_hell[0][1] < left_hell[1][1] and left_hell[2][1] < left_hell[1][1]):
				left_hell = [left_hell[2],left_hell[0],left_hell[1]]
				#left_hell = deque(left_hell)
				left_indices = [1,0]
				#this created clockwise order from right, bottom and up
			else:
				left_hell = [left_hell[2],left_hell[1],left_hell[0]]
				#left_hell = deque(left_hell)
				left_indices = [2,0]
		else:	#exactly 2 points
			#left_hell = deque(left_hell)
			left_hell = [left_hell[1],left_hell[0]]
			left_indices = [1,0]
	if num_of_right_points < 4:
		if num_of_right_points > 2:	# here must be different num for same clockwise
			if right_hell[1][1] > right_hell[2][1]:
				right_hell = [right_hell[0],right_hell[1],right_hell[2]]
				#right_hell = deque(right_hell)
				right_indices = [0,2]
			else:
				right_hell = [right_hell[0],right_hell[2],right_hell[1]]
				#right_hell = deque(right_hell)
				right_indices = [0,1]
		else:
			#right_hell = deque(right_hell)
			right_indices = [0,1]
	#now the arrays are ordered clockwise form the middle line and dequed
	i = 0	# the most right point on X in left hell
	j = 0	#the most left point on X in right hell
	'''
	result1 = get_y_intersection(left_hell[i],right_hell[(j+1)%num_of_right_points], x_of_line)
	result2 = get_y_intersection(left_hell[i],right_hell[j], x_of_line)
	result3 = get_y_intersection(left_hell[(i-1)%num_of_left_points],right_hell[j], x_of_line)
	result4 = get_y_intersection(left_hell[i],right_hell[j], x_of_line)
	print(result1, " > ", result2)
	print(result3," > ", result4)
	'''
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
	#print("upper tangent ", upper_tangent)
	#here starts get lower tangent
	i = 0	# reset the most right point on X
	j = 0	# reset the most left point on X

	result5 = get_y_intersection(left_hell[i],right_hell[(j-1)%num_of_right_points], x_of_line)
	result6 = get_y_intersection(left_hell[i],right_hell[j], x_of_line)
	result7 = get_y_intersection(left_hell[(i+1)%num_of_left_points],right_hell[j], x_of_line)
	result8 = get_y_intersection(left_hell[i],right_hell[j], x_of_line)
	print(result5, " < ", result6)
	print(result7," < ", result8)

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
			# mod is there because after iterate to the last point in array
			# we want to return to the 0 index, so the last point is connected with the first

	lower_tangent = [i,j]	#array of two indices which represent points coords.
	#print("lower_tangent ", lower_tangent)
	tangents = [upper_tangent,lower_tangent]
	indices = [left_indices[0], right_indices[1]]	# send further left, right points
	result = [left_hell,right_hell,tangents,indices]
	return result

def merge_convex_hells(left_convex, right_convex, tangents, indices):
	upper_tangent = tangents[0]	#extract upper tangent
	lower_tangent = tangents[1]	#extract lower tangent
	num_of_left_points = len(left_convex)
	num_of_right_points = len(right_convex)
	print("upper_tangent ", upper_tangent)
	print("lower_tangent ", lower_tangent)
	#start with upper_tangent
	print("left_convex ", left_convex)
	print("right_convex ", right_convex)
	new_convex = [left_convex[upper_tangent[0]],right_convex[upper_tangent[1]]]

	next_point = (upper_tangent[1]+1)%num_of_right_points
	while next_point != lower_tangent[1]:
		new_convex.append(right_convex[next_point])
		next_point = (next_point + 1)%num_of_right_points
	#then append the right lower bound
	new_convex.append(right_convex[next_point])
	next_point = lower_tangent[0]
	while next_point != upper_tangent[0]:
		new_convex.append(left_convex[next_point])
		next_point = (next_point + 1)%num_of_left_points

	new_convex.append(indices)
	return new_convex	#this is new convex hell without inner points




def make_convex_hell(array):
	#array comes already sorted based on X coordinates
	try:
		if len(array) < 4:
			most_left = 0	#initialize with some index, cannot be 0
			most_right = len(array)-1	#initialize with some index, cannot be 0
			indices = [most_left, most_right]
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

try:
	#generate random, but uniq points no x and y coordinates are same
	uniq_points = gen_rand_uniq_points(10,10,6)
	#sort based on x coordinate
	#uniq_points = [[4, 1], [0, 9], [3, 3], [6, 4], [7, 8], [8, 5]]
	uniq_points = sorted(uniq_points, key=itemgetter(0))
	convex_hell = make_convex_hell(uniq_points)
	indices = convex_hell.pop()
	print("indices at the end ", indices)
	print ("convex_hell ", convex_hell)


except KeyboardInterrupt:
	print ("  Quit")
