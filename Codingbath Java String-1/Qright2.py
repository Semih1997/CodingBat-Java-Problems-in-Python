def right2(a):
    a = a[-2:] + a[:-2]
    return a
test_inputs = ["Hello","java","Hi","code","cat","12345"]
expected = ["loHel", "vaja","Hi","deco","atc", "45123"]
all_correct = True
for i in range(len(expected)):
    if right2(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)