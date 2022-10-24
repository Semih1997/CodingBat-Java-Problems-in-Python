def cigarParty(a,b):
    control = False
    if b == False:
        if a <= 60 and 40 <= a:
            control = True
    if b == True:
        if a >= 40:
            control = True
    return control
test_inputs = [30,50,70,30,50,60,61,40,39,40,39]
other_test_inputs = [False,False,True,True,True,False,False,False,False,True,True]
expected = [False,True,True,False,True,True,False,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if cigarParty(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)