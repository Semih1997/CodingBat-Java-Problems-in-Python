def xyBalance(a):
    correction = True
    if "x" in a:
        for x in range(len(a)):
            if a[x] == "x" and not("y" in a[x:]):
                correction = False
    return correction
test_inputs = ["aaxbby","aaxbb","yaaxbb","yaaxbby","xaxxbby","xaxxbbyx","xxbxy","xxbx","bbb","bxbb","bxyb","xy","y","x","","yxyxyxyx","yxyxyxyxy","12xabxxydxyxyzz"] #18
expected = [True,False,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,True]
all_correct = True
for i in range(len(expected)):
    if xyBalance(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
print(len(test_inputs),len(expected))