class Solution:
    def checkString(self, s: str) -> bool:
        last_a_pos = 0
        last_b_pos = math.inf
        
        for indx, val in enumerate(s):
            if val == 'a':
                last_a_pos = indx
            else:
                last_b_pos = indx
                
            if last_a_pos > last_b_pos:
                return False
        return True