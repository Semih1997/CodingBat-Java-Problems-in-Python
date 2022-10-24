def frontAgain(a):
    control = False
    if len(a) > 1:
        if a[0] == a[len(a)-2] and a[1] == a[len(a)-1]:
            control = True
    return control
test_inputs = ["edited","edit","ed","jj","jjj","jjjj","jjjk","x","","java","javaja"]
expected = [True,False,True,True,True,True,False,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if frontAgain(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)