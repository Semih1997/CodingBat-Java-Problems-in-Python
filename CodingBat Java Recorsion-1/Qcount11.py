def count11(a):
    if len(a) <= 1:
        return 0
    elif a[0] == "1" and a[1] == "1":
        return 1 + count11(a[2:])
    else:
        return count11(a[1:])
test_inputs = ["11abc11","abc11x11x11","111","1111","1","","hi","11x111x1111","1x111","1Hello1","Hello"]
expected = [2,3,1,2,0,0,0,4,1,0,0]
all_correct = True
for i in range(len(expected)):
    if count11(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)