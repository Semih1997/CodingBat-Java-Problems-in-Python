def sleepIn(weekday , vacation):
    if (not weekday) or vacation:
        return True
    else:
        return False

test_inputs = [(False, False),(True, False),(False, True),(True, True)]
expected = [(True),(False),(True),(True)]
all_correct = True
for i in range(len(expected)):
    if sleepIn(test_inputs[i],test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)