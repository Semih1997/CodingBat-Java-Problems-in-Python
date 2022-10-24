def missingChar(a,b):
    a = str(a)
    a = a[:b] + a[b+1:]
    return a