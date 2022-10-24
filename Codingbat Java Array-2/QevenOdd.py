def evenOdd(a):
    last_list = []
    for i in a:
        if i % 2 == 0:
            last_list.append(i)
    for i in a:
        if i % 2 == 1:
            last_list.append(i)
    return last_list
test_inputs = [[1, 0, 1, 0, 0, 1, 1],[3, 3, 2],[2, 2, 2],[3, 2, 2],[1, 1, 0, 1, 0],[1],[1, 2],[2, 1],[]]
expected = [[0, 0, 0, 1, 1, 1, 1],[2, 3, 3],[2, 2, 2],[2, 2, 3],[0, 0, 1, 1, 1],[1],[2, 1],[2, 1],[]]
all_correct = True
for i in range(len(expected)):
    if evenOdd(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)