def lastTwo(a):
    if len(a) > 2:
        a = a[:len(a)-2] + a[len(a)-1] + a[len(a)-2]
    elif len(a) == 2:
        a = a[1] + a[0]
    else:
        a = a
    return a
test_inputs = ["coding","cat","ab","a",""]
expected = ["codign","cta","ba","a",""]
all_correct = True
for i in range(len(expected)):
    if lastTwo(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)