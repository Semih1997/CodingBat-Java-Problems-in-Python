def nTwice(a,b):
    a = a[:b] + a[len(a)-b:]
    return a
test_inputs = ["Hello","Chocolate","Chocolate","Chocolate","Hello","Code","Code"]
other_test_inputs = [2,3,1,0,4,4,2]
expected = ["Helo","Choate","Ce","","Hellello", "CodeCode","Code"]
all_correct = True
for i in range(len(expected)):
    if nTwice(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)