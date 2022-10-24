def seriesUp(a):
    last_list = []
    minus = a - 1
    for k in range(a):
        for i in range(a):
            if i <= k:
                last_list.append(a - minus + i)
    return last_list
test_inputs = [3,4,2]
expected = [[1, 1, 2, 1, 2, 3],[1, 1, 2, 1, 2, 3, 1, 2, 3, 4],[1, 1, 2]]
all_correct = True
for i in range(len(expected)):
    if seriesUp(test_inputs[i]) != expected[i]:
        print(test_inputs[i],seriesUp(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)