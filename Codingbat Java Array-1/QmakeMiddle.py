def makeMiddle(a):
    a = a[len(a)//2-1:len(a)//2+1]
    return a
test_inputs = [[1, 2, 3, 4],[7, 1, 2, 3, 4, 9],[1, 2],[5, 2, 4, 7],[9, 0, 4, 3, 9, 1]]
expected = [[2, 3],[2, 3],[1, 2],[2, 4],[4, 3]]
all_correct = True
for i in range(len(expected)):
    if makeMiddle(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)