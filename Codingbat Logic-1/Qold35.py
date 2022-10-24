def old35(a):
    control = False
    if a % 3 == 0 or a % 5 == 0:
        control = True
    if a % 3 == 0 and a % 5 == 0:
        control = False
    return control
test_inputs = [3,10,15,5,9,8,7,6,17,18,29,20,21,22,45,99]
expected = [True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True]
all_correct = True
for i in range(len(expected)):
    if old35(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)