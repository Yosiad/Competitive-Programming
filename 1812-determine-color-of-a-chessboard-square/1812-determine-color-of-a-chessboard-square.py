class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        odd=["a","c","e","g"]
        even=["b","d","f","h"]
        if (coordinates[0] in odd and not int(coordinates[1])%2) or (coordinates[0] in even and  int(coordinates[1])%2):
                                                                return True
        return False                                                            