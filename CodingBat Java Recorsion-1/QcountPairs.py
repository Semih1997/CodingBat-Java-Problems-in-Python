def countPairs(a):
    if len(a) <= 2:
        return 0
    elif a[0] == a[2]:
        return 1 + countPairs(a[1:])
    else:
        return countPairs(a[1:])
test_inputs = ["axa","axax","axbx","hi","hihih","ihihhh","ihjxhh","","aaa"]
expected = [1,2,1,0,3,3,0,0,1]
all_correct = True
for i in range(len(expected)):
    if countPairs(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)