import random

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

def get_upper_tangent(points):
	i = 1
	j = 1
	while (y(i,j+1)>y(i,j) or y(i+1,j) > y(i,j)):
		if (y(i,j+1) > y(i,j)):		#move right
			j = (j+1)%q
		else:
			i = (i-1)%p				#move left
		pass
	return(ai,bj)


def get_lower_tangeent():
try:
	uniq_points = gen_rand_uniq_points(10,10,6)
	print (uniq_points)


except KeyboardInterrupt:
	print ("  Quit")
