def stringE(a):
    count_e = str(a).count('e')
    if count_e >= 1 and count_e <= 3 :
        return True
    else:
        return False
test_inputs = ["Hello","Heelle","Heelele","Hll","e",""]
expected = [True,True,False,False,True,False]
all_correct = True
for i in range(len(expected)):
    if stringE(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)