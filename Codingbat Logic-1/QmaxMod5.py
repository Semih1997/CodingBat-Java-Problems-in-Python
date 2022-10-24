def maxMod5(a,b):
    large_num = (a < b) * b + (b < a) * a
    if a % 5 == b % 5:
        large_num =(a < b) * a + (b < a) * b
    if a == b :
        large_num = 0
    return large_num
test_inputs = [2,6,3,8,7,11,2,7,9,9,1]
other_test_inputs = [3,2,2,12,12,6,7,7,1,14,2]
expected = [3,6,3,12,7,6,2,0,9,9,2]
all_correct = True
for i in range(len(expected)):
    if maxMod5(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)