def modThree(a):
    count_odd = 0
    count_even = 0
    control_odd_even = False
    for i in range(len(a)):
        if a[i] % 2 == 1:
            count_odd += 1
            count_even = 0
            if count_odd == 3:
                control_odd_even = True
        if a[i] % 2 == 0:
            count_even += 1
            count_odd = 0
            if count_even == 3:
                control_odd_even = True
    return control_odd_even
test_inputs = [[2, 1, 3, 5],[2, 1, 2, 5],[2, 4, 2, 5],[1, 2, 1, 2, 1],[9, 9, 9],[1, 2, 1],[1, 2],[1],[],[9, 7, 2, 9],[9, 7, 2, 9, 2, 2],[9, 7, 2, 9, 2, 2, 6]]
expected = [True,False,True,False,True,False,False,False,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if modThree(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)