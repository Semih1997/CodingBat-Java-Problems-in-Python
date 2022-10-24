def mixStart(a):
    if a[1:3] == "ix":
        return True
    else:
        return False
test_inputs = ["mix snacks","pix snacks","piz snacks","nix","ni","n",""]
expected = [True,True,False,True,False,False,False]
all_correct = True
for i in range(len(expected)):
    if mixStart(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)