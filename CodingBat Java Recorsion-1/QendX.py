def endX(a):
    if len(a) == 0:
        return a
    elif a[0] == "x":
        return endX(a[1:]) + "x"
    else:
        return a[0] + endX(a[1:])
test_inputs = ["xxre","xxhixx","xhixhix","hiy","x","","bxx"]
expected = ["rexx","hixxxx","hihixxx","hiy","x","","bxx"]
all_correct = True
for i in range(len(expected)):
    if endX(test_inputs[i]) != expected[i]:
        print(test_inputs[i],endX(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)