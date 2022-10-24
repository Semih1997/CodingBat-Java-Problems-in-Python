def makeTags(a,b):
    last_string = "<" + a + ">" + b + "</" + a + ">"
    return last_string
test_inputs = ["i","i","cite","address","body","i","i"]
other_test_inputs = ["Yay","Hello","Yay","here", "Heart","i",""]
expected = [ "<i>Yay</i>","<i>Hello</i>","<cite>Yay</cite>"]
all_correct = True
for i in range(len(expected)):
    if makeTags(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)