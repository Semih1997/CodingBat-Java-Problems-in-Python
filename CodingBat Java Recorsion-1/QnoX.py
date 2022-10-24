def noX(a):
    if len(a) == 0:
        return a
    if a[len(a) - 1] == "x":
        return noX(a[:len(a) - 1]) + ""
    else:
        return noX(a[:len(a) - 1]) + a[len(a) - 1]
test_inputs = ["xaxb","abc","xx","axxbxx","","Hellox"]
expected = ["ab","abc","","ab","","Hello"]
all_correct = True
for i in range(len(expected)):
    if noX(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)