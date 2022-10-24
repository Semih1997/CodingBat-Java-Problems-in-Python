def lastDigit(a,b):
    if (a % 10) == (b % 10):
        return True
    else:
        return False
test_inputs = [7,6,3,114,114,10,11]
other_test_inputs = [17,17,113,113,4,0,0]
expected = [True,False,True,False,True,True,False]
all_correct = True
for i in range(len(expected)):
    if lastDigit(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)