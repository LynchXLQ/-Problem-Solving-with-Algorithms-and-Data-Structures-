# Time: 2021/11/6  20:30
def anagramSolution1():
    word1 = input('Please enter the first word:')
    word2 = input('Please enter the second word:')
    lst1 = list(word1)
    lst2 = list(word2)
    print(f'list1:{lst1}, list2:{lst2}')
    cnt = 0
    if len(lst1) == len(lst2):
        for letter in lst1:
            if letter in lst2:
                cnt += 1
                print(cnt)
                lst1.remove(letter)
                lst2.remove(letter)
        if lst2 == lst1:
            return '* Is Anagram *'
        else:
            return '* Not Anagram *'
    else:
        return '* Not Anagram *'



def anagramSolution2():
    word1 = input('Please enter the first word:')
    word2 = input('Please enter the second word:')
    lst1 = list(word1)
    lst2 = list(word2)
    print(f'list1:{lst1}, list2:{lst2}')
    if sorted(lst1)==sorted(lst2):
        return '* Is Anagram *'
    else:
        return '* Not Anagram *'



def anagramSolution3():
    word1 = input('Please enter the first word:')
    word2 = input('Please enter the second word:')
    lst1 = [0] * 26
    lst2 = [0] * 26

    for i in range(len(word1)):
        index1 = ord(word1[i]) - ord('a')
        lst1[index1] += 1

    for j in range(len(word2)):
        index2 = ord(word2[j]) - ord('a')
        lst2[index2] += 1

    print(f'lst1 = {lst1}\nlst2 = {lst2}')
    if lst1 == lst2:
        return '* Is Anagram *'
    else:
        return '* Not Anagram *'


# print(anagramSolution1())
# print(anagramSolution2())
# print(anagramSolution3())

