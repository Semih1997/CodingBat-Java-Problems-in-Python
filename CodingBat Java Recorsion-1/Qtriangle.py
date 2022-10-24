def triangle(a):
    if a == 0:
        return 0
    return a + triangle(a-1)
test_inputs = [0,1,2,3,4,5,6,7]
expected = [0,1,3,6,10,15,21,28]
all_correct = True
for i in range(len(expected)):
    if triangle(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)