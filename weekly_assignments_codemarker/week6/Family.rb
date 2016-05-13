def median(array)
	array.sort!
	return array[array.size/2]
end
def measure_distance(array, median)
	distance = 0
	array.each{|num| if num < median then distance += median-num else distance += num-median end}
	return distance.to_s+"\n"
end
for line in STDIN.read.split("\n")
	ary_of_char = line.split(" ")
	ary_of_num = []
	ary_of_char.each{|n| ary_of_num << n.to_i }
	num_of_houses = ary_of_num.shift
	house = median(ary_of_num) unless ary_of_num.empty?
	print measure_distance(ary_of_num, house)  unless ary_of_num.empty?
end