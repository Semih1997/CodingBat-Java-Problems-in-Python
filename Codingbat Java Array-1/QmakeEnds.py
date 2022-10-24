def makeEnds(a):
    if len(a) < 2:
        a = [a[0],a[0]]
    else:
        a = [a[0],a[len(a)-1]]
    return a
test_inputs = [[1, 2, 3],[1, 2, 3, 4],[7, 4, 6, 2],[1, 2, 2, 2, 2, 2, 2, 3],[7, 4],[7],[5, 2, 9],[2, 3, 4, 1]]
expected = [[1, 3],[1, 4], [7, 2],[1, 3],[7, 4],[7, 7],[5, 9],[2, 1]]
all_correct = True
for i in range(len(expected)):
    if makeEnds(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
    