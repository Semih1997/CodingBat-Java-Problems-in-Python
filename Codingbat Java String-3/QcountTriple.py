def countTriple(a):
    i = 0
    count_triple = 0
    while i < len(a)-2:
        if a[i] == a[i+1] == a[i+2]:
            count_triple += 1
            i += 1
        else:
            i += 1
    return count_triple
test_inputs = ["abcXXXabc","xxxabyyyycd","a","","XXXabc","XXXXabc","XXXXXabc","222abyyycdXXX","abYYYabXXXXXab","abYYXabXXYXXab"]
expected = [1,3,0,0,1,2,3,3,4,0]
all_correct = True
for i in range(len(expected)):
    if countTriple(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)