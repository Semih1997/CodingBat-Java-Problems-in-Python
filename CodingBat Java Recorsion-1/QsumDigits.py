def sumDigits(a):
    if a == 0:
        return 0
    return (a % 10) + sumDigits(a // 10)
test_inputs = [126,49,12,10,1,0,730,1111,11111,11000100,235]
expected = [9,13,3,1,1,0,10,4,5,3,10]
all_correct = True
for i in range(len(expected)):
    if sumDigits(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)