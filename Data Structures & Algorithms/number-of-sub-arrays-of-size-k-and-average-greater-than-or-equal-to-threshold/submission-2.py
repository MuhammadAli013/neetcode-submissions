class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # count = 0
        # for right in range(k,len(arr)+1):
        #     # print(arr[right])
        #     left = right - k
        #     window = arr[left:right]
        #     # print(window)
        #     avg = sum(window)/k
        #     if avg >= threshold:
        #         count = count + 1
        # return count
        window = arr[0:k]
        count = 0

        window_sum = sum(window)
        avg = window_sum / k
        if avg>=threshold:
            count = count + 1
        print(window_sum)
        for right in range(k,len(arr)):
            left = right - k # this one will be avoided
            # right will be added
            window_sum = window_sum - arr[left] + arr[right]    
            avg = window_sum/k
            if avg >= threshold:
                count = count + 1
        return count