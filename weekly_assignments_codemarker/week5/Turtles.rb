input_ary = STDIN.read.split("\n")
number_of_tests = input_ary[0].to_i
number_of_done = 0
i=1
output_ary = []
while number_of_done != number_of_tests
	num_of_turtles = input_ary[i].to_i
	turtles_now = input_ary[i+1..i+num_of_turtles]
	turtles_wanted = input_ary[i+1+num_of_turtles..i+2*num_of_turtles]
	index_now = index_wanted = turtles_now.length-1.to_i
	num_from_top = 0.to_i
	while index_now >= 0
		if turtles_now[index_now] == turtles_wanted[index_wanted] then
			index_now -= 1
			index_wanted -= 1
		else
			index_now -= 1
			num_from_top += 1
		end
	end
	i = i+2*num_of_turtles+1
	number_of_done += 1
	output_array = turtles_wanted[0,num_from_top].reverse
	output_array.each{|name| print name+"\n"}
	print "\n"
end