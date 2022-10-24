def bigHeights(a):
    return_num = 0
    name_list = [a[0][0],a[2][0]]
    number_list = [a[1],a[3]]
    sorted_name = [a[0][0],a[2][0]]
    sorted_number = [a[1],a[3]]
    sorted_name.sort()
    sorted_number.sort()
    if (sorted_name == name_list) and (sorted_number == number_list) and ((a[0] != a[2] and a[1] != a[3]) or (a[0] == a[2] and a[1] != a[3]) or (a[0] != a[2] and a[1] == a[3])):
        return_num = -1
    elif a[0] == a[2] and a[1] == a[3]:
        return_num = 0
    else:
        return_num = 1
    return return_num
test_inputs = [("bb", 1, "zz", 2),("bb", 1, "aa", 2),("bb", 1, "bb", 1),("bb", 5, "bb", 1),("bb", 5, "bb", 10),("adam", 1, "bob", 2),("bob", 1, "bob", 2)]
expected = [-1,1,0,1,-1,-1,-1]
all_correct = True
for i in range(len(expected)):
    if bigHeights(test_inputs[i]) != expected[i]:
        print(test_inputs[i],bigHeights(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)