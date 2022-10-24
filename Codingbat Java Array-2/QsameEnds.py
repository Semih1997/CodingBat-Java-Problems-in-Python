def sameEnds(a,b):
    control_same_ends = False
    if b == 0:
        control_same_ends = True
    if a[:b] == a[-b:]:
        control_same_ends = True
    return control_same_ends
test_inputs = [[5, 6, 45, 99, 13, 5, 6],[5, 6, 45, 99, 13, 5, 6],[5, 6, 45, 99, 13, 5, 6],[1, 2, 5, 2, 1],[1, 2, 5, 2, 1],[1, 2, 5, 2, 1],[1, 2, 5, 2, 1],[1, 1, 1],[1, 1, 1],[1, 1, 1],[1, 1, 1],[],[4, 2, 4, 5]]
other_test_inputs = [1,2,3,1,2,0,5,0,1,2,3,0,1]
expected = [False,True,False,True,False,True,True,True,True,True,True,True,False]
all_correct = True
for i in range(len(expected)):
    if sameEnds(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)