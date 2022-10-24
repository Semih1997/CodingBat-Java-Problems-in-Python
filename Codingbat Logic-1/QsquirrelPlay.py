def squirrelPlay(a,b):
    correction = False
    if b == False:
        if a >= 60 and a <= 90:
            correction = True
    if b == True:
        if a >= 60 and a <= 100:
            correction = True
    return correction
test_inputs = [70,95,95,90,90,50,50,100,100,105,59,59,60]
other_test_inputs = [False,False,True,False,True,False,True,False,True,True,False,True,False]
expected = [True,False,True,True,True,False,False,False,True,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if squirrelPlay(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)