def less20(a):
    control = False
    if a % 20 == 18 or a % 20 == 19:
        control = True
    return control
test_inputs = [18,19,20,8,17,23,25,30,31,58,59,60,61,62,1017,1018]
expected = [True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if less20(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)