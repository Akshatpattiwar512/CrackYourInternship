# Convert a non-negative integer num to its English words representation.

class Solution:
    def numberToWords(self, num: int) -> str:
        ones = {
                0: '',
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
        tens = {
                0: 'Ten',
                1: 'Eleven',
                2: 'Twelve',
                3: 'Thirteen',
                4: 'Fourteen',
                5: 'Fifteen',
                6: 'Sixteen',
                7: 'Seventeen',
                8: 'Eighteen',
                9: 'Nineteen'
            }
        hundreds = {
                0: '',
                1: 'Ten',
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
        
        res = ''
        
        if num==0:
            return 'Zero'
        elif num<10:
            res =  ones[num]
        elif num<20:
            res =  tens[num-10]
        elif num<100:
            res = hundreds[num//10] + ' ' + ones[num%10]
        elif num<1000:
            res = self.numberToWords((num//100)) + ' Hundred ' + self.numberToWords(num%100)
        elif num<1000000:
            res = self.numberToWords((num//1000)) + ' Thousand ' + self.numberToWords(num%1000)
        elif num<1000000000:
            res = self.numberToWords((num//1000000)) + ' Million ' + self.numberToWords(num%1000000)
        else:
            res = self.numberToWords((num//1000000000)) + ' Billion ' + self.numberToWords(num%1000000000)
        return res.replace('Zero','').strip()
