def powerN(a,b):
    if b == 0:
        return 1
    return a * powerN(a,b-1)
test_inputs = [3,3,3,2,10]
other_test_inputs = [2,1,3,5,3]
expected = [9,3,27,32,1000]
all_correct = True
for i in range(len(expected)):
    if powerN(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],powerN(test_inputs[i],other_test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)