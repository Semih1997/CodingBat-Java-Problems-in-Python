def withoutDoubles(a,b,c):
    resulting = a + b
    if c == True and a == b:
        resulting += 1
        if resulting == 13:
            resulting = 7
    return resulting
test_inputs = [2,3,3,2,5,5,5,5,6,6,1,6]
other_test_inputs = [3,3,3,3,4,4,5,5,6,6,6,1]
other_test_inputs_1 = [True,True,False,False,True,False,True,False,True,False,True,False]
expected = [5,7,6,5,9,9,11,10,7,12,7,7]
all_correct = True
for i in range(len(expected)):
    if withoutDoubles(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)