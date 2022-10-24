def without2(a):
    last_string = a
    if len(a) == 2:
        last_string = ""
    elif len(a) > 2 and a[0:2] == a[len(a)-2:]:
        last_string = a[2:]
    return last_string
test_inputs = ["HelloHe","HelloHi","Hi","Chocolate","xxx","xx","x","","Fruits"]
expected = ["lloHe","HelloHi","","Chocolate","x","","x","","Fruits"]
all_correct = True
for i in range(len(expected)):
    if without2(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)