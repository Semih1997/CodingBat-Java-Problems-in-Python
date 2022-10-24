def teenSum(a,b):
    summing = a + b
    if a in range(13,20) or b in range(13,20):
        summing = 19
    return summing
test_inputs = [3,10,13,3,13,10,6,15,19,19,2,12,2,2,2,6]
other_test_inputs = [4,13,2,19,13,10,14,2,19,20,18,4,20,17,16,7]
expected = [7,19,19,19,19,20,19,19,19,19,19,16,22,19,19,13]
all_correct = True
for i in range(len(expected)):
    if teenSum(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)