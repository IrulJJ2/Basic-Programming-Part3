def palindrome(input_string):
    length = len(input_string)
    for x in range (0,length//2):
        if (input_string[x] != input_string[length-x-1]):
            return False   
        return True


if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False