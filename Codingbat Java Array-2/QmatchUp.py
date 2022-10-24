def matchUp(a,b):
    count_match = 0
    for i in range(len(a)):
        if abs(a[i] - b[i]) <= 2 and abs(a[i] - b[i]) != 0:
            count_match += 1
    return count_match
test_inputs = [[1, 2, 3],[1, 2, 3],[1, 2, 3],[5, 3],[5, 3],[5, 3],[5, 3],[5, 3],[5, 3],[4],[4]]
other_test_inputs = [[2, 3, 10],[2, 3, 5],[2, 3, 3],[5, 5],[4, 4], [3, 3],[2, 2],[1, 1],[0, 0],[4],[5]]
expected = [2,3,2,1,2,1,1,1,0,0,1]
all_correct = True
for i in range(len(expected)):
    if matchUp(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)