import math

class RadixSorter:
    def __init__(self, base):
        self.base = base

    def countingSortRadix(self, vals, radix):
        countingList = [0] * self.base

        for val in vals:
            radixVal = (val // radix) % self.base
            countingList[radixVal] += 1

        for i in range(1, self.base):
            countingList[i] += countingList[i - 1]

        resultantList = [0] * len(vals)
        i = len(vals) - 1
        while i >= 0:
            cur = vals[i]
            radixVal = (vals[i] // radix) % self.base
            countingList[radixVal] -= 1
            j = countingList[radixVal]
            resultantList[j] = cur
            i -= 1

        return resultantList

    def floorLog(self, n):
        x = math.floor(math.log(n, self.base))
        r = self.base**x
        return x + (self.base*r <= n) - (r > n)

    def digitLen(self, n):
        return 1 if n == 0 else 1 + self.floorLog(abs(n))

    def radixSort(self, vals):
        if not all(isinstance(e, int) for e in vals):
            raise TypeError("Expecting values to be of type int only")
        maxVal = max(vals)
        maxDigits = self.digitLen(maxVal)

        curRadix = 1
        sortedVals = vals
        while maxDigits > 0:
            sortedVals = self.countingSortRadix(sortedVals, curRadix)
            curRadix *= self.base
            maxDigits -= 1

        for i, sortedVal in enumerate(sortedVals):
            if sortedVal < 0:
                sortedVals = sortedVals[i:] + sortedVals[:i]
                break

        return sortedVals

if __name__ == "__main__":
    sample = [1, -5, -12, 63, 21, 67, 81, 26]
    sorter = RadixSorter(base=10)
    sortedSample = sorter.radixSort(sample)

    print(sample)
    print(sortedSample)
