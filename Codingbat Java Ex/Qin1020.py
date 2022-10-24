def in1020(a,b):
    if a in range(10,21) or b in range(10,21):
        return True
    else:
        return False
test_inputs = [12,21,8,99,20,21,9]
other_test_inputs = [99,12,99,10,20,21,9]
expected = [True,True,False,True,True,False,False]
all_correct = True
for i in range(len(expected)):
    if in1020(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)