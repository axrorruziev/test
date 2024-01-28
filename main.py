# Task 1
class Task1(object):
    def moveZeroes(self, nums):
        self.nums = nums
        lst = []
        for i in self.nums:
            if i == 0:
                lst.append(i)
                self.nums.remove(0)

        return self.nums + lst


t1 = Task1()
print(t1.moveZeroes([0, 1, 0, 3, 12]))


# Task 2
class Task2(object):
    def removeDuplicates(self, nums: list):
        self.nums = nums
        lst = []
        for i in self.nums:
            if i not in lst:
                lst.append(i)
        numbers = f'numbers = {len(lst)}'
        return numbers, lst


t2 = Task2()
print(t2.removeDuplicates([1, 8, 9, 5, 6, 8, 1, 6]))


# Task 3
class Task3(object):
    def IsPalindrome(self, string: str):

        reverse = ''.join(reversed(string))

        if reverse == string:
            return 'это палиндром'
        else:
            return 'это обычное слово'


t3 = Task3()
while True:
    s = (input('Введите слово: '))

    print(t3.IsPalindrome(s))
    if s == 'stop':
        print('Программа завершена')
        break


class Task4(object):
    def NumberPalindrome(self, x):
        reverse = int(str(x)[::-1])

        if reverse == x:
            return 'это палиндром'
        else:
            return 'это обычное число'

t4 = Task4()
while True:
    number = int(input('Введите число: '))

    print(t4.NumberPalindrome(number))