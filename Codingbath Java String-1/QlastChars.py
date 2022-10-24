def lastChars(a,b):
    if len(a) < 1:
        last_a = "@"
    else:
        last_a = a[0]
    if len(b) < 1:
        last_b = "@"
    else:
        last_b = b[len(b)-1]
    last_string = last_a + last_b
    return last_string
test_inputs = ["last","yo","hi","","","kitten","k","kitten","kitten"]
other_test_inputs = ["chars","java","","hello","","hi","zip","","zip"]
expected = ["ls","ya","h@","@o","@@","ki","kp","k@","kp"]
all_correct = True
for i in range(len(expected)):
    if lastChars(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)