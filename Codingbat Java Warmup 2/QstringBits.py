def stringBits(a):
    a = a[::2]
    return a
test_inputs = ["Hello","Hi","Heeololeo","HiHiHi","","Greetings","Chocoate","pi","Hello Kitten","hxaxpxpxy"]
expected = ["Hlo","H","Hello","HHH","","Getns","Coot","p","HloKte","happy"]
all_correct = True
for i in range(len(expected)):
    if stringBits(test_inputs[i]) != expected[i]:
        print(stringBits(test_inputs[i]))
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
    