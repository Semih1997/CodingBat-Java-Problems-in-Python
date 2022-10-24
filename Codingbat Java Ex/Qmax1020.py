def max1020(a,b):
    if a < b:
        if b in range(10,21):
            return b
        elif a in range(10,21):
            return a
        else:
            return 0
    else:
        if a in range(10,21):
            return a
        elif b in range(10,21):
            return b
        else:
            return 0
test_inputs = [11,19,11,9,10,21,9,23,20,7,17]
other_test_inputs =[19,11,9,21,21,10,11,10,10,20,16]
expected = [19,19,11,0,10,10,11,10,20,20,17]
all_correct = True
for i in range(len(expected)):
    if max1020(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)