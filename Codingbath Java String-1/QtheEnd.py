def theEnd(a,b):
    if b:
        a = a[0]
    else:
        a = a[len(a)-1]
    return a
test_inputs = ["Hello","Hello","oh","oh","x","x","java","chocolate","1234","code"]
other_test_inputs = [True,False,True,False,True,False,True,False,True,False]
expected = ["H","o","o","h","x","x","j","e","1","e"]
all_correct = True
for i in range(len(expected)):
    if theEnd(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)