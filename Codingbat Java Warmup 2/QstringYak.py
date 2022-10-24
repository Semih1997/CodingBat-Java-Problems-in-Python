def stringYak(a):
    a = a.replace("yak","")
    return a
test_inputs = ["yakpak","pak","yak123ya","yak","yakxxxyak","HiyakHi","xxxyakyyyakzzz"]
expected = ["pak","pak","123ya","","xxx","HiHi","xxxyyzzz"]
all_correct = True
for i in range(len(expected)):
    if stringYak(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
