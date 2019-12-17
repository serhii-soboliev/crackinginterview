from typing import List


class MinHeightShelves:

    def min_height_shelves(self, books: List[List[int]], shelf_width: int) -> int:
        if not books:
            return 0
        n = len(books)
        min_height = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            cur_min = min_height[i - 1] + books[i-1][1]
            start = i-1
            while start > 0:
                books_on_shelve = books[start-1:i]
                lst = sum([b[0] for b in books_on_shelve])
                if lst > shelf_width:
                    break
                max_height = max([b[1] for b in books_on_shelve])
                cur_min = min(max_height + min_height[start-1], cur_min)
                start -= 1
            min_height[i] = cur_min
        return min_height[n]


