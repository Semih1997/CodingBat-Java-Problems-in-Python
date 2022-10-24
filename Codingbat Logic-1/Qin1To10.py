def in1To10(a,b):
    control = False
    if b == True:
        if a <= 1 or a >= 10:
            control = True
    else:
        if a > 0 and a < 11:
            control = True
    return control
test_inputs = [5,11,11,10,10,9,9,1,1,0,0,-1,-1,99,-99] #15
other_test_inputs = [False,False,True,False,True,False,True,False,True,False,True,False,True,False,True] #15
expected = [True,False,True,True,True,True,False,True,True,False,True,False,True,False,True] #15
all_correct = True
for i in range(len(expected)):
    if in1To10(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)