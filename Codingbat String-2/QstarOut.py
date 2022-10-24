def starOut(a):
    last_string = a
    if len(a) <= 2 and "*" in a:
        last_string = ""
    elif len(a) > 2 and "*" in a:
        last_string = ""
        for x in range(len(a)-1):
            if a[x+1] != "*" and a[x] != "*" and a[x-1] != "*":
                last_string += a[x]
        if a[len(a)-1] != "*":
            last_string += a[len(a)-1]
        if a[len(a)-1] == "*":
            last_string = a[0] + last_string
    if len(a) == 3 and a[1] == "*":
        last_string = ""
    return last_string
test_inputs = ["ab*cd","ab**cd","sm*eilly","sm*eil*ly","sm**eil*ly","sm***eil*ly","stringy*","*stringy","*str*in*gy","abc","a*bc","ab","a*b","a*","*a"]
expected = ["ad","ad","silly","siy","siy","siy","string","tringy","ty","abc","c","ab","","",""]
all_correct = True
for i in range(len(expected)):
    if starOut(test_inputs[i]) != expected[i]:
        print(test_inputs[i],starOut(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)