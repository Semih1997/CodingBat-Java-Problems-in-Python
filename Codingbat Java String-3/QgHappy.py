def gHappy(a):
    i = 0
    a += "/////"
    happy_control = True
    if len(a) == 1:
        happy_control = False
    if len(a) > 1:
        while i < len(a)-1:
            if a[i] == "g" and a[i+1] == "g" :
                happy_control = True
                i += 3
            if a[i] == "g" and a[i+1] != "g":
                happy_control = False
                i += 1
            else:
                i += 1
    return happy_control

test_inputs = ["xxggxx","xxgxx","xxggyygxx","g","gg","","xxgggxyz","xxgggxyg","xxgggxygg","mgm","mggm","yyygggxyy"]
expected = [True,False,False,False,True,True,True,False,True,False,True,True]
all_correct = True
for i in range(len(expected)):
    if gHappy(test_inputs[i]) != expected[i]:
        print(test_inputs[i],gHappy(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)