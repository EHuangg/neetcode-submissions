class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(s.split())
        new_s = new_s.lower()
        new_s = ''.join(char for char in new_s if char.isalnum())
        reverse_s = ""
        print (new_s)
        for i in range (len(new_s) - 1, -1, -1):
            reverse_s += (str(new_s[i]))
            print(reverse_s)
        if reverse_s == new_s:
            return True
        return False