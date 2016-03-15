require 'matrix'
class Matrix
  def []=(i, j, x)
    @rows[i][j] = x
  end
end

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
capacity_origin = capacity_first_serve = gets.chomp.to_i
p "Write number of groups: "
no_of_groups = gets.chomp.to_i
seated_groups_first_serve = []
rejected_groups_first_serve = []
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
seated_groups_first_serve.each {|i| p i}
p "First come first serve heuristic - rejected groups are:"
rejected_groups_first_serve.each{|i| p i}
p "First come first serve heuristic - left capacity: " + capacity_first_serve.to_s
# optimal solution
optimal_result = knapsack_optimal(capacity_origin,groups)
left_capacity_optimal = optimal_result.pop
p optimal_result
p "Optimal solution - left capacity: " + left_capacity_optimal.to_s
p "Optimal solution is better than first come first serve: " + (capacity_first_serve-left_capacity_optimal).to_s + " seats."