class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg = True if numerator/denominator < 0 else False
        numerator = -numerator if numerator < 0 else numerator
        denominator = -denominator if denominator < 0 else denominator
        out = str(numerator//denominator)
        if numerator % denominator:
            out += "."
        remainders = []
        quotients = []
        numerator %= denominator
        while numerator:
            numerator *= 10
            if str(numerator) in remainders:
                duplicateStart = remainders.index(str(numerator))
                out += "".join(quotients[:duplicateStart])
                out += "("+"".join(quotients[duplicateStart:])+")"
                return "-"+out if neg else out
            else:
                remainders.append(str(numerator))
                quotients.append(str(numerator // denominator))
                numerator %= denominator
        out += "".join(quotients)
        return "-"+out if neg else out