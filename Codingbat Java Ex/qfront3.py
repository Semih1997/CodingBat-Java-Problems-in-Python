def front3(a):
    if len(a) >= 3:
        a = a[:3] * 3
    elif len(a) < 3:
        a = a[:len(a)] * 3
    elif len(a) == 0:
        a = a
    return a
test_inputs = ["Java","Chocolate","abc","abcXYZ","ab","a",""]
expected = ["JavJavJav","ChoChoCho","abcabcabc","abcabcabc","ababab","aaa",""]
all_correct = True
for i in range(len(expected)):
    if front3(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)