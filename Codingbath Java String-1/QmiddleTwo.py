def middleTwo(a):
    a = a[len(a)//2-1:len(a)//2+1]
    print(a)
    return a
test_inputs = ["string","code","Practice","ab","0123456789"]
expected = ["ri","od","ct","ab","45"]
all_correct = True
for i in range(len(expected)):
    if middleTwo(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)