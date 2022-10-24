def notreplace(a):
    i = 0
    new_a = ""
    a += " "
    while i < len(a):
        if a[i:i+2] == "is" and (a[i-1].isalpha() == False and a[i+2].isalpha() == False):
            new_a += a[i:i+2] + " not"
            i += 2
        if i == len(a) -1:
            i += 1
        else:
            new_a += a[i]
            i += 1
    return new_a
test_inputs = ["is test","This is right","is-is","This is isabell","","is","isis","Dis is bliss is","is his","xis yis","AAAis is"]
expected = ["is not test","This is not right","is not-is not","This is not isabell","","is not","isis","Dis is not bliss is not","is not his","xis yis","AAAis is not"]
all_correct = True
for i in range(len(expected)):
    if notreplace(test_inputs[i]) != expected[i]:
        print(test_inputs[i],"--",notreplace(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)