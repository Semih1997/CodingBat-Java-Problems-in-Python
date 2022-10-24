def evenlySpaced(a,b,c):
    equal_spaced = (abs(a-b) == abs(b-c) and a != c) or (abs(a-b) == abs(a-c) and b != c) or (abs(c-a) == abs(c-b) and a != b) or (a == b == c)
    return equal_spaced
test_inputs = [2,4,4,6,6,2,2,9,10,10,2,2,3,12]
other_test_inputs = [4,6,6,2,2,2,2,10,9,9,4,2,6,3]
other_test_inputs_1 = [6,2,3,4,8,2,3,11,11,9,4,4,12,6]
expected = [True,True,False,True,False,True,False,True,True,False,False,False,False,False]
all_correct = True
for i in range(len(expected)):
    if evenlySpaced(test_inputs[i],other_test_inputs[i],other_test_inputs_1[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)