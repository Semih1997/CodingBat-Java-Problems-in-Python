def xyzMiddle(a):
    correction = False
    if (a[len(a)//2-1:len(a)//2+2] == "xyz"):
        correction = True
    if len(a[:len(a)//2]) > len(a[len(a)//2+1:]):
        a = a[:len(a)-1]
        if (a[len(a)//2-1:len(a)//2+2] == "xyz"):
            correction = True
    return correction
test_inputs = ["AAxyzBB","AxyzBB","AxyzBBB","AxyzBBBB","AAAxyzB","AAAxyzBB","AAAAxyzBB","AAAAAxyzBBB","1x345xyz12x4","xyzAxyzBBB","xyzAxyzBxyz","xyzxyzAxyzBxyzxyz","xyzxyzxyzBxyzxyz","xyzxyzAxyzxyzxyz","xyzxyzAxyzxyzxy","AxyzxyzBB","","x","xy","xyz","xyzz"]
expected = [True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True]
all_correct = True
for i in range(len(expected)):
    if xyzMiddle(test_inputs[i]) != expected[i]:
        print(test_inputs[i],len(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)