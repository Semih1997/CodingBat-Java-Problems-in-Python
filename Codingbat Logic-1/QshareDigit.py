def shareDigit(a,b):
    controller = False
    if a % 10 == b // 10 or a % 10 == b % 10 or a // 10 == b // 10 or a // 10 == b % 10 :
        controller = True
    return controller
test_inputs = [12,12,12,23,23,23,30,30,55,55]
other_test_inputs = [23,43,44,12,39,19,90,91,55,44]
expected = [True,False,False,True,True,False,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if shareDigit(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)