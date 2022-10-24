def getSandwich(a):
    bread_list = []
    sandwich_type = ""
    if len(a) > 5 and "bread" in a:
        for x in range(len(a)):
            if a[x:x+5] == "bread":
                bread_list.append(x)
        sandwich_type = a[bread_list[0]+5:bread_list[len(bread_list)-1]]
    return sandwich_type
test_inputs = ["breadjambread","xxbreadjambreadyy","xxbreadyy","xxbreadbreadjambreadyy","breadAbread","breadbread","abcbreaz","xyz","","breadbreaxbread","breaxbreadybread","breadbreadbreadbread"]
expected = ["jam","jam","","breadjam","A","","","","","breax","y","breadbread"]
all_correct = True
for i in range(len(expected)):
    if getSandwich(test_inputs[i]) != expected[i]:
        print(test_inputs[i],getSandwich(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)