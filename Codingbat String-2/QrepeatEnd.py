def repeatEnd(a,b):
    a = a[len(a)-b:] * b
    return a
test_inputs = ["Hello","Hello","Hello","Hello","abc","1234","1234",""]
other_test_inputs = [3,2,1,0,3,2,3,0]
expected = ["llollollo","lolo", "o","","abcabcabc","3434","234234234",""]
all_correct = True
for i in range(len(expected)):
    if repeatEnd(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)