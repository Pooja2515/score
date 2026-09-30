import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        meetings.sort()
        
        available = list(range(n))
        heapq.heapify(available)
        
        busy = []
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (end_time + duration, room))
            
            count[room] += 1
        
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i


if __name__ == "__main__":
    sol = Solution()
    
    n = 2
    meetings = [[0,10],[1,5],[2,7],[3,4]]
    print(sol.mostBooked(n, meetings)) 
   
    n = 3
    meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    print(sol.mostBooked(n, meetings)) 

