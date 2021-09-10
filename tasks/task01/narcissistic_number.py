k = int(input('Please enter an integer k(1<=k<=1000): '))
if 1 <= k <= 1000:
    powers = 1
    for i in range(1, k + 1):
        #
        if 10**powers < i:
            powers += 1
        # sum of narcissistic numbers
        narcissisticNumbSum = 0
        # a string showing the sum of the narcissistic numbers
        narcissisticNumbStr = ""
        # whole part of division
        divWholePart = i

        while divWholePart > 0:
            # get remainder of division
            # last digit of numbers
            divRemainder = divWholePart % 10

            narcissisticNumbSum += divRemainder ** powers

            # conversion for rendering information
            if narcissisticNumbStr:
                narcissisticNumbStr = " + " + narcissisticNumbStr
            narcissisticNumbStr = str(divRemainder) + "**" + str(powers) + narcissisticNumbStr

            # get the new integer part of the narcissistic number
            divWholePart //= 10

        if i == narcissisticNumbSum:
            print("Narcissistic number: ", i, " = ", narcissisticNumbStr)
else:
    # if the user entered an incorrect k, show auxiliary information
    print("You entered wrong k, k must be 1 <= k <= 1000")