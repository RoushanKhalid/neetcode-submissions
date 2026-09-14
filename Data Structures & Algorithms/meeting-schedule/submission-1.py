class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        flag = True

        if intervals == []:
            return flag

        #1 big most, small most -> value find out
        #2 then small to big array -> all zero
        #3 all subarray loop start to end and add 1 each; so the most value would be 1
        #4 if any of total array value goes 2 or more then its overlapping. 

        arr = []

        for pair in intervals:
            arr.append(pair.start)
            arr.append(pair.end)

        #1
        big = max(arr)
        sml = min(arr)

        #2
        main_arr = [0] * (big + 1)

        #3
        for pair in intervals:
            start = pair.start
            end = pair.end

            for i in range(start, end):
                main_arr[i] += 1

        #4
        for value in main_arr:
            if value >= 2:
                flag = False
                break

        return flag