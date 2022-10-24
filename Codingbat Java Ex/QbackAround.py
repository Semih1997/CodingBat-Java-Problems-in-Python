def backAround(a):
    a = str(a)
    a = a[len(a)-1] + a + a[len(a)-1]
    return a
test_inputs = ["cat","Hello","a","abc","read","boo"]
expected = ["tcatt","oHelloo","aaa","cabcc","dreadd","obooo"]
all_correct = True
for i in range(len(expected)):
    if backAround(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)