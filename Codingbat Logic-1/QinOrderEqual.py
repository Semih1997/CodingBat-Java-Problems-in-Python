def inOrderEqual(a,b,c,d):
    control = False
    if d == True:
        if a <= b and b <= c:
            control = True
    if a < b < c:
        control = True
    return control
test_inputs = [2,5,5,5,2,3,3,3,3,1,5]
other_test_inputs = [5,7,5,5,5,4,4,4,4,5,5]
other_test_inputs_1 = [11,6,7,7,4,3,4,3,4,5,5]
other_test_inputs_2 = [False,False,True,False,False,False,False,True,True,True,True]
expected = [True,False,True,False,False,False,False,False,True,True,True]
all_correct = True
for i in range(len(expected)):
    if inOrderEqual(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i],other_test_inputs_2[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)