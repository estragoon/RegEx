from math import ceil

def main():

    print(regex('aa', 'a'))
    print(regex('aa', 'a*'))
    print(regex('ab', '.*'))

    print(regex('abacada', 'a.*'))

    print(regex('aab', 'c*a*b'))

    print(regex('mississippi', 'mis*is*ip*.'))

def regex(input, pattern):

    buffer = ''

    etoile_index = -1

    etoile_buffer = ''
    
    etoile_input = input

    pattern_buffer = pattern

    for i in range(len(pattern)):

        # Detect etoile in pattern
        if pattern[i] == '*':

            # Put in etoile_buffer the text before the etoile
            etoile_buffer = pattern[etoile_index + 1 : i]

            etoile_index = i

            # Match input == i * etoile_buffer (for maximum number of multiple for etoile_buffer)
            for j in range(ceil(len(etoile_input) / len(etoile_buffer))):

                dot_buffer = list(etoile_buffer)

                # Replace each '.' by corresponding char in input
                for o in range(len(dot_buffer)):

                    if dot_buffer[o] == '.':

                        try:
                            dot_buffer[o] = etoile_input[o]
                        
                        except IndexError:
                            return False

                dot_buffer = ''.join(dot_buffer)

                if etoile_input[:len(dot_buffer)] == dot_buffer:

                    buffer += dot_buffer
                    
                    etoile_input = etoile_input[len(dot_buffer):]

                else:

                    break
        
            pattern_buffer = pattern_buffer[len(etoile_buffer) + 1 :]
                    
    buffer += pattern_buffer

    # Match for buffer == pattern
    if buffer == input:

        return True

    return False


if __name__ == '__main__':

    main()

