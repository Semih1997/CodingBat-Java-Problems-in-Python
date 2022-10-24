def startOz(a):
    if len(a) < 1:
        return ""
    if a[:2] == "oz":
        return "oz"
    elif a[0] == "o":
        return "o"
    elif a[1] == "z":
        return "z"
    else:
        return ""
test_inputs = ["ozymandias","bzoo","oxx","oz","ounce","o","abc","","zoo","aztec","zzzz","oznic"]
expected = ["oz","z","o","oz","o","o","","","","z","z","oz"]
all_correct = True
for i in range(len(expected)):
    if startOz(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)