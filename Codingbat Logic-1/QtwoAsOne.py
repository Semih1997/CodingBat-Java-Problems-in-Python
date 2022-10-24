def twoAsOne(a,b,c):
    control = False
    if a + b + c - a == a or a + b + c - b == b or a + b + c - c ==c:
        control = True
    return control
test_inputs = [1,3,3,2,5,5,2,9,9,5,3,3]
other_test_inputs = [2,1,2,3,3,3,5,5,4,4,3,3]
other_test_inputs_1 = [3,2,2,1,-2,-3,3,5,5,9,0,2]
expected = [True,True,False,True,True,False,True,False,True,True,True,False]
all_correct = True
for i in range(len(expected)):
    if twoAsOne(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)