def greaterThan(num1, num2)
	if num1 + num2 > 9 then
		return 1
	else
		return 0
	end
end

def carry(num1_array, num2_array)
	carry_count = 0
	remainder = 0
	length_of_num1 = num1_array.length
	length_of_num2 = num2_array.length

	if length_of_num1 > length_of_num2 then
		while length_of_num2 > 0
			remainder = greaterThan((num1_array[length_of_num1-1]+remainder), num2_array[length_of_num2-1])
			if remainder == 1 then
				carry_count += 1
			end 
			length_of_num1 -= 1
			length_of_num2 -= 1
		end
	else
		while length_of_num1 > 0
			remainder = greaterThan((num1_array[length_of_num1-1]+remainder), num2_array[length_of_num2-1])
			if remainder == 1 then
				carry_count += 1
			end 
			length_of_num1 -= 1
			length_of_num2 -= 1
		end
	end		
	return carry_count		
end

#string = "123 456\n555 555\n123 594\n0 0"
output_array = []
for line in STDIN.read.split("\n") #string.split("\n")
	array = line.split(' ')
	if array[0] && array[1] != "0" then
		num1 = array[0]
		num1_array_s = num1.split('')
		num1_array_i = []
		num1_array_s.each{|a| num1_array_i << a.to_i}
		num2 = array[1]
		num2_array_s = num2.split('')
		num2_array_i = []
		num2_array_s.each{|a| num2_array_i << a.to_i}
		carry_count = carry(num1_array_i, num2_array_i)
		if carry_count == 1 then
			output_array << carry_count.to_s + " carry operation.\n"
		elsif carry_count > 1 then
			output_array << carry_count.to_s + " carry operations.\n"
		else 
			output_array << "No carry operation.\n"
		end

	else
		output_array.each {|a| print a}
	end
end 

