def dateFashion(a,b):
    sit_control = 1
    if a >= 8 or b >= 8:
        sit_control = 2
    if a <= 2 or b <= 2:
        sit_control = 0
    return sit_control
test_inputs = [5,5,5,3,10,2,9,10,2,3,2,6]
other_test_inputs = [10,2,5,3,2,9,9,5,2,7,7,2]
expected = [2,0,1,1,0,0,2,2,0,1,0,0]
all_correct = True
for i in range(len(expected)):
    if dateFashion(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)