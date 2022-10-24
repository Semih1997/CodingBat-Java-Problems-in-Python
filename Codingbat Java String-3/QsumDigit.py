def sumDigit(a):
    sum_string = 0
    for i in range(len(a)):
        if a[i].isnumeric() == True:
            sum_string += int(a[i])
    return sum_string
test_inputs = ["aa1bc2d3","aa11b33","Chocolate","5hoco1a1e","123abc123","","5432a"]
expected = [6,8,0,7,12,0,14]
all_correct = True
for i in range(len(expected)):
    if sumDigit(test_inputs[i]) != expected[i]:
        print(test_inputs[i],sumDigit(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)