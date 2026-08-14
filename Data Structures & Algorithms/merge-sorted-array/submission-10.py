class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, len(nums1)):
            nums1[i] = 0
        for index,num in enumerate(nums1):
            try:
                if nums2[index] < num: #add number to nums1
                    nums1.insert(index, nums2[index])
                else:
                    continue
            except:
                pass
        difference = n
        if len(nums1) > m:
            for index, num in enumerate(nums1):
                if difference != 0:
                    nums1.pop(len(nums1)-1)
                    difference -= 1
        