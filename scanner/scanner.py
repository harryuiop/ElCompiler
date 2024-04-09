import re
import sys

class Scanner:
    '''The interface comprises the methods lookahead and consume.
       Other methods should not be called from outside of this class.
    '''

    def __init__(self, input_file):
        '''Reads the whole input_file to input_string, which remains constant.
           current_char_index counts how many characters of input_string have
           been consumed.
           current_token holds the most recently found token and the
           corresponding part of input_string.
        '''
        # source code of the program to be compiled t
        self.input_string = input_file.read()
        # index where the unprocessed part of input_string starts
        self.current_char_index = 0
        # a pair (most recently read token, matched substring of input_string)
        self.current_token = self.get_token()

    def skip_white_space(self):
        '''Consumes white-space characters in input_string up to the 
           next non-white-space character.
        '''
        current_index = self.current_char_index

        while current_index < len(self.input_string) and self.input_string[current_index].isspace():
            current_index += 1
        
        self.current_char_index = current_index
        

    def no_token(self):
        '''Stop execution if the input cannot be matched to a token.'''
        print('lexical error: no token found at the start of ' +
              self.input_string[self.current_char_index:])
        sys.exit()

    def get_token(self):
        '''Returns the next token and the part of input_string it matched.
           The returned token is None if there is no next token.
           The characters up to the end of the token are consumed.
           TODO:
           Call no_token() if the input contains extra characters that 
           do not match any token (and are not white-space).
        '''
        self.skip_white_space()
        # find the longest prefix of input_string that matches a token
        token, longest = None, ''
        for (t, r) in Token.token_regexp:
            match = re.match(r, self.input_string[self.current_char_index:])
            if match and match.end() > len(longest):
                token, longest = t, match.group()
        # consume the token by moving the index to the end of the matched part

        if token == None and self.current_char_index < len(self.input_string):
            self.no_token()

        self.current_char_index += len(longest)
        return (token, longest)

    def lookahead(self):
        '''Returns the next token without consuming it.
           Returns None if there is no next token.
        '''
        return self.current_token[0]

    def unexpected_token(self, found_token, expected_tokens):
        '''Stop execution because an unexpected token was found.
           found_token contains just the token, not its value.
           expected_tokens is a sequence of tokens.
        '''
        print('syntax error: token in ' + repr(sorted(expected_tokens)) +
              ' expected but ' + repr(found_token) + ' found')
        sys.exit()

    def consume(self, *expected_tokens):
        '''Returns the next token and consumes it, if it is in
           expected_tokens. Calls unexpected_token(...) otherwise.
           If the token is a number or an identifier, not just the
           token but a pair of the token and its value is returned.
        '''

        for token in Token.token_regexp:
            
            if expected_tokens[0] == token[0]:

                if expected_tokens[0] == Token.ID or expected_tokens[0] == Token.NUM:
                    token_to_return = self.current_token
                    self.current_token = self.get_token()
                    return token_to_return

                token_to_return = self.current_token[0]
                self.current_token = self.get_token()
                return token_to_return

        Scanner.unexpected_token(self, expected_tokens[0], Token.token_regexp)

class Token:
    # The following enumerates all tokens.
    DO    = 'DO'
    ELSE  = 'ELSE'
    END   = 'END'
    IF    = 'IF'
    THEN  = 'THEN'
    WHILE = 'WHILE'
    SEM   = 'SEM'
    BEC   = 'BEC'
    LESS  = 'LESS'
    EQ    = 'EQ'
    GRTR  = 'GRTR'
    LEQ   = 'LEQ'
    NEQ   = 'NEQ'
    GEQ   = 'GEQ'
    ADD   = 'ADD'
    SUB   = 'SUB'
    MUL   = 'MUL'
    DIV   = 'DIV'
    LPAR  = 'LPAR'
    RPAR  = 'RPAR'
    NUM   = 'NUM'
    ID    = 'ID'
    READ  = 'READ'
    WRITE = 'WRITE'

    # The following list gives the regular expression to match a token.
    # The order in the list matters for mimicking Flex behaviour.
    # Longer matches are preferred over shorter ones.
    # For same-length matches, the first in the list is preferred.
    token_regexp = [
        (DO,    'do'),
        (ELSE,  'else'),
        (END,   'end'),
        (IF,    'if'),
        (THEN,  'then'),
        (WHILE, 'while'),
        (READ,  'read'),
        (WRITE, 'write'),
        (SEM,   ';'),
        (BEC,   ':='),
        (LESS,  '<'),
        (EQ,    '='),
        (DIV,   '/'), 
        (GRTR,  '>'),
        (LEQ,   '<='),
        (GEQ,   '>='),
        (NEQ,   '!='),
        (MUL,   '\\*'),
        (ADD,   '\\+'), # + is special in regular expressions
        (SUB,   '-'),
        (LPAR,  '\\('), # ( is special in regular expressions
        (RPAR,  '\\)'), # ) is special in regular expressions
        (ID,    '[a-z]+'),
        (NUM,   '[0-9]+'),
    ]

# Initialise scanner.

#scanner = Scanner(sys.stdin)
scanner = Scanner(open("test2.txt"))

# Show all tokens in the input.

token = scanner.lookahead()
while token != None:
    if token in [Token.NUM, Token.ID]:
        token, value = scanner.consume(token)
        print(token, value)
    else:
        print(scanner.consume(token))
    token = scanner.lookahead()



