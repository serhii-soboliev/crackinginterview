from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for human in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(human[1], [human[0], human[1]])
        return res
