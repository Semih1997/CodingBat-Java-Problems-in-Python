def startHi(a):
    if a[:2] == "hi":
        return True
    else :
        return False
test_inputs = ["hi there","hi","hello hi","he","h","","ho hi","hi ho"]
expected = [True,True,False,False,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if startHi(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)