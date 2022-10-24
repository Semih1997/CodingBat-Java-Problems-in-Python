def doubleChar(a):
    last_string = ""
    for x in a:
        last_string += x * 2
    return last_string
test_inputs = ["The","AAbb","Hi-There","Word!","!!","","a",".","aa"]
expected = ["TThhee", "AAAAbbbb","HHii--TThheerree","WWoorrdd!!","!!!!","","aa", "..","aaaa"]
all_correct = True
for i in range(len(expected)):
    if doubleChar(test_inputs[i]) != expected[i]:
        print(test_inputs[i],doubleChar(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)