def groupSum6(a,b,c):
    if a >= len(b):
        return (c == 0)
    elif groupSum6(a+1, b, c - b[a]):
        return True
    elif groupSum6(a+1, b, c) and b[a] != 6:
        return True
    else:
        return False
test_inputs = [0,0,0,0]
other_test_inputs = [[5, 6, 2],[5, 6, 2],[5, 6, 2],[1]]
other_test_inputs_1 = [8,9,7,1]
expected = [True,False,False,True]
all_correct = True
for i in range(len(expected)):
    if groupSum6(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)