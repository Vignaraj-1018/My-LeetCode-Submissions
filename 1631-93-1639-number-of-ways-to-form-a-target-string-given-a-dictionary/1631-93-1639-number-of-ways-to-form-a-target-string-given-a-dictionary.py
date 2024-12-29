class Solution:
    MOD = 1000000007
    def numWays(self, words: List[str], target: str) -> int:
        target_size = len(target)
        word_size = len(words[0])
        n = len(words)
        char_freq = [[0] * 26 for _ in range(word_size)]

        # Calculate char freq for each position
        for word in words:
            for j, char in enumerate(word):
                char_freq[j][ord(char) - ord('a')] += 1

        mem = [[-1] * target_size for _ in range(word_size)]

        def count_ways(idx, tpos):
            if tpos == target_size:  # Match
                return 1 if idx <= word_size else 0
            if idx >= word_size or (word_size - idx < target_size - tpos):  # No Match or Insufficient Size
                return 0
            if mem[idx][tpos] != -1:  # Repeating sub-problem
                return mem[idx][tpos]

            curr = target[tpos]
            ways_by_not_matching = count_ways(idx + 1, tpos)
            ways_by_matching = count_ways(idx + 1, tpos + 1) % self.MOD
            total_ways = (ways_by_not_matching + char_freq[idx][ord(curr) - ord('a')] * ways_by_matching) % self.MOD

            mem[idx][tpos] = total_ways
            return mem[idx][tpos]

        return count_ways(0, 0)