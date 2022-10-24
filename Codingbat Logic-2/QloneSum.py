def loneSum(a,b,c):
    summing = (int(a != b and a != c and c != b) * (a + b + c)) + (int(a == b) and (b != c) * c) + (int(a == c) and (c != b) * b) + (int(b == c) and (c != a) * a)
    return summing
test_inputs = [1,3,3,9,2,2,2,4,1]
other_test_inputs = [2,2,3,2,2,9,9,2,3]
other_test_inputs_1 = [3,3,3,2,9,2,3,3,1]
expected = [6,2,0,9,9,9,14,9,3]
all_correct = True
for i in range(len(expected)):
    if loneSum(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],loneSum(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]))
        all_correct = False
print("All Correct: ", all_correct)