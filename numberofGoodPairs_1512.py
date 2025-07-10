class numberofGoodPairs_1512(object):

    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        sum_good_pairs = 0
        for i in range(len(nums), 0, -1):
            num = nums[i - 1]
            if (num in counts.keys()):
                counts.update({num : counts[num] + 1})
            else:
                counts.update({num : 0})
            current_count = counts[num]
            sum_good_pairs += current_count
        return sum_good_pairs