def seeColor(a):
    last_a = ""
    if len(a) > 2:
        if a[0] == "r" and a[1] == "e" and a[2] == "d":
            last_a = "red"
    if len(a) > 3:
        if a[0] == "b" and a[1] == "l" and a[2] == "u" and a[3] == "e":
            last_a = "blue"
    return last_a
test_inputs = ["redxx","xxred","blueTimes","NoColor","red","re","blu","blue","a","","xyzred"]
expected = ["red","","blue","","red","","","blue","","",""]
all_correct = True
for i in range(len(expected)):
    if seeColor(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)