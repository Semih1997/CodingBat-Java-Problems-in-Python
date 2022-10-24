def nearTen(a):
    control = False
    if a % 10 in range(1,3) or a % 10 in range(8,10) or a % 10 == 0:
        control = True
    return control
test_inputs = [12,17,19,31,6,10,11,21,22,23,54,155,158,3,1]
expected = [True,False,True,True,False,True,True,True,True,False,False,False,True,False,True]
all_correct = True
for i in range(len(expected)):
    if nearTen(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)