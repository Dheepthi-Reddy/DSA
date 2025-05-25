'''
A string without considering the alphanumeric values spells same when written backwards.

An empty string is also a Palindrome
'''

class Solution:
  def isPalindrome(self, s: str) -> bool:

    first, last = 0, len(s) - 1
    while first < last:
      if not s[first].isalnum():
        first += 1
        continue
      if not s[last].isalnum():
        last -= 1
        continue
      if s[first].lower() != s[last].lower():
        return False
  
      first, last = first + 1, last - 1
    return True

'''
O/P:

"A man, a plan, a canal: Panama" - True
"race a car" - False
" " - True

'''
