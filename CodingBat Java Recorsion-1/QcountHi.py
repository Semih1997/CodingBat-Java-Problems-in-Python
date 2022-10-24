def countHi(a):
    x = len(a)
    if x == 0:
        return 0
    if a[x-2:] == "hi":
        return 1 + countHi(a[:x-1])
    else:
        return countHi(a[:x-1])
test_inputs = ["xxhixx","xhixhix","hi","hihih","h","","ihihihihih","ihihihihihi","hiAAhi12hi","xhixhxihihhhih","ship"]
expected = [1,2,1,2,0,0,4,5,3,3,1]
all_correct = True
for i in range(len(expected)):
    if countHi(test_inputs[i]) != expected[i]:
        print(test_inputs[i],countHi(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)