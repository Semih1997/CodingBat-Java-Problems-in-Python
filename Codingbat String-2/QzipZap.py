def zipZap(a):      
    a += "?" * (3-1)
    new_a = ""
    i = 0
    while i < len(a)-2:
        if a[i] == 'z' and a[i+2] == 'p':
            new_a += a[i] + a[i+2]
            i += 3
        else:
            new_a += a[i]
            i += 1
    return new_a
test_inputs = ["zipXzap","zopzop","zzzopzop","zibzap","zip","zi","z","","zzp","abcppp","azbcppp","azbcpzpp"]
expected = ["zpXzp","zpzp","zzzpzp","zibzp","zp","zi","z","","zp","abcppp","azbcppp","azbcpzp"]
all_correct = True
for i in range(len(expected)):
    if zipZap(test_inputs[i]) != expected[i]:
        print(test_inputs[i],zipZap(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)