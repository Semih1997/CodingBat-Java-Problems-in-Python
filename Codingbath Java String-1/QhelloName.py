def helloName(a):
    a = "Hello " + a + "!"
    return a
test_inputs = ["Bob","Alice","X","Dolly","Alpha","Omega","Goodbye","ho ho ho","xyz!","Hello"]
expected = ["Hello Bob!","Hello Alice!","Hello X!","Hello Dolly!","Hello Alpha!","Hello Omega!","Hello Goodbye!","Hello ho ho ho!","Hello xyz!!","Hello Hello!"]
all_correct = True
for i in range(len(expected)):
    if helloName(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)