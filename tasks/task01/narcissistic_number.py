k = int(input('Please enter an integer k(1<=k<=1000): '))

powers = 1
for i in range(k+1):
    # sum of narcissistic numbers
    narcissisticNumbSum = 0
    # a string showing the sum of the narcissistic numbers
    printString = ""
    # whole part of division
    divWholePart = i

    if 10**powers < i:
        powers += 1

    while divWholePart > 0:
        # get remainder of division
        # last digit of numbers
        divRemainder = divWholePart % 10
        narcissisticNumbSum += divRemainder ** powers
        # conversion for rendering information
        stringDivRemainderInPower = f"{divRemainder}^{powers}"
        printString = f"{stringDivRemainderInPower} + {printString}" if printString else stringDivRemainderInPower
        # get the new integer part of the narcissistic number
        divWholePart //= 10

    if i and i == narcissisticNumbSum:
        print(f"Narcissistic number: {i} = {printString}")
