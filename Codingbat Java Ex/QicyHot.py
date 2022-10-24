def icyHot(a, b):
    if (a * b) < 0 and ((a > 100) or (b > 100)):
        return True
    else :
        return False
test_inputs = [120,-1,2,-1,-2,120]
other_test_inputs =[-1,120,120,100,-2,120]
expected = [True,True,False,False,False,False]
all_correct = True
for i in range(len(expected)):
    if icyHot(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)