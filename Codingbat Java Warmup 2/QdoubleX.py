def doubleX(a):
    second_x = a.find('x') + 1
    if second_x == len(a):
        return False
    if len(a) > 1:
        if a[second_x] == 'x':
            return True
        else:
            return False
    else:
        return False
test_inputs = ["axxbb","axaxax","xxxxx","xaxxx","aaaax","","abc","x","xx","xax","xaxx"]
expected = [True,False,True,False,False,False,False,False,True,False,False]
all_correct = True
for i in range(len(expected)):
    if doubleX(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)