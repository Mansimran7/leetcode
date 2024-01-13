class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dic = {}

        for pos, i in enumerate(nums):
            if i not in dic:
                dic[i] = pos
            else:
                if abs(pos-dic[i]) <= k:
                    return True
                else:
                    dic[i] = pos
        return False
