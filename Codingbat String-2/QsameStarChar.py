def sameStarChar(a):
    correction = True
    if len(a) > 1:
        for x in range(len(a)-1):
            if a[x] == "*" and (a[x-1] != a[x+1]) and (x != 0):
                correction = False
    return correction
test_inputs = ["xy*yzz","xy*zzz","*xa*az","*xa*bz","*xa*a*","","*xa*a*a","*xa*a*b","*12*2*2","12*2*3*","ABCdef","XY*YYYY*Z*","XY*YYYY*Y*","12*2*3*","*","**"]
expected = [True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True]
all_correct = True
for i in range(len(expected)):
    if sameStarChar(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)