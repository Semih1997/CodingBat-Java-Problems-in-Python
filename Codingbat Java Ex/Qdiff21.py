def diff21(n):
    difference = (21 - n)
    if difference < 0 :
        difference = (n - 21) * 2
    return difference
test_inputs = [19,10,21,22,25,30,0,1,2,-1,-2,50]
expected = [2,11,0,2,8,18,21,20,19,22,23,58]
all_correct = True
for i in range(len(expected)):
    if diff21(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)