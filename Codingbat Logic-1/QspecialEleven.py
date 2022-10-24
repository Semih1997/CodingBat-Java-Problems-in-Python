def specialEleven(a):
    control = False
    if a % 11 == 0 or (a-1) % 11 == 0:
        control = True
    return control
test_inputs = [22,23,24,21,11,12,10,9,8,0,1,2,121,122,123,46,49,52,54,55]
expected = [True,True,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if specialEleven(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)