require 'benchmark'
require 'matrix'
class Matrix
  def []=(i, j, x)
    @rows[i][j] = x
  end
end
def first_come(capacity, groups)
	# heuristic first come first serve
	seated_groups = []
	groups.each_with_index {|group, index|
		if capacity >= group then
			capacity -= group
			seated_groups << index
		end
	}
	return seated_groups << capacity
end
def merge_sort_heur(capacity, groups)
	seated_groups = []
	sorted_groups = merge_sort(groups)
	sorted_groups.each {|group|
		if capacity >= group then
			capacity -= group
			seated_groups << groups.index(group)
		end
	}
	return seated_groups << capacity
end
def counting_heur(capacity,groups)
	seated_groups = []
	sorted_groups = counting_sort(groups)
	sorted_groups.each {|group|
		if capacity >= group then
			capacity -= group
			seated_groups << groups.index(group)
		end
	}
	return seated_groups << capacity
end
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
    markings[array_max - a] += 1
  end
  res = []
  markings.length.times do |i|
    markings[i].times do
      res << array_max - i;
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
p "=================================================================================="
p "Array of groups is: "
p "=================================================================================="
p groups
p "=================================================================================="
# first come solution
p "First come first serve heuristic - seated groups are: "
first_come_result = first_come(capacity,groups)
left_capacity_first = first_come_result.pop
p first_come_result
p "First come first serve heuristic - left capacity: " + left_capacity_first.to_s
p "=================================================================================="
# heuristic solution with mergesort n log n
merge_sort_result = merge_sort_heur(capacity,groups)
left_capacity_merge = merge_sort_result.pop
p "Merge Sorted heuristic - seated groups are: "
p merge_sort_result
p "Merge Sorted heuristic - left capacity: " + left_capacity_merge.to_s
p "==================================================================================="
# heuristic solution with counting sort O(n)
counting_sort_result = counting_heur(capacity,groups)
left_capacity_counting = counting_sort_result.pop
p "Counting Sorted heuristic - seated groups are: "
p counting_sort_result
p "Counting Sorted heuristic - left capacity: " + left_capacity_counting.to_s
p "==================================================================================="
# optimal solution
optimal_result = knapsack_optimal(capacity,groups)
left_capacity_optimal = optimal_result.pop
p "Optimal solution - seated groups are: "
p optimal_result
p "Optimal solution - left capacity: " + left_capacity_optimal.to_s
p "==================================================================================="
p "Sorted heuristic left seats minus first come left seats: "+ (left_capacity_first - left_capacity_merge).to_s + " seats."
p "Optimal solution is better than Sorted heuristic about: " + (left_capacity_merge - left_capacity_optimal).to_s + " seats."
p "Optimal solution is better than first come first serve about: " + (left_capacity_first-left_capacity_optimal).to_s + " seats."
# start benchmark
p "==================================================================================="
p "BENCHMARK FOR ALL ALGORITHMS"
Benchmark.bmbm do |x|
  x.report("mergesort") { merge_sort_heur(capacity,groups) }
  x.report("counting sort")  { counting_heur(capacity,groups)  }
  x.report("optimal solution with expanding matrix rows") { knapsack_optimal(capacity,groups) }
end
p "==================================================================================="
