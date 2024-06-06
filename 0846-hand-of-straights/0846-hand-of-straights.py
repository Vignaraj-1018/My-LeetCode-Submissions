class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        print(count)
        for card in sorted(count):
            if count[card] > 0:
                num_groups = count[card]
                for i in range(groupSize):
                    if count[card + i] < num_groups:
                        return False
                    count[card + i] -= num_groups
        
        return True