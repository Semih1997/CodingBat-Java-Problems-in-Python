from sqlalchemy import false


def dividesSelf(a):
    digits_a = a
    a_digit_list = []
    divide_self = True
    while digits_a > 0:
        control = digits_a % 10
        a_digit_list.append(control)
        digits_a = digits_a // 10
    for i in range(len(a_digit_list)):
        if a_digit_list[i] == 0:
            divide_self = False
        elif a % a_digit_list[i] != 0:
            divide_self = False
    return divide_self
test_inputs = [128,12,120,122,13,32,22,42,212,213,162]
expected = [True,True,False,True,False,False,True,False,True,False,True]
all_correct = True
for i in range(len(expected)):
    if dividesSelf(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)