
# Python3 program to find the smallest window  
no_of_chars = 256
  
def findSubString(string, pat):  
  
    len1 = len(string)  
    len2 = len(pat)  

    if len1 < len2:  
      
        print("No such window exists")  
        return None
  
    hash_pat = [0] * no_of_chars 
    hash_str = [0] * no_of_chars  
  
    for i in range(len2):  
        hash_pat[ord(pat[i])] += 1
  
    start, start_index, min_len = 0, -1, float('inf')  

    count = 0
    for j in range(len1):  

        hash_str[ord(string[j])] += 1
  
        if (hash_pat[ord(string[j])] != 0 and
            hash_str[ord(string[j])] <= 
            hash_pat[ord(string[j])]):  
            count += 1

        if count == len2:  
 
            while (hash_str[ord(string[start])] >  
                   hash_pat[ord(string[start])] or
                   hash_pat[ord(string[start])] == 0):  
              
                if (hash_str[ord(string[start])] >  
                    hash_pat[ord(string[start])]):  
                    hash_str[ord(string[start])] -= 1
                start += 1
              
            len_window = j - start + 1
            if min_len > len_window:  

                min_len = len_window  
                start_index = start  

    if start_index == -1: 
        print("No such window exists")  
        return None  
        
    return string[start_index : start_index + min_len]  

if __name__ == "__main__": 
    string = "this is a test string"
    pat = "tist"
    print("Smallest window is : ") 
    print(findSubString(string, pat))  