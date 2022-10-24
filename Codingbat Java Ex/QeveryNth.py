def everyNth(a,b):
    a = a[::b]
    return a
test_inputs = ["Miracle","abcdefg","abcdefg","Chocolate","Chocolates","Chocolates","Chocolates"]
other_test_inputs = [2,2,3,3,3,4,100]
expected = ["Mrce","aceg","adg","Cca","Ccas","Coe","C"]
all_correct = True
for i in range(len(expected)):
    if everyNth(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(everyNth(test_inputs[i],other_test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)