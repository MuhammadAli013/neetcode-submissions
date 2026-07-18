class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def wait_day(day_temp,_list):
            # last value case
            if len(_list) == 0:
                return 0
            count = 1
            done = False
            for ith in _list:
                if ith>day_temp:
                    done = True
                    return count
                elif ith <=day_temp:
                    count = count + 1
            if done == False:
                return 0
        # full_list = [30,40,50,60]
        tot_count = 0
        ans = []
        for elem in temperatures:
            # print(elem)
            # print(full_list[tot_count+1:])
            t1 = wait_day(elem,temperatures[tot_count+1:])
            ans.append(t1)
            tot_count = tot_count + 1
        return ans