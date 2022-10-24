def noTeenSum(a,b,c):
    no_teen_sum = a + b + c
    if a in range(13,15) or a in range(17,20):
            no_teen_sum -= a
    if b in range(13,15) or b in range(17,20):
            no_teen_sum -= b
    if c in range(13,15) or c in range(17,20):
            no_teen_sum -= c
    return no_teen_sum
test_inputs = [1,2,2,2,2,2,17,2,16,17,15,15,15,5,17,17]
other_test_inputs = [2,13,1,1,1,1,1,15,17,18,16,15,19,17,18,19]
other_test_inputs_1 = [3,1,14,15,16,17,2,2,18,19,1,19,16,18,16,18]
expected = [6,3,3,18,19,3,3,19,16,0,32,30,31,5,16,0]
all_correct = True
for i in range(len(expected)):
    if noTeenSum(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)