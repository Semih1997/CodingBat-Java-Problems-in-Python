def hasTeen(a,b,c):
    if (a in range(13,20)) or (b in range(13,20)) or (c in range(13,20)):
        return True
    else :
        return False
test_inputs = [13,20,20,1,19,12,12,12,14,4,11]
other_test_inputs = [20,19,10,20,20,20,9,18,2,2,22]
other_test_inputs1 = [10,10,13,12,12,19,20,20,20,20,22]
expected = []
all_correct = True
for i in range(len(expected)):
    if hasTeen(test_inputs[i],other_test_inputs[i],other_test_inputs1 = [i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)