def tenRun(a):
    out_list = []
    divide_ten_control = False
    ten_times = 0
    for i in range(len(a)):
        if a[i] % 10 == 0:
            divide_ten_control = True
            ten_times = a[i]
        if divide_ten_control == False:
            out_list.append(a[i])
        else:
            out_list.append(ten_times)
    return out_list
test_inputs = [[2, 10, 3, 4, 20, 5],[10, 1, 20, 2],[10, 1, 9, 20],[1, 2, 50, 1],[1, 20, 50, 1],[10, 10],[10, 2],[0, 2],[1, 2],[1],[]]
expected = [[2, 10, 10, 10, 20, 20],[10, 10, 20, 20],[10, 10, 10, 20],[1, 2, 50, 50],[1, 20, 50, 50],[10, 10],[10, 10],[0, 0],[1, 2],[1],[]]
all_correct = True
for i in range(len(expected)):
    if tenRun(test_inputs[i]) != expected[i]:
        print(test_inputs[i],tenRun(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)