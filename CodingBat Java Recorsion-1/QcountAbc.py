def countAbc(a):
    if len(a) <= 2:
        return 0
    elif a[0] == "a" and a[1] == "b" and (a[2] == "c" or a[2] == "a"):
        return 1 + countAbc(a[1:])
    else:
        return countAbc(a[1:])
test_inputs = ["abc","abcxxabc","abaxxaba","ababc","abxbc","aaabc","hello","","ab","aba","aca","aaa"]
expected = [1,2,2,2,0,1,0,0,0,1,0,0]
all_correct = True
for i in range(len(expected)):
    if countAbc(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)