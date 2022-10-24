def loneTeen(a,b):
    if a in range(13,20) and b in range(13,20):
        return False
    if a in range(13,20) or b in range(13,20):
        return True
    else :
        return False
test_inputs = [13,21,13,14,20,16,16,16,13,13,6,99,99]
other_test_inputs = [99,19,13,20,15,17,9,18,19,20,18,13,99]
expected = [True,True,False,True,True,False,True,False,False,True,True,True,False]
all_correct = True
for i in range(len(expected)):
    if loneTeen(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)