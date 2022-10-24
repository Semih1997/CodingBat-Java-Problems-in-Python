def countHi(a):
    count_hi = 0
    for x in range(len(a)-1):
        if a[x:x+2] == "hi":
            count_hi += 1
    return count_hi
test_inputs = ["abc hi ho","ABChi hi","hihi","hiHIhi","","h","hi","Hi is no HI on ahI","hiho not HOHIhi"]
expected = [1,2,2,2,0,0,1,0,2]
all_correct = True
for i in range(len(expected)):
    if countHi(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)