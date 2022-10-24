def count8(a):
    if a == 0:
        return 0
    if a % 100 == 88:
        return 2 + count8(a // 10)
    elif a % 10 == 8:
        return 1 + count8(a // 10)
    else:
        return count8(a // 10)
test_inputs = [8,818,8818,8088,23884,88888]
expected = [1,2,4,4,3,9]
all_correct = True
for i in range(len(expected)):
    if count8(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)