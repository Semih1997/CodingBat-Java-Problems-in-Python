def makeOutWord(a,b):
    diveder = len(a)/2
    final_string = a[:2] + b + a[2:]
    return final_string
test_inputs = ["<<>>","<<>>","[[]]","HHoo","abyz"]
other_test_inputs = ["Yay","WooHoo","word","Hello","YAY"]
expected = ["<<Yay>>","<<WooHoo>>", "[[word]]","HHHellooo","abYAYyz"]
all_correct = True
for i in range(len(expected)):
    if makeOutWord(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)