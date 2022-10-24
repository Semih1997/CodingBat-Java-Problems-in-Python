def answerCell(isMorning,isMom,isAsleep):
    open_phone = True
    if isMorning == True and isMom == False:
        open_phone = False
    if isAsleep == True:
        open_phone = False
    return open_phone
test_inputs = [False,False,True,True,False,True]
other_test_inputs = [False,False,False,True,True,True]
other_test_inputs_1 = [False,True,False,False,False,True]
expected = [True,False,False,True,True,False]
all_correct = True
for i in range(len(expected)):
    if answerCell(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)