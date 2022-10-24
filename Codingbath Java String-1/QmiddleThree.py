def middleThree(a):
    a = a[len(a)//2-1] + a[len(a)//2] + a[len(a)//2+1]
    return a
test_inputs = ["Candy","and","solving","Hi yet Hi","java yet java","Chocolate","XabcxyzabcX"]
expected = ["and","and","lvi","yet","yet","col","xyz"]
all_correct = True
for i in range(len(expected)):
    if middleThree(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)