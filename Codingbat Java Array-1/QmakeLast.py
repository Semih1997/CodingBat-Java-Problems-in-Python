def makeLast(a):
    last_list = []
    for x in range(len(a)*2):
        last_list.append(0)
    last_list[len(last_list)-1] = a[len(a)-1]
    return last_list
test_inputs = [[4, 5, 6],[1, 2],[3],[0],[7, 7, 7],[3, 1, 4],[1, 2, 3, 4],[1, 2, 3, 0],[2, 4]]
expected = [[0, 0, 0, 0, 0, 6],[0, 0, 0, 2],[0, 3],[0, 0],[0, 0, 0, 0, 0, 7],[0, 0, 0, 0, 0, 4],[0, 0, 0, 0, 0, 0, 0, 4],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 4]]
all_correct = True
for i in range(len(expected)):
    if makeLast(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)