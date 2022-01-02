class Solution(object):
    def plusOne(self, digits):
        i=1
        n=len(digits)
        while i<=n:
            digits[-i]+=1
            if digits[-i]==10 :
                digits[-i]=0
                if i==n :
                    digits.insert(0,1)
                i+=1
            else :
                break
        return digits