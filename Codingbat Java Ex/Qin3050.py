def in3050(a,b):
    if (a in range(30,41) and b in range(30,41)) or (a in range(40,51) and b in range(40,51)):
        return True
    else:
        return False
test_inputs = [30,30,40,40,39,50,40,49,50,50,35,35]
other_test_inputs = [31,41,50,51,50,39,39,48,40,51,36,45]
expected = [True,False,True,False,False,False,True,True,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if in3050(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)