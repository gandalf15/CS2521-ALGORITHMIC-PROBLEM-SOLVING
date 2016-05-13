require 'thread'
array1 = STDIN.read.split("\n")
number_of_records = array1.shift
array2 = array1.slice!((number_of_records.to_i),array1.size)
t1 = Thread.new{array1.sort!}
array2.sort!
x = 0
output_value = ""
t1.join
for i in array1
    value = array2[x].split(" ")
    output_value << (i + " " + value[1] + "\n")
	x += 1
end
puts output_value