def bigDiff(a):
    a.sort()
    big_diff = a[len(a)-1] - a[0]
    return big_diff
test_inputs = [[10, 3, 5, 6],[7, 2, 10, 9],[2, 10, 7, 2],[2, 10],[10, 2],[10, 0],[2, 3],[2, 2],[2],[5, 1, 6, 1, 9, 9],[7, 6, 8, 5],[7, 7, 6, 8, 5, 5, 6]]
expected = [7,8,8,8,8,10,1,0,0,8,3,3]
all_correct = True
for i in range(len(expected)):
    if bigDiff(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)