def parenBit(a):
    if len(a) == 0:
        return a
    elif a[0] == "(":
        i = a.find(")")
        return a[0:i+1] + parenBit(a[1:])
    else:
        return parenBit(a[1:])
test_inputs = ["xyz(abc)123","x(hello)","(xy)1","()","res (ipsa) loquitor"]
expected = ["(abc)","(hello)","(xy)","()","(ipsa)"]
all_correct = True
for i in range(len(expected)):
    if parenBit(test_inputs[i]) != expected[i]:
        print(test_inputs[i],parenBit(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)