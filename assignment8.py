#In this task you will given a word and you must find the longest subword of this word that is also a palindrome.

#For example if the given word is abbba then the answer is abbba. If the given word is abcbcabbacba then the answer is bcabbacb.





def longestPalSubstr(string):
    n = len(string) # calculating size of string
    if (n < 2):
        return n # if string is empty then size will be 0.
                  # if n==1 then, answer will be 1(single
                  # character will always palindrome)
    start=0
    maxLength = 1
    for i in range(n):
        low = i - 1
        high = i + 1
        while (high < n and string[high] == string[i] ):                              
            high=high+1
       
        while (low >= 0 and string[low] == string[i] ):                
            low=low-1
       
        while (low >= 0 and high < n and string[low] == string[high] ):
          low=low-1
          high=high+1
         
     
        length = high - low - 1
        if (maxLength < length):
            maxLength = length
            start=low+1
             
 
     
    return maxLength,string[start:start + maxLength]
  
  
