# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(below, elbow):
    # [assignment] Add your code here
    str1 = input("string: ")
    str2 = input("string2: ")

    #sort the string
    if(sorted(str1) == sorted(str2)):
        print(sorted(str1), sorted(str2))

    #compare the string
 
     

    return False
    print(find_anagram("below", "elbow"))
    print(find_anagram("hello", "check"))