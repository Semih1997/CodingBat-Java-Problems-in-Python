def extraEnd(a):
    last_string = a[-2:] * 3
    return last_string
test_inputs = ["Hello","ab","Hi","Candy","Code"]
expected = [ "lololo","ababab","HiHiHi","dydydy","dedede"]
all_correct = True
for i in range(len(expected)):
    if extraEnd(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)