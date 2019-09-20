from random import randint, choice

def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)  # 相当于是以上注释的两行
    op = choice('+-')
    result = cmds[op](*nums)
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:  # 可以捕获所有异常，但是不建议
            continue

        if answer == result:
            print('Very good!')
            break
        else:
            print('Wrong answer.')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

if __name__ == '__main__':
    while True:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print('\nBye-bye')
            yn = 'n'

        if yn in 'nN':
            break
