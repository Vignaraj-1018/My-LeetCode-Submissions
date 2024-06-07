class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        for w in range(len(sentence)):
            for i in range(len(sentence[w])):
                if sentence[w][:i] in dictionary:
                    sentence[w] = sentence[w][:i]
                
                       
        return " ".join(sentence)