def withoutX(a):
    if len(a) < 2:
        a = ""
    else:
        if a[0] == "x" :
            a = a[1:len(a)]
        if a[len(a)-1] == "x":
            a = a[:len(a)-1]
    return a
test_inputs = ["xHix","xHi","Hxix","Hi","xxHi","Hix","xaxbx","xx","x","","Hello","Hexllo"]
expected = ["Hi","Hi","Hxi","Hi","xHi","Hi","axb","","","","Hello","Hexllo"]
all_correct = True
for i in range(len(expected)):
    if withoutX(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(withoutX(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)