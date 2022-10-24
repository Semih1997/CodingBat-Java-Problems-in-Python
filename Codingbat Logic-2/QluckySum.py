def luckySum(a,b,c):
    summing = a + b + c
    if a == 13:
        summing = 0
    elif b == 13:
        summing = a
    elif c == 13:
        summing = a + b
    return summing
test_inputs = [1,1,1,1,6,13,13,13,9,8,7,3]
other_test_inputs = [2,2,13,13,5,2,2,13,4,13,2,3]
other_test_inputs_1 = [3,13,3,13,2,3,13,2,13,2,1,13]
expected = [6,3,1,1,13,0,0,0,13,8,10,6]
all_correct = True
for i in range(len(expected)):
    if luckySum(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)