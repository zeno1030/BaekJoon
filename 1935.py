n=int(input())
cal = input()
num_list=[0]*n

for i in range(n):
    num_list[i]=int(input())

stack = []

for i in cal:
    if 'A'<=i<='Z':
        stack.append(num_list[ord(i)-ord('A')])
    else :
        str2 = stack.pop()
        str1 = stack.pop()

    if i=='+':
        stack.append(str1+str2)
    elif i == '-':
        stack.append(str1-str2)
    elif i == '*':
        stack.append(str1 * str2)
    elif i == '/':
        stack.append(str1/str2)

print('%.2f'%stack[0])
