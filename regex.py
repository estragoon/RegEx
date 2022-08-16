
class regex(object):

    def valid(self, input, pattern):

        if not pattern:
        
            return not input

        initial = bool(input) and pattern[0] in {input[0], '.'}

        if len(pattern) > 1 and pattern[1] == '*':
            
            return (self.valid(input, pattern[2:]) or initial and self.valid(input[1:], pattern))
        
        else:
        
            return initial and self.valid(input[1:], pattern[1:])

