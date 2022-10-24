def close10(a,b):
    if abs(a - 10) < abs(b - 10):
        return a
    if abs(a - 10) > abs(b - 10):
        return b 
    else:
        return 0
test_inputs = [8,13,13,7,9,13,10,11,5,0,10]
other_test_inputs = [13,8,7,13,13,8,12,10,21,20,10]
expected = [8,8,0,0,9,8,10,10,5,0,0]
all_correct = True
for i in range(len(expected)):
    if close10(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)