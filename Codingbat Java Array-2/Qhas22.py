def has22(a):
    i = 0
    control2_2 = False
    for i in range(len(a)-1):
        if a[i] == 2 and a[i+1] == 2:
            control2_2 = True
    return control2_2
test_inputs = [[1, 2, 2],[1, 2, 1, 2],[2, 1, 2],[2, 2, 1, 2],[1, 3, 2],[1, 3, 2, 2],[2, 3, 2, 2],[4, 2, 4, 2, 2, 5],[2, 2],[],[3, 3, 2, 2],[5, 2, 5, 2]]
expected = [True,False,False,True,False,True,True,True,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if has22(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)