def pre4(a):
    first_4 = a.index(4)
    if len(a) > 0 and 4 in a:
        a = a[:first_4]
    return a
test_inputs = [[1, 2, 4, 1],[3, 1, 4],[1, 4, 4],[1, 4, 4, 2],[1, 3, 4, 2, 4],[4, 4],[3, 3, 4],[1, 2, 1, 4],[2, 1, 4, 2],[2, 1, 2, 1, 4, 2]]
expected = [[1, 2],[3, 1],[1],[1],[1, 3],[],[3,3],[1, 2, 1],[2, 1],[2, 1, 2, 1]]
all_correct = True
for i in range(len(expected)):
    if pre4(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)