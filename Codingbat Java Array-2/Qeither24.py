def either24(a):
    control_24 = 0
    true_false = True
    for i in range(len(a)-1):
        if (a[i] == 2 and a[i+1] == 2) or (a[i] == 4 and a[i+1] == 4):
            control_24 += 1
    if control_24 % 2 != 1:
        true_false = False
    return true_false
test_inputs = [[1, 2, 2],[4, 4, 1],[4, 4, 1, 2, 2],[1, 2, 3, 4],[3, 5, 9],[1, 2, 3, 4, 4],[2, 2, 3, 4],[1, 2, 3, 2, 2, 4],[1, 2, 3, 2, 2, 4, 4],[1, 2],[2, 2],[4, 4],[2],[]]
expected = [True,True,False,False,False,True,True,True,False,False,True,True,False,False]
all_correct = True
for i in range(len(expected)):
    if either24(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)