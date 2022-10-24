def love6(a,b):
    control = False
    if a == 6 or b == 6:
        control = True
    elif a + b == 6:
        control = True
    elif abs(a-b) == 6: 
        control = True
    return control
test_inputs = [6,4,1,1,1,1,7,8,6,-6,-4,-7,7,-6,-2,7,0,8,3,3]
other_test_inputs = [4,5,5,6,8,7,5,2,6,2,-10,1,-1,12,-4,1,9,3,3,4]
expected = [True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False]
all_correct = True
for i in range(len(expected)):
    if love6(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i], i)
        all_correct = False
print("All Correct: ", all_correct)