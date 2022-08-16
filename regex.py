
def main():

    print(regex('ab', 'aa'))
    print(regex('aa', 'aa'))

def regex(input, pattern):
    
    if input == pattern:

        return True

    else:

        return False


if __name__ == '__main__':

    main()

