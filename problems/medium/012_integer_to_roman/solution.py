class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = ""
        
        for i in range(len(values)):
            # Quantas vezes o valor atual cabe no número
            count = num // values[i]
            if count:
                result += symbols[i] * count
                num %= values[i]
        
        return result