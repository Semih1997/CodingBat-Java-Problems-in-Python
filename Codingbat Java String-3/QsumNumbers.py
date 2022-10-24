def sumNumbers(a):
    summing = 0
    i = len(a) - 1
    numbers = 0
    tenx_num = 0
    list_numbers = []
    while i > -1:
        if a[i].isnumeric() == True:
            numbers += (int(a[i]) * (10 ** tenx_num))
            tenx_num += 1
            if i == 0:
                list_numbers.append(numbers)
                i -= 1
            else:    
                i -= 1
        else:
            list_numbers.append(numbers)
            numbers = 0
            tenx_num = 0
            i -= 1
    summing = sum(list_numbers)
    return summing
test_inputs = ["abc123xyz","aa11b33","7 11","Chocolate","5hoco1a1e","5$$1;;1!!","a1234bb11","","a22bbb3"]
expected = [123,44,18,0,7,7,1245,0,25]
all_correct = True
for i in range(len(expected)):
    if sumNumbers(test_inputs[i]) != expected[i]:
        print(test_inputs[i],sumNumbers(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)