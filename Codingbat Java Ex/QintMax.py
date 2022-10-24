def intMax(a,b,c):
    if a < b:
        max = b
    else:
        max = a
    if c > max:
        max = c
    else:
        max = max
    return max
test_inputs = [1,1,3,9,3,3,8,-3,6,5,5]
other_test_inputs = [2,3,2,3,9,3,2,-1,2,6,2]
other_test_inputs1 = [3,2,1,3,3,9,3,-2,5,2,6]
expected = [3,3,3,9,9,9,8,-1,6,6,6]
all_correct = True
for i in range(len(expected)):
    if intMax(test_inputs[i],other_test_inputs[i],other_test_inputs1[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)