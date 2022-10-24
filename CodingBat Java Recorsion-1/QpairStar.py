def pairStar(a):
    if len(a) <= 1:
        return a
    elif a[0] == a[1]:
        return a[0] + "*" + pairStar(a[1:])
    else:
        return a[0] + pairStar(a[1:])
test_inputs = ["hello","xxyy","aaaa","aaab","aa",""]
expected = ["hel*lo","x*xy*y","a*a*a*a","a*a*ab","a*a",""]
all_correct = True
for i in range(len(expected)):
    if pairStar(test_inputs[i]) != expected[i]:
        print(test_inputs[i],pairStar(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)