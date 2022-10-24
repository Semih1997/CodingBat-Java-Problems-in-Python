def or35(a):
    correction = False
    if a % 3 == 0 or a % 5 == 0:
        correction = True
    else :
        correction
    return correction
test_inputs = [3,10,8,15,5,9,4,7,6,17,21,20,22]
expected = [True,True,False,True,True,True,False,False,True,False,True,True,False]
all_correct = True
for i in range(len(expected)):
    if or35(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)