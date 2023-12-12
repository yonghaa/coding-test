palindrome = input()
if palindrome[::1] == palindrome[::-1]:
    print(1)
else:
    print(0)