def changeXY(a):
    if len(a) == 0:
        return a
    if a[len(a) - 1] == "x":
        return changeXY(a[:len(a) - 1]) + "y"
    else:
        return changeXY(a[:len(a) - 1]) + a[len(a) - 1]
test_inputs = ["codex","xxhixx","xhixhix","hiy","h","x","","xxx","yyhxyi","hihi"]
expected = ["codey","yyhiyy","yhiyhiy","hiy","h","y","","yyy","yyhyyi","hihi"]
all_correct = True
for i in range(len(expected)):
    if changeXY(test_inputs[i]) != expected[i]:
        print(test_inputs[i],changeXY(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)