def posNeg(a, b, negative):
    negcorrection = False
    if negative == True:
        if (a < 0) and (b < 0):
            negcorrection = True
        else:
            negcorrection
    else:
        if (a * b <0):
            negcorrection = True
    return negcorrection