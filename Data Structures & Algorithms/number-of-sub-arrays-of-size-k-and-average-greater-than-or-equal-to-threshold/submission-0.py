class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        for right in range(k,len(arr)+1):
            # print(arr[right])
            left = right - k
            window = arr[left:right]
            # print(window)
            avg = sum(window)/k
            if avg >= threshold:
                count = count + 1
        return count