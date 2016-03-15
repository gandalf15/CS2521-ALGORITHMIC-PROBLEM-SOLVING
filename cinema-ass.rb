require 'matrix'
class Matrix
  def []=(i, j, x)
    @rows[i][j] = x
  end
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
#start of heapify
def make_heap(array)
	for i in 0..array.length-1 
		child = i
		while child > 0
			parent = (child - 1) / 2
			if array[parent] < array[child] then
				array[parent], array[child] = array[child], array[parent]
				child = parent
			else
				break
			end
		end
	end
	return array
end

def heapify(array, index)
	larger = index
	left = 2*index+1
	right = 2*index+2
	if left > array.length-1 then 
		return array
	elsif array[left] > array[index] then
		larger = left
	elsif array[right] > array[index] then
		larger = right
	end
	if larger != index
		array[index], array[larger] = array[larger], array[index]
		heapify(array,larger)
	end
	return array
end

def seat_by_heur(heap, groups, capacity)
seated_groups_heap_heur = []
	for i in 0..groups.length-1
		max_group = heap.unshift
		heap.shift(heap.pop)
		heap = heapify(heap,0)
		if capacity >= max_group then
			capacity -= max_group
			seated_groups_heap_heur << groups.index(max_group)
		else
			seated_groups_heap_heur << capacity
			return seated_groups_heap_heur
		end
	end 
end
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
capacity_heur = capacity_origin = capacity_first_serve = gets.chomp.to_i
p "Write number of groups: "
no_of_groups = gets.chomp.to_i
seated_groups_heur = seated_groups_first_serve = []
rejected_groups_heur = rejected_groups_first_serve = []
groups = gen_groups_ary(capacity_origin,no_of_groups)
# heuristic first come first serve
groups.each_with_index {|group, index| 
	if capacity_first_serve >= group then
		capacity_first_serve -= group
		seated_groups_first_serve << index
	else
		rejected_groups_first_serve << index
	end
}
p "Array of groups is: "
p groups
p "First come first serve heuristic - seated groups are: "
p seated_groups_first_serve
p "First come first serve heuristic - left capacity: " + capacity_first_serve.to_s
p ""
# optimal solution
optimal_result = knapsack_optimal(capacity_origin,groups)
left_capacity_optimal = optimal_result.pop
p optimal_result
p "Optimal solution - left capacity: " + left_capacity_optimal.to_s
p ""
# heuristic solution with heapify n log n
sorted_groups = merge_sort(groups)
sorted_groups.each {|group| 
	if capacity_heur >= group then
		capacity_heur -= group
		seated_groups_first_serve << groups.index(group)
	else
		rejected_groups_first_serve << groups.index(group)
	end
}
p "Sorted heuristic - seated groups are: "
p seated_groups_heur
p "Sorted heuristic - left capacity: " + capacity_heur.to_s
p ""
p "Sorted heuristic is better than first come first serve about: "+ (capacity_first_serve-capacity_heur).to_s + " seats."
p "Optimal solution is better than Sorted heuristic about: " + (capacity_heur-left_capacity_optimal).to_s + " seats."
p "Optimal solution is better than first come first serve about: " + (capacity_first_serve-left_capacity_optimal).to_s + " seats."
