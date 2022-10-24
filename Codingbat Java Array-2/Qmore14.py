def more14(a):
    counter_1 = 0
    counter_4 = 0
    control14 = False
    for i in range(len(a)):
        if a[i] == 1:
            counter_1 += 1
        elif a[i] == 4:
            counter_4 += 1
    if counter_1 > counter_4:
        control14 = True
    return control14
test_inputs = [[1, 4, 1],[1, 4, 1, 4],[1, 1],[1, 6, 6],[1],[1, 4],[6, 1, 1],[1, 6, 4],[],[4, 1, 4, 6],[1, 4, 1, 4, 1, 6]]
expected = [True,False,True,True,True,False,True,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if more14(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)