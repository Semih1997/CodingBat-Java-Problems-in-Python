def conCat(a,b):
    last_string = a + b
    if len(a) > 0 and len(b) > 0:
        if a[len(a)-1] == b[0]:
            last_string = a + b[1:]
    return last_string
test_inputs = ["abc","dog","abc","","pig","pig"]
other_test_inputs = ["cat","cat","","cat","g","doggy"]
expected = ["abcat","dogcat","abc","cat","pig","pigdoggy"]
all_correct = True
for i in range(len(expected)):
    if conCat(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)