def oneTwo(a):
    last_string = ""
    if len(a) >= 3:
        for x in range(0,len(a)-2,3):
            last_string += a[x+1] + a[x+2] + a[x]
    return last_string
test_inputs = ["abc","tca","tcagdo","chocolate","1234567890","xabxabxabxabxabxabxab","abcdefghijklkmnopqrstuvwxyz1234567890","","x","xy","xyz","abcdefghijklkmnopqrstuvwxyz123456789"]
expected = ["bca","cat","catdog","hocolctea","231564897","abxabxabxabxabxabxabx","bcaefdhigkljmnkpqostrvwuyzx231564897","","","","yzx","bcaefdhigkljmnkpqostrvwuyzx231564897"]
all_correct = True
for i in range(len(expected)):
    if oneTwo(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)