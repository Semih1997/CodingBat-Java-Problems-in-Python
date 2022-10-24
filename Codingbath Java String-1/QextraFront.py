def extraFront(a):
    last_a = a * 3
    if len(a) > 1:
        last_a = a[:2] * 3
    return last_a
test_inputs = ["Hello","ab","H","","Candy","Code"]
expected = ["HeHeHe","ababab","HHH","","CaCaCa","CoCoCo"]
all_correct = True
for i in range(len(expected)):
    if extraFront(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)