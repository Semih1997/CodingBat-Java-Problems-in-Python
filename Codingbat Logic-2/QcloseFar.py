def closeFar(a,b,c):
    correction = False
    if abs(a-b) <= 1 and abs(a-c) >= 2 and abs(b-c) >= 2: 
        correction = True
    elif abs(a-c) <= 1 and abs(b-c) >= 2 and abs(a-b) >= 2:
        correction = True
    return correction
test_inputs = [1,1,4,4,4,-1,0,10,10,8,8,8]
other_test_inputs = [2,2,1,5,3,10,-1,10,8,9,9,6]
other_test_inputs_1 = [10,3,3,3,5,0,10,8,9,10,7,9]
expected = [True,False,True,False,False,True,True,True,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if closeFar(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)