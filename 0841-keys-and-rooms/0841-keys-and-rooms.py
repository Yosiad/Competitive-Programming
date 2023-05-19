class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q=collections.deque([rooms[0]])
        seen=set()
        while q:
            keys=q.popleft()
            for key in keys:
                if  key not in seen:
                    q.append(rooms[key])
                    if key:seen.add(key)
        return len(seen)==len(rooms)-1