def more20(a):
    control = False
    if a % 20 == 1 or a % 20 == 2:
        control = True
    return control
test_inputs = [20,21,22,23,25,30,31,59,60,61,62,1020,1021,1000,1001] #15
expected = [False,True,True,False,False,False,False,False,False,True,True,False,True,False,True]
all_correct = True
for i in range(len(expected)):
    if more20(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)