def canBalance(a):
    control_balance = False
    for i in range(len(a)):
        before_i_sum = 0
        after_i_sum = 0
        for x in range(len(a[:i])):
            before_i_sum += a[x]
        for j in range(len(a[i:])):
            after_i_sum += a[j+i]
        if before_i_sum == after_i_sum:
            control_balance = True
    return control_balance
test_inputs = [[1, 1, 1, 2, 1],[2, 1, 1, 2, 1],[10,10],[10, 0, 1, -1, 10],[1, 1, 1, 1, 4],[2, 1, 1, 1, 4],[2, 3, 4, 1, 2],[2, 3, 4, 1, 2],[1, 2, 3, 1, 0, 2, 3],[1, 2, 3, 1, 0, 1, 3],[1],[1, 1, 1, 2, 1]]
expected = [True,False,True,True,True,False,False,False,True,False,False,True]
all_correct = True
for i in range(len(expected)):
    if canBalance(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)