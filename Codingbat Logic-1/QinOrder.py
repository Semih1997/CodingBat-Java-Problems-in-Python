def inOrder(a,b,c,d):
    control = False
    if d == True:
        if b < c:
            control = True
    if a < b < c:
        control = True
    return control
test_inputs = [1,1,1,3,3,4,4]
other_test_inputs = [2,2,1,2,2,2,5]
other_test_inputs_1 = [4,1,2,4,4,2,2]
other_test_inputs_2 = [False,False,True,False,True,True,True]
expected = [True,False,True,False,True,False,False]
all_correct = True
for i in range(len(expected)):
    if inOrder(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i],other_test_inputs_2[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
