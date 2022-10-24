def hasBad(a):
    control = False
    for x in range(len(a)):
        if a[0] == "b" or a[1] == "b":
            if a[x:x+3] == "bad":
                control = True
    return control
test_inputs = ["badxx","xbadxx","xxbadxx","code","bad","ba","xba","xbad","","badyy"]
expected = [True,True,False,False,True,False,False,True,False,True]
all_correct = True
for i in range(len(expected)):
    if hasBad(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)