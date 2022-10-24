def xyzThere(a):
    controlling = False
    for x in range(len(a) - 2):
        if a[x:x+3] == "xyz" and a[x-1] != ".":
            controlling = True        
    return controlling
test_inputs = ["abcxyz","abc.xyz","xyz.abc","abcxy","xyz","xy","x","","abc.xyzxyz","abc.xxyz",".xyz","12.xyz","12xyz","1.xyz.xyz2.xyz"]
expected = [True,False,True,False,True,False,False,False,True,True,False,False,True,False]
all_correct = True
for i in range(len(expected)):
    if xyzThere(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)