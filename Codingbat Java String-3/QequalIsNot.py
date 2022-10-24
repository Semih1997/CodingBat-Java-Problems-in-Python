def equalIsNot(a):
    i = 0
    control = False
    count_is = 0
    count_not = 0
    while i < len(a):
        if a[i:i+2] == "is":
            count_is += 1
            i += 1
        if a[i:i+3] == "not":
            count_not += 1
            i += 1
        else:
            i += 1
    if count_not == count_is:
        control = True
    return control
test_inputs = ["This is not","This is notnot","noisxxnotyynotxisi","noisxxnotyynotxsi","xxxyyyzzzintint","","isisnotnot","isisnotno7Not","isnotis","mis3notpotbotis"]
expected = [False,True,True,False,True,True,True,False,False,False]
all_correct = True
for i in range(len(expected)):
    if equalIsNot(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)