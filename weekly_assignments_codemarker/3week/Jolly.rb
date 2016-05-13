#string = "4 1 4 2 3\n5 1 4 2 -1 6\n0"


def isJolly(num_ary)
    first_num = num_ary.shift
    if num_ary.length == first_num then
        check_ary = []
        num_ary.each_with_index {|n, i|
            if i != first_num-1
                abs_value = (n-num_ary[i+1]).abs
                unless check_ary.include?(abs_value)
                
                   check_ary << abs_value
                   
                else

                    print "Not Jolly\n"
                    return
                end
            else
                print "Jolly\n"
                return
            end
        }
    else
        print "Not Jolly\n"
        return
    end
end


for i in STDIN.read.split("\n") #string.split("\n")
   string_ary = i.split(" ")
   num_ary = []
   string_ary.each {|s| num_ary << s.to_i}
    unless num_ary[0] == 0
       isJolly(num_ary)
    else
        exit
    end
end
