def mirrorEnds(a):
    i = 0
    new_a = ""
    while i < len(a):
        if a[i] == a[-i-1] and (a[i].isalpha() or a[i].isnumeric())== True:
            new_a += a[i]
            i += 1
        else:
            break
    return new_a
test_inputs = ["abXYZba","abca","aba","abab","xxx","xxYxx","Hi and iH","x","","123and then 321","band andab"]
expected = ["ab","a","aba","","xxx","xxYxx","Hi","x","","123","ba"]
all_correct = True
for i in range(len(expected)):
    if mirrorEnds(test_inputs[i]) != expected[i]:
        print(test_inputs[i],mirrorEnds(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)