"""
Calculates whether two target variables M & F can be reached from two starting values
of 1 and 1. Each iteration, one value must increase by the other's value. The number of
iterations, or "cycles", must be printed when the target values are reached. Otherwise,
print "impossible".
"""
def answer(M, F):
    numM = int(M)
    numF = int(F)
    cycles = 0
    # On each iteration, see how many times the smaller number goes into
    # the larger number. We are iterating on the condition that the last
    # step must be adding the smaller number X times to the larger number.
    while numM > 0 and numF > 0:
        if numM > numF:
            # Check if one value is a multiple of another.
            if numM % numF == 0:
                # If one value is 1, your final answer is numM - 1.
                if numF == 1:
                    numTimes = numM - 1
                    cycles += numTimes
                    return str(cycles)
                # If the two numbers are multiples, you cannot achieve numM=1 & numF=1.
                else:
                    break
            # Otherwise, subtract the larger number by (numM / numF) * numF.
            else:
                numTimes = numM / numF
                cycles += numTimes
                numM = numM - numTimes * numF
        # The same logic as above applies, except reversing numM with numF.
        elif numF > numM:
            if numF % numM == 0:
                if numM == 1:
                    numTimes = numF - 1
                    cycles += numTimes
                    return str(cycles)
                else:
                    break
            else:
                numTimes = numF / numM
                cycles += numTimes
                numF = numF - numTimes * numM
    return "impossible"
