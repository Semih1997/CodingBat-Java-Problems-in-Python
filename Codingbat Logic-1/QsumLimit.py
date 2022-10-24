def sumLimit(a,b):
    summing = a + b
    if len(str(a)) < len(str(summing)):
        summing = a
    return summing
test_inputs = [2,8,8,11,11,0,99,99,123,1,23,23,9000,90000000,9000]
other_test_inputs = [3,3,1,39,99,0,0,1,1,123,60,80,1,1,1000]
expected = [5,8,9,50,11,0,99,99,124,1,83,23,9001,90000001,9000]
all_correct = True
for i in range(len(expected)):
    if sumLimit(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)