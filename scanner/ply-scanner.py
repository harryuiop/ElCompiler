"""
This program uses PLY (Python Lex-Yacc). Documentation for PLY is
available at
    https://www.dabeaz.com/ply/ply.html

"""

import ply.lex as lex
import sys

# reserved words
reserved = {
    'do': 'DO',
    'else': 'ELSE',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'while': 'WHILE',
    'read': 'READ',
    'write': 'WRITE'

}

# all token types
tokens = [
    'SEM', 'BEC', 'LESS', 'EQ', 'GRTR', 'LEQ', 'NEQ', 'GEQ',
    'ADD', 'SUB', 'MUL', 'DIV', 'LPAR', 'RPAR', 'NUM', 'ID'
] + list(reserved.values())

"""
DOCUMENTAION FROM PLY FROM REFERENCE:

A regular expression is associated to a token as in the following
example:

    t_EXAMPLE1 = r'\+'

The declared name must start with 't_' and end with the name of a
token (an element of tokens). It is assigned a string denoting a
regular expression. The prefix 'r' of the string is not related to
regular expressions but specifies raw strings in Python. In raw
strings, Python does not treat backslashes as escape sequences.

By declaring a function instead of a string, an action can be
performed after a token has been matched:

    def t_EXAMPLE2(t):
        r'\+'
        t.type = 'ADD' # must be the name of a token
        t.value = 'ADD' # can be any value associated with the token
        return t

In this case, the regular expression is the docstring of the
function. The function has a single input 't', a token object with
attributes type and value, both of which are already set. The
attribute t.type is set to the function's name without 't_' and
t.value is set to the string that the regular expression matched.
These attributes can be modified if necessary, as shown above.
"""

# rules specifying regular expressions and actions

t_SEM = r';'
t_BEC = r':='
t_LESS = r'<'
t_EQ = r'='
t_GRTR = r'>'
t_LEQ = r'<='
t_GEQ = r'>='
t_ADD = r'\+'
t_SUB = r'-'
t_LPAR = r'\('
t_RPAR = r'\)'
t_MUL = r'\*'
t_DIV = r'/'
t_NEQ = r'!='
t_NUM = r'[0-9]+'


### add code for inequality, multiplication, division and numbers ###

def t_ID(t):

    r'[a-z]+'
    
    for res in reserved:
        if t.value == res:
            t.type = reserved[t.value]

    return t

# rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# rule to ignore whitespace
t_ignore = ' \t'

# error handling rule
def t_error(t):
    print("lexical error: illegal character '{}'".format(t.value[0]))
    t.lexer.skip(1)

# Show all tokens in the input.

scanner = lex.lex()
scanner.input(sys.stdin.read())

for token in scanner:
    if token.type in ['NUM', 'ID']:
        print(token.type, token.value)
    else:
        print(token.type)
