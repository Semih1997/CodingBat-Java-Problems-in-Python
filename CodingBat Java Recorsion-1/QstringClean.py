def stringClean(a):
    if len(a) <= 1:
        return a
    elif a[0] == a[1]:
        return stringClean(a[1:])
    elif a[0] != a[1]:
        return a[0] + stringClean(a[1:])
test_inputs = ["yyzzza","abbbcdd","Hello","XXabcYY","112ab445","Hello Bookkeeper"]
expected = ["yza","abcd","Helo","XabcY","12ab45","Helo Bokeper"]
all_correct = True
for i in range(len(expected)):
    if stringClean(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)