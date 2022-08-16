def main():

    print(regex('aa', 'a'))
    print(regex('aa', 'a*'))
    print(regex('ab', '.*'))

    print(regex('abacada', 'a.*'))

    print(regex('aab', 'c*a*b'))

    print(regex('mississippi', 'mis*is*ip*.'))

    print(regex('aaa', 'a*a'))

    print(regex('ab', '.*..'))

    print(regex('ab', '.*..c*'))

    print(regex('a', '.*..'))

def regex(input, pattern):

    buffer = ''

    etoile_buffer = ''
    
    etoile_input = input

    end = ''

    for i in range(len(pattern)):

        if etoile_input[-1:] == pattern[-1:] or pattern[-1:] == '.':

            end += etoile_input[-1:]

            pattern = pattern[:-1]

            etoile_input = etoile_input[:-1]
        
        else:

            if '*' not in pattern:
            
                break

            else:
            
                # Detect etoile in pattern
                if pattern[1] == '*':

                    # Put in etoile_buffer the text before the etoile
                    etoile_buffer = pattern[0]

                    # Match input == i * etoile_buffer (for maximum number of multiple for etoile_buffer)
                    for j in range(len(etoile_input)):

                        # Replace '.' by corresponding char in input
                        if etoile_buffer == '.':

                            dot_buffer = etoile_input[0]

                        else:

                            dot_buffer = etoile_buffer
                        
                        # If match, add to buffer and cut etoile_input
                        if etoile_input[0] == dot_buffer:

                            buffer += dot_buffer
                            
                            etoile_input = etoile_input[1:]

                        else:

                            break
                
                    # Cut etoile group from pattern_buffer
                    pattern = pattern[2:]

                else:

                    buffer += pattern[0]
                    
                    etoile_input = etoile_input[1:]

                    pattern = pattern[1:]

    for z in range(len(pattern)):

        if pattern[z] == '.':

            try:
                buffer += etoile_input[z]

            except IndexError:

                return False

        else:

            buffer += pattern[z]
    
    buffer += end[::-1]

    # Match for buffer == pattern
    if buffer == input:

        return True

    return False


if __name__ == '__main__':

    main()

