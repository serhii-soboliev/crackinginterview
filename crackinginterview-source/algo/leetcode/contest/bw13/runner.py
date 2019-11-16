from algo.leetcode.contest.bw13.bw13_5110_synonymous_sentences import Solution

synonyms = [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]]
text = "I am happy today but was sad yesterday"
print(Solution().generate_sentences(synonyms, text))
