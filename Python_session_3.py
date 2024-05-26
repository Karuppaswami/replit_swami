class Solution(object):
    def winnerOfGame(self, colors):
         colors = colors.length();
         aliceWins = 0, 
         bobWins = 0;
         for  i in range (i == 1, i < colors - 1, ++i):
          if (colors[i - 1] == 'A' and colors[i] == 'A' and colors[i + 1] == 'A'):
              aliceWins++
           elif (colors[i - 1] == 'B' and colors[i] == 'B' and colors[i + 1] == 'B'):
                bobWins++
        
         if (aliceWins > bobWins):
            return true
        else:
        
             return false
            

t1 = Solution()
user_input = input("Enter the value: ")
print(t1.winnerOfGame(user_input))
