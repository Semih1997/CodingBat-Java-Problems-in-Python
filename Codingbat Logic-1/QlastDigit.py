def lastDigit(a,b,c):
    control = False
    if a % 10 == b % 10 or a % 10 == c % 10 or b % 10 == c %10:
        control = True
    return control
test_inputs = [23,23,23,23,1,1,1,14,14,248,248,10,0] #13
other_test_inputs = [19,19,19,19,2,1,2,25,25,106,106,11,11] #13
other_test_inputs_1 = [13,12,3,39,3,2,2,43,45,1002,1008,20,0] #13
expected = [True,False,True,True,False,True,True,False,True,False,True,True,True] #13
all_correct = True
for i in range(len(expected)):
    if lastDigit(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)