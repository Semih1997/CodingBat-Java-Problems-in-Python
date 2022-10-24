def sortaSum(a,b):
    summing = a + b
    if summing < 20 and summing > 9:
        summing = 20
    return summing
test_inputs = [3,9,10,12,-3,4,4,14,14]
other_test_inputs = [4,4,11,-3,12,5,6,7,6]
expected = [7,20,21,9,9,9,20,21,20]
all_correct = True
for i in range(len(expected)):
    if sortaSum(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)