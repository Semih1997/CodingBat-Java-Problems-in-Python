def groupSum(a,b,c):
    if a >= len(b):
        return (c == 0)
    elif groupSum(a+1,b,c - b[a]):
        return True
    elif groupSum(a+1,b,c):
        return True
    else:
        return False
test_inputs = [0,0,0,0,1,1,0,0,1,0,0,0,0,0,0]
other_test_inputs = [[2, 4, 8],[2, 4, 8],[2, 4, 8],[2, 4, 8],[2, 4, 8],[2, 4, 8],[1],[9],[9],[],[10, 2, 2, 5],[10, 2, 2, 5],[10, 2, 2, 5]]
other_test_inputs_1 = [10,14,9,8,8,2,1,1,0,0,17,15,9]
expected = [True,True,False,True,True,False,True,False,True,True,True,True,True]
all_correct = True
for i in range(len(expected)):
    if groupSum(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)