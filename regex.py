
def main():

    regex('aa', 'a')
    regex('aa', 'a*')
    regex('ab', '.*')

def regex(input, pattern):
    
    buffer = ''
    
    for i in range(len(pattern)):

        if pattern[i] == '*':

            buffer = pattern[:i]

            print(buffer)


if __name__ == '__main__':

    main()

