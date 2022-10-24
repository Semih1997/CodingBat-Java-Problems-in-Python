def make2(a,b):
    all_together = []
    for x in a:
        all_together.append(x)
    for y in b:
        all_together.append(y)
    return all_together[:2]
test_inputs = [[4, 5],[4],[],[1, 2],[3],[3],[3, 1, 4],[1],[1, 2, 3],[7, 8],[7],[5, 4]]
other_test_inputs = [[1, 2, 3],[1, 2, 3],[1, 2],[],[1, 2, 3],[1],[],[1],[7, 8],[1, 2, 3],[1, 2, 3],[2, 3, 7]]
expected = [[4, 5],[4, 1],[1, 2],[1, 2],[3, 1],[3, 1],[3, 1],[1,1],[1, 2],[7, 8],[7, 1],[5, 4]]
all_correct = True
for i in range(len(expected)):
    if make2(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(make2(test_inputs[i],other_test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)