def atFirst(a):
    if len(a) >= 2:
        a = a[:2]
    elif len(a) == 1:
        a = a + "@"
    else:
        a = "@@"
    return a
test_inputs = ["hello","hi","h","","kitten","java","j"]
expected = ["he","hi","h@","@@","ki","ja","j@"]
all_correct = True
for i in range(len(expected)):
    if atFirst(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)