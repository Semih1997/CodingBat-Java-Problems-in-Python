def count7(a):
    if a == 0:
        return 0
    if a % 10 == 7:
        return 1 + count7(a // 10)
    else:
        return count7(a // 10)
test_inputs = [717,7,123,77,7123,771237,7777777,7123456,99999,9997999]
expected = [2,1,0,2,1,3,7,1,0,1]
all_correct = True
for i in range(len(expected)):
    if count7(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)