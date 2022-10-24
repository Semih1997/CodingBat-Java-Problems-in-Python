def withoutX2(a):
    last_string = ""
    if len(a) < 2:
        return last_string
    elif len(a) >= 2:
        if "x" in a[:2]:
            last_string = a[:2].replace("x","",) + a[2:]
        else:
            last_string = a
    return last_string
test_inputs = ["xHi","Hxi","Hi","xxHi","Hix","xaxb","xx","x","","Hello","Hexllo","xHxllo"]
expected = ["Hi","Hi","Hi","Hi","Hix","axb","","","","Hello","Hexllo","Hxllo"]
all_correct = True
for i in range(len(expected)):
    if withoutX2(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(withoutX2(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)