def strCount(a,b):
    if len(a) < len(b):
        return 0
    elif a[:len(b)] == b:
        return 1 + strCount(a[len(b):],b)
    else:
        return strCount(a[1:],b)
test_inputs = ["catcowcat","catcowcat","catcowcat","iiiijj","aaabababab","aaabababab"]
other_test_inputs = ["cat","cow","dog","iii","ab","aa"]
expected = [2,1,0,1,4,1]
all_correct = True
for i in range(len(expected)):
    if strCount(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)