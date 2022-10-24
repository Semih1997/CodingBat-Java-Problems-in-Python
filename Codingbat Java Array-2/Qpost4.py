def post4(a):
    last_4 = 0
    for i in range(len(a)):
        if a[i] == 4:
            last_4 = i
    a = a[last_4 + 1:]
    return a
test_inputs = [[2, 4, 1, 2],[4, 1, 4, 2],[4, 4, 1, 2, 3],[4, 4]]
expected = [[1, 2],[2],[1, 2, 3],[]]
all_correct = True
for i in range(len(expected)):
    if post4(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)