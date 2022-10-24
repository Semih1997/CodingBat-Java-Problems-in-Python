def frontTimes(a,b):
    if len(a) > 3:
        a = a[:3] * b
    else:
        a = a * b
    return a
test_inputs = ["Chocolate","Chocolate","Abc","Ab","A","","Abc"]
other_test_inputs = [2,3,3,4,4,4,0]
expected = ["ChoCho","ChoChoCho","AbcAbcAbc","AbAbAbAb","AAAA","",""]
all_correct = True
for i in range(len(expected)):
    if frontTimes(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)