def startWord(a,b):
    last_string = ""
    if (len(a) or len(b))== 0:
        last_string = ""
    elif a[1:len(b)] == b[1:]:
        last_string = a[:len(b)]
    return last_string
test_inputs = ["hippo","hippo","hippo","hippo","h","","hip","hip","hip","h","hippo","hippo","hippo","kitten","kit"] #15
other_test_inputs = ["hi","xip","i","ix","ix","i","zi","zip","zig","z","xippo","xyz","hip","cit","cit"] #15
expected = ["hi","hip","h","","","","hi","hip","","h","hippo","","hip","kit","kit"] #15
all_correct = True
for i in range(len(expected)):
    if startWord(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        #print(startWord(test_inputs[i],other_test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)