def withoutString(a,b):
    i = 0
    x = 0
    new_a = ""
    last_a = ""
    control_a = a.lower()
    control_b = b.lower()
    while i < len(a):
        if control_a[i:i+len(b)] != control_b:
            new_a += a[i]
            i += 1
        else:
            i += len(b)
    while x < len(new_a):
        if new_a[x] != " " or new_a[x+1] != " ":
            last_a += new_a[x]
            x += 1
        else:
            x += 1
    return last_a

test_inputs = ["Hello there","Hello there","Hello there","This is a FISH","This is a FISH","This is a FISH","abxxxxab","abxxxab","abxxxab","xxx","xxx","","1111"]
other_test_inputs = ["llo","e","x","IS","is","iS","xx","xx","x","x","xx","x","11"]
expected = ["He there","Hllo thr","Hello there","Th a FH","Th a FH","Th a FH","abab","abxab","abab","","x","",""]
all_correct = True
for i in range(len(expected)):
    if withoutString(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],withoutString(test_inputs[i],other_test_inputs[i]),i)
        all_correct = False
print("All Correct: ", all_correct)
print(len(expected),len(test_inputs),len(other_test_inputs))