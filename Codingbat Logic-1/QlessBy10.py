def lessBy10(a,b,c):
    conrtol = False
    if abs(a - b) >= 10 or abs(a - c) >= 10 or abs(b - c) >= 10:
        conrtol = True
    return conrtol
test_inputs = [1,1,11,10,-10,2,3,3,10,10,10,3,2,2]
other_test_inputs = [7,7,1,7,2,11,3,3,1,11,11,30,2,8]
other_test_inputs_1 = [11,10,7,1,2,11,30,3,11,1,2,3,-8,12]
expected = [True,False,True,False,True,False,True,False,True,True,False,True,True,True]
all_correct = True
for i in range(len(expected)):
    if lessBy10(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)