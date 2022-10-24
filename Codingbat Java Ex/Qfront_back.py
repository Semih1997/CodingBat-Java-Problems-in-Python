def front_back(a):
    if len(a) > 1:
        a = str(a)
        a = a[len(a)-1] + a[1:len(a)- 1] + a[0]
    else :
        a = a
    return a
test_inputs = ["code","a","ab","abc","","Chocolate","aavJ","hello"]
expected = ["eodc","a","ba","cba","","ehocolatC","Java","oellh"]
all_correct = True
for i in range(len(expected)):
    if front_back(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)