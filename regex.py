from math import ceil

def main():

    print(regex('aa', 'a'))
    print(regex('aa', 'a*'))
    print(regex('ab', '.*'))

    print(regex('abacada', 'a.*'))

    print(regex('aab', 'c*a*b'))

def regex(input, pattern):
    
    etoile_buffer = ''
    
    for i in range(len(pattern)):

        # Detect etoile in pattern
        if pattern[i] == '*':

            # Put in etoile_buffer the text before the etoile
            etoile_buffer = pattern[:i]

            # Get maximum number of multiple for etoile_buffer
            x = ceil(len(input) / len(etoile_buffer))

            # Match input == i * etoile_buffer
            for j in range(0, x + 1):

                dot_buffer = list(etoile_buffer * j)

                # Replace each '.' by corresponding char in input
                for i in range(len(dot_buffer)):

                    if dot_buffer[i] == '.':

                        try:
                            dot_buffer[i] = input[i]
                        
                        except IndexError:
                            return False

                dot_buffer = ''.join(dot_buffer)

                # Match for input == dot_buffer
                if input == dot_buffer:

                    return True

            return False

    # If no etoile, match for input == pattern
    if input == pattern:

        return True

    return False


if __name__ == '__main__':

    main()

