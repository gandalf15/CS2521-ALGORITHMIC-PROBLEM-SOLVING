require 'benchmark'
require 'matrix'
class Matrix
  def []=(i, j, x)
    @rows[i][j] = x
  end
end

def knapsack_optimal_2 (capacity, groups)
	value_matrix = Matrix.build(groups.length+1, capacity+1) {|row,col| 0}
	wanted_groups_matrix = Matrix.build(groups.length+1, capacity+1) {|row,col| 0}
	groups.unshift(0)
	groups_length = groups.length
	for i in 0..groups_length-1
		for j in 0..capacity
			if i == 0 then
				value_matrix[i,j] = 0
			else
				if j >= groups[i] then
					if value_matrix.[](i-1,j) >= groups[i]+value_matrix.[](i-1,j-groups[i]) then
						value_matrix[i,j] = value_matrix.[](i-1,j)
						wanted_groups_matrix[i,j] = 0
					else
						value_matrix[i,j] = groups[i]+value_matrix.[](i-1,j-groups[i])
						wanted_groups_matrix[i,j] = 1
					end

				else
					value_matrix[i,j] = value_matrix.[](i-1,j)
					wanted_groups_matrix[i,j] = 0
				end
			end
		end
		if value_matrix.[](i,j) == capacity then
			return knapsack_result_lookup(wanted_groups_matrix, groups)
		end
	end
	return knapsack_result_lookup(wanted_groups_matrix, groups)
end
#end of ideal solution - DP knapsack
# start of the ideal solution - DP knapsack - my own work
def double_matrix_rows(m, max_rows)
	num_of_rows = m.row_count
	num_of_columns = m.column_count
	m = m.to_a
	if num_of_rows*2 <= max_rows then
		num_of_rows.times{ m << [0]*num_of_columns}
	else 
		(max_rows-num_of_rows).times{ m << [0]*num_of_columns}
	end
	return m = Matrix.rows(m)	
end

def knapsack_result_lookup(wanted_groups_matrix,groups)
	chosen_groups_indexes = []
	i = wanted_groups_matrix.row_count-1
	j = wanted_groups_matrix.column_count-1
	while i > 0 do
		if wanted_groups_matrix.[](i,j) == 1 then
			chosen_groups_indexes << i-1
			j = j-groups[i]
			i -= 1
		else
			i -= 1
		end						
	end
	return chosen_groups_indexes << j
end

def knapsack_optimal (capacity, groups)
	value_matrix = Matrix.build(2, capacity+1) {|row,col| 0}
	wanted_groups_matrix = Matrix.build(2, capacity+1) {|row,col| 0}
	groups.unshift(0)
	groups_length = groups.length
	for i in 0..groups_length-1
		for j in 0..capacity
			if i == 0 then
				value_matrix[i,j] = 0
			else
				if j >= groups[i] then
					if value_matrix.[](i-1,j) >= groups[i]+value_matrix.[](i-1,j-groups[i]) then
						value_matrix[i,j] = value_matrix.[](i-1,j)
						wanted_groups_matrix[i,j] = 0
					else
						value_matrix[i,j] = groups[i]+value_matrix.[](i-1,j-groups[i])
						wanted_groups_matrix[i,j] = 1
					end

				else
					value_matrix[i,j] = value_matrix.[](i-1,j)
					wanted_groups_matrix[i,j] = 0
				end
			end
		end
		if value_matrix.[](i,j) == capacity then
			return knapsack_result_lookup(wanted_groups_matrix, groups)
		end
		no_of_rows = value_matrix.row_count
		if no_of_rows = i then
			value_matrix = double_matrix_rows(value_matrix, groups_length)
			wanted_groups_matrix = double_matrix_rows(wanted_groups_matrix, groups_length)
		end
	end
	return knapsack_result_lookup(wanted_groups_matrix, groups)
end
#end of ideal solution - DP knapsack
# merge sort
def merge_sort(array)
  if array.length <= 1
    return array
  else
    mid = (array.length/2).floor
    left = merge_sort(array[0..mid-1])
    right = merge_sort(array[mid..array.length])
    merge(left, right)
  end
end

def merge(left, right)
  if left.empty?
    return right
  elsif right.empty?
    return left
  elsif left[0] > right[0]
    [left[0]] + merge(left[1..left.length], right)
  else
    [right[0]] + merge(left, right[1..right.length])
  end
end
#start of counting sort for heuristic method in O(n) time
def counting_sort(array)
  array_max = array.max
  array_min = array.min
  markings = [0] * (array_max - array_min + 1)
  array.each do |a|
    markings[a - array_min] += 1
  end
  res = []
  markings.length.times do |i|
    markings[i].times do
      res << i + array_min;
    end
  end
  res
end
# start of function for generating rand numbers for groups
def gen_groups_ary(capacity, groups)
	r = Random.new
	ary_groups = []
	groups.times{
		 ary_groups << r.rand(1..capacity)
	}
	return ary_groups
end
# initialize value and generate random groups upto capacity
p "Write number of seats: "
capacity = gets.chomp.to_i
p "Write number of groups: "
no_of_groups = gets.chomp.to_i
groups = gen_groups_ary(capacity,no_of_groups)

# heuristic first come first serve
capacity_first_serve = capacity
seated_groups_first_serve = []
groups.each_with_index {|group, index| 
	if capacity_first_serve >= group then
		capacity_first_serve -= group
		seated_groups_first_serve << index
	end
}
p "Array of groups is: "
p groups
p "First come first serve heuristic - seated groups are: "
p seated_groups_first_serve
p "First come first serve heuristic - left capacity: " + capacity_first_serve.to_s
p "=================================================================================="
# heuristic solution with mergesort n log n
capacity_heur = capacity
seated_groups_heur = []
sorted_groups = merge_sort(groups)
sorted_groups.each {|group| 
	if capacity_heur >= group then
		capacity_heur -= group
		seated_groups_heur << groups.index(group)
	end
}
p "Sorted heuristic - seated groups are: "
p seated_groups_heur
p "Sorted heuristic - left capacity: " + capacity_heur.to_s
p "==================================================================================="
# heuristic solution with counting sort O(n)
capacity_counting = capacity
seated_groups_counting = []
sorted_groups_counting = counting_sort(groups)
sorted_groups.each {|group| 
	if capacity_counting >= group then
		capacity_counting -= group
		seated_groups_counting << groups.index(group)
	end
}
p "Counting Sorted heuristic - seated groups are: "
p seated_groups_heur
p "Counting Sorted heuristic - left capacity: " + capacity_counting.to_s
p "==================================================================================="
# optimal solution
optimal_result = knapsack_optimal(capacity,groups)
left_capacity_optimal = optimal_result.pop
p "Optimal solution - seated groups are: "
p optimal_result
p "Optimal solution - left capacity: " + left_capacity_optimal.to_s
p "==================================================================================="
p "Sorted heuristic left seats minus first come left seats: "+ (capacity_first_serve-capacity_heur).to_s + " seats."
p "Optimal solution is better than Sorted heuristic about: " + (capacity_heur-left_capacity_optimal).to_s + " seats."
p "Optimal solution is better than first come first serve about: " + (capacity_first_serve-left_capacity_optimal).to_s + " seats."

=begin
#benchmark
p "BENCHMARK OF OPTIMAL SOLUTION"
Benchmark.bmbm do |x|
  x.report("optimal solution with expanding matrix rows") { knapsack_optimal(capacity,groups) }
  x.report("optimal solution with preconstructed whole matrix")  { knapsack_optimal_2(capacity,groups)  }
end
=end