def notString(a):
    if a[:3] == "not":
        return a
    else:
        a = str(a)
        a = "not " + a
        return a
test_inputs = [("candy"),("x"),("not bad"),("bad"),("not"),("is not"),("no")]
expected = [("not candy"),("not x"),("not bad"),("not bad"),("not"),("not is not"),("not no")]
all_correct = True
for i in range(len(expected)):
    if notString(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)