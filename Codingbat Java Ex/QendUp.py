def endUp(a):
    a = str(a)
    if len(a) > 3:
        last_3 = len(a) - 3
        last_3_string = a[last_3:len(a)]
        a = a[0:last_3] + last_3_string.upper()
        return a
    elif len(a) <= 3:
        a = a.upper()
        return a
test_inputs = ["Hello","hi there","woo hoo","xyz12","x",""]
expected = ["HeLLO","hi thERE","woo HOO","xyZ12","X",""]
all_correct = True
for i in range(len(expected)):
    if endUp(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
