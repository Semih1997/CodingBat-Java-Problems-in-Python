def countX(a):
    x = len(a)
    if x == 0:
        return 0
    if a[x-1] == "x":
        return 1 + countX(a[:x-1])
    else :
        return countX(a[:x-1])
test_inputs = ["xxhixx","xhixhix","hi","x","","hiAAhi12hi"]
expected = [4,3,0,1,0,0]
all_correct = True
for i in range(len(expected)):
    if countX(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)