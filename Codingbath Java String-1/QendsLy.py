def endsLy(a):
    control = False
    if a[len(a)-2:] == "ly":
        control = True
    return control
test_inputs = ["oddly","y","oddy","oddl","olydd","ly","falsey","","evenly"]
expected = [True,False,False,False,False,True,False,False,True]
all_correct = True
for i in range(len(expected)):
    if endsLy(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)