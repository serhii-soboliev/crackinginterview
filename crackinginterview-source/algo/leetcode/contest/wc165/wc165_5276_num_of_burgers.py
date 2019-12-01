class NumOfBurgers:

    def result(self, tomatoSlices, cheeseSlices):
        if [0, 0] == [tomatoSlices, cheeseSlices]:
            return [0, 0]
        if tomatoSlices < 2 * cheeseSlices or 4 * cheeseSlices < tomatoSlices or tomatoSlices % 2 == 1:
            return []
        jumbo_burgers = int((tomatoSlices - 2 * cheeseSlices) / 2)
        return [jumbo_burgers, cheeseSlices - jumbo_burgers]
