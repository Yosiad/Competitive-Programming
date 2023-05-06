class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        total=abs((ay2-ay1)*(ax2-ax1))+abs((by2-by1)*(bx2-bx1))
        diff=0
        if ay2>=by2 and ay1<by2 and ax2>=bx2 and ax1<bx2:
            diff=(by2-max(ay1,by1))*(bx2-max(ax1,bx1))
        elif by2>=ay2 and by1<ay2 and ax2>=bx2 and ax1<bx2:
            diff=(ay2-max(ay1,by1))*(bx2-max(ax1,bx1))
        if ay2>=by2 and ay1<by2 and bx2>=ax2 and bx1<ax2:
            diff=(by2-max(ay1,by1))*(ax2-max(ax1,bx1))
        if by2>=ay2 and by1<ay2 and bx2>=ax2 and bx1<ax2:
            diff=(ay2-max(ay1,by1))*(ax2-max(ax1,bx1))
        return total-diff