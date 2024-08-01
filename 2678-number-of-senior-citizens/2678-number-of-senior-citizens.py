class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        cnt=0
        for detail in details:
            age = detail[11] + detail[12]
            if int(age)>60: 
                cnt+=1
        return cnt