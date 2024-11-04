# Algoritmo de un palindrome

def isPalindromo(str):
    starIndex = 0
    endIndex = len(str) -1

    for x in str: 
        if str[starIndex] != str[endIndex]:
            return False
    return True

print(isPalindromo("osos")) 