def shiftLeft(a):
    last_list = []
    if len(a) > 1:
        for i in range(1,len(a)):
            last_list.append(a[i])
        last_list.append(a[0])
    else:
        last_list = a
    return last_list
test_inputs = [[6, 2, 5, 3],[1, 2],[1],[],[1, 1, 2, 2, 4],[1, 1, 1],[1, 2, 3]]
expected = [[2, 5, 3, 6],[2, 1],[1],[],[1, 2, 2, 4, 1],[1, 1, 1],[2, 3, 1]]
all_correct = True
for i in range(len(expected)):
    if shiftLeft(test_inputs[i]) != expected[i]:
        print(test_inputs[i],shiftLeft(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)