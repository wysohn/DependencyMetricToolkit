#!/usr/bin/env python3

import os
import sys

from ply import lex

# Define the list of token names
tokens = [
    'IDENTIFIER',
    'INTEGER_LITERAL',
    'STRING_LITERAL',
    'KEYWORD',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMENT',
    'IMPORT',
]

# Regular expression rules for tokens
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INTEGER_LITERAL = r'\d+'
t_STRING_LITERAL = r'\"([^\\\n]|(\\.))*?\"'
t_KEYWORD = r'class|interface|abstract'

t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMENT = r'//.*|/\*(.|\n)*?\*/'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule


def t_IMPORT(t):
    r'import\s+[\w.]+(?:\*|\.[\w*]+)?\s*;'
    return t


def t_error(t):
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


def read_java_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    yield file_path, f.read()


# Test the lexer
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Please provide the folder path and package prefix as an argument.')
        sys.exit(1)

    folder_name = sys.argv[1]
    package_prefix = sys.argv[2]
    java_files_generator = read_java_files(folder_name)

    number_of_imports = 0

    for file_path, java_code in java_files_generator:
        lexer.input(java_code)
        for token in lexer:
            if token.type == 'IMPORT' and token.value.startswith('import ' + package_prefix):
                print(file_path)
                print(token.value)
                number_of_imports += 1
                break

    print('Number of files that imports from {}: {}'.format(
        package_prefix, number_of_imports))
