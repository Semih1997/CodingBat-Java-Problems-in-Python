def firstLast6(a):
    if a[0] == 6 or a[len(a)-1] == 6:
        return True
    else:
        return False
test_inputs = [[1, 2, 6],[6, 1, 2, 3],[13, 6, 1, 2, 3],[13, 6, 1, 2, 6],[3, 2, 1],[3, 6, 1],[3, 6],[6],[3],[5,6],[5,5],[1, 2, 3, 4, 6],[1, 2, 3, 4]]
expected = [True,True,False,True,False,False,True,True,False,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if firstLast6(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)