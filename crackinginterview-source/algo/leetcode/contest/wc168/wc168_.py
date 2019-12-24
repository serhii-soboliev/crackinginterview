class Solution:

    def max_candies(self, status, candies, keys, containedBoxes, initialBoxes):
        candies_cnt = 0
        my_keys = []
        current_boxes = initialBoxes
        opened = True
        while opened:
            opened = False
            new_boxes = []
            for box in current_boxes:
                if status[box] == 1 or box in my_keys:
                    opened = True
                    candies_cnt += candies[box]
                    new_boxes += containedBoxes[box]
                    my_keys += keys[box]
                else:
                    new_boxes.append(box)
            current_boxes = new_boxes
        return candies_cnt

    def maxFreq(self, s, maxLetters, minSize, maxSize):
        n = len(s)
        sub_dict = {}
        for i in range(n - minSize + 1):
            sub = s[i:i + minSize]
            if sub in sub_dict:
                sub_dict[sub] = sub_dict[sub] + 1
            elif len(set(list(sub))) <= maxLetters:
                sub_dict[sub] = 1

        if not sub_dict:
            return 0
        else:
            return sub_dict[max(sub_dict.keys(), key=(lambda k: sub_dict[k]))]

    def findNumbers(nums):
        return len(list(filter(lambda x: len(str(x)) % 2 == 0, nums)))

    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False
        else:
            nums = sorted(nums)
            n = len(nums)
            nums_cnt = {}
            mmin = 10 ** 9
            for num in nums:
                nums_cnt[num] = nums_cnt.get(num, 0) + 1
                mmin = min(mmin, num)

            m = n // k
            for i in range(m):
                p_min = mmin
                for j in range(k):
                    cur_num = p_min + j
                    if cur_num not in nums_cnt:
                        return False
                    else:
                        cur_cnt = nums_cnt[cur_num]
                        if cur_cnt > 1:
                            nums_cnt[cur_num] = cur_cnt - 1
                        else:
                            nums_cnt.pop(cur_num, None)
                            if cur_num == mmin and nums_cnt:
                                new_min = mmin + 1
                                while True:
                                    if new_min in nums_cnt:
                                        mmin = new_min
                                        break
                                    else:
                                        new_min += 1
            return True

    def isValid(self, st: str) -> bool:
        par = []
        for s in st:
            if s == "(":
                par.append(s)
            if s == ")":
                if not par or par.pop() != "(":
                    return False

            if s == "{":
                par.append(s)
            if s == "}":
                if not par or par.pop() != "{":
                    return False

            if s == "[":
                par.append(s)
            if s == "]":
                if not par or par.pop() != "[":
                    return False

        return not par
