from math import ceil


def main():

    print(regex('aa', 'a'))
    print(regex('aaaaa', 'a*'))
    print(regex('ab', '.*'))

def regex(input, pattern):
    
    buffer = ''
    
    for i in range(len(pattern)):

        # Detect etoile in pattern
        if pattern[i] == '*':

            # Put in buffer the text before the etoile
            buffer = pattern[:i]

            # Get maximum number of multiple for buffer
            x = ceil(len(input) / len(buffer))

            # Match input == i * buffer
            for j in range(0, x + 1):

                if input == buffer * j:

                    return True

            return False

    # If no etoile match for input == pattern
    if input == pattern:

        return True

    return False


if __name__ == '__main__':

    main()

