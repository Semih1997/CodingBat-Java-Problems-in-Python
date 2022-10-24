def altPairs(a):
    last_a = ""
    for x in range(len(a)):
        last_a += a[x*4:(x*4)+2]
    return last_a
test_inputs = ["kitten","Chocolate","CodingHorror","yak","ya","y","","ThisThatTheOther"]
expected = ["kien","Chole","Congrr","ya","ya","y","","ThThThth"]
all_correct = True
for i in range(len(expected)):
    if altPairs(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)