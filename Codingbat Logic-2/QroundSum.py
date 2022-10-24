def roundSum(a,b,c):
    def rolling(x):
        number = x % 10
        if number < 5:
            x -= number
        else:
            x += 10 - number
        return x
    summing = rolling(a) + rolling(b) + rolling(c)
    return summing
test_inputs = [16,12,6,4,4,9,0,0,10,20,45,23,23,25,23,11,24,14,12]
other_test_inputs = [17,13,4,6,4,4,0,9,10,30,21,11,24,24,24,24,36,12,10]
other_test_inputs_1 = [18,14,4,5,6,4,1,0,19,40,30,26,25,25,29,36,32,26,24]
expected = [60,30,10,20,10,10,0,10,40,90,100,60,70,80,70,70,90,50,40]
all_correct = True
for i in range(len(expected)):
    if roundSum(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],roundSum(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]))
        all_correct = False
print("All Correct: ", all_correct)