def changePi(a):
    if len(a) == 0:
        return a
    if a[len(a) - 2: len(a)] == "pi":
        return changePi(a[:len(a)-2]) + "3.14"
    else:
        return changePi(a[:len(a)-1]) + a[len(a)-1]
    
def changePi_2(a):
    if len(a) < 2:
        return a
    elif a[:2] == "pi":
        return "3.14" + changePi_2(a[2:])
    else:
        return a[:1] + changePi_2(a[1:])

test_inputs = ["pi","xpix","pipi","pip","hip","p","x","","pixx"]
expected = ["3.14","x3.14x","3.143.14","3.14p","hip","p","x","","3.14xx"]
all_correct = True
for i in range(len(expected)):
    if changePi_2(test_inputs[i]) != expected[i]:
        # print(test_inputs[i],changePi(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)