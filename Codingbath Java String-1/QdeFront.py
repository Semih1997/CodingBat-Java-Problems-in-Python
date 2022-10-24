def deFront(a):
    last_string = a[2:]
    if a[0:2] == "ab":
        last_string = a
    elif a[0] == "a":
        last_string = "a" + last_string
    elif a[1] == "b":
        last_string = "b" + last_string
    return last_string
test_inputs = ["Hello","java","away","axy","abc","xby","ab","ax","axb","aaa","xbc","bbb","bazz","ba","abxyz","hi","his","xz","zzz"]
expected = ["llo","va","aay","ay","abc","by","ab","a","ab","aa","bc","bb","zz","","abxyz","","s","","z"]
all_correct = True
for i in range(len(expected)):
    if deFront(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)