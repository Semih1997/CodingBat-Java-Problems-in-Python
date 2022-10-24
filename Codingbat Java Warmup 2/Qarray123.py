def array123(a):
    if len(a) < 3:
        return False
    else:
        for x in range(len(a)-2):
            if a[x] == 1 and a[x+1] == 2 and a[x+2] == 3:
                return True
    return False
test_inputs = [[1, 1, 2, 3, 1],[1, 1, 2, 4, 1],[1, 1, 2, 1, 2, 3],[1, 1, 2, 1, 2, 1],[1, 2, 3, 1, 2, 3],[1, 2, 3],[1, 1, 1],[1,2],[1],[]]
expected = [True,False,True,False,True,True,False,False,False,False]
all_correct = True
for i in range(len(expected)):
    if array123(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)