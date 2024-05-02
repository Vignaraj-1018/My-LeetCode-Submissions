class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans=0
        for item in items:
            if ruleKey == 'type' and item[0]==ruleValue:
                ans+=1
            if ruleKey == 'color' and item[1]==ruleValue:
                ans+=1
            if ruleKey == 'name' and item[2]==ruleValue:
                ans+=1
        
        return ans