def  recursivePalindrome(stringa : str):
    stringa = stringa.replace(" ", "").lower()

    if len(stringa) <= 1 :
        return True
    
    if stringa[0] != stringa[-1]:
        return False
    

    return recursivePalindrome(stringa[1:-1])





test = recursivePalindrome("I topi non avevano nipoti")
print(test)