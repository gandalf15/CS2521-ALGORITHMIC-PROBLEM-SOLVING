def sort_pancakes(pancake_stack)
	big_pancake = pancake_stack.max
	small_pancake = pancake_stack.min
	height = pancake_stack.length
	compare_array = pancake_stack.sort.reverse
	log = ""
	counter = 0
	while compare_array != pancake_stack
		index_of_max = pancake_stack.index(pancake_stack[counter,height].max)
		if index_of_max == height-1
			reverse_array = pancake_stack[counter,height]
			buffer_array = []
			if counter != 0
				buffer_array = pancake_stack[0,counter]
			end
			reverse_array.reverse!
			pancake_stack = buffer_array+reverse_array
			counter += 1
			log << (counter).to_s + " "
		else
			reverse_array = pancake_stack[index_of_max,height]
			buffer_array = pancake_stack[0,index_of_max]
			reverse_array.reverse!
			pancake_stack = buffer_array+reverse_array
			log << (index_of_max+1).to_s + " "
		end
	end
	return log.to_s + "0\n"
end

for pancake_stack in STDIN.read.split("\n")
	unless pancake_stack == "0"
		array_of_pancakes = pancake_stack.split(" ")
		num_array = []
		array_of_pancakes.each {|n| num_array << n.to_i}
		print pancake_stack + "\n" + sort_pancakes(num_array)
	else
		print "0\n"
	end
end