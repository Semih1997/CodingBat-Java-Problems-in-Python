def minCat(a,b):
    last_string = ""
    if len(a) == 0 or len(b) == 0:
        last_string = ""
    elif len(a) < len(b):
        last_string = a + b[-len(a):]
    elif len(b) < len(a):
        last_string = a[-len(b):] + b
    return last_string
test_inputs = ["Hello","Hello","java","abc","x","abc"]
other_test_inputs = ["Hi","java","Hello","x","abc",""]
expected = ["loHi","ellojava","javaello","cx","xc",""]
all_correct = True
for i in range(len(expected)):
    if minCat(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)