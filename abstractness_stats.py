#!/usr/bin/env python3

import os
import sys
import csv

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
    if len(sys.argv) < 2:
        print('Please provide the folder path as an argument.')
        sys.exit(1)

    folder_names = sys.argv[1:]

    with open('abstractness.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Project', 'A'])

        for folder_name in folder_names:
            java_files_generator = read_java_files(folder_name)

            num_classes = 0
            num_abstract_classes = 0
            num_interfaces = 0

            for file_path, java_code in java_files_generator:
                lexer.input(java_code)
                for token in lexer:
                    if token.type == 'KEYWORD' and token.value == 'abstract':
                        # print('Abstract class:', file_path)
                        num_abstract_classes += 1
                        break
                    elif token.type == 'KEYWORD' and token.value == 'class':
                        # print('Class:', file_path)
                        num_classes += 1
                        break
                    elif token.type == 'KEYWORD' and token.value == 'interface':
                        # print('Interface:', file_path)
                        num_interfaces += 1
                        break

            print(f'Number of classes: {num_classes}')
            print(f'Number of abstract classes: {num_abstract_classes}')
            print(f'Number of interfaces: {num_interfaces}')

            abstract_count = num_abstract_classes + num_interfaces
            total_count = num_classes + num_abstract_classes + num_interfaces
            if (total_count == 0):
                print('No classes found for', folder_name)
                writer.writerow([folder_name, None])
            else:
                print(f'Abstractness: {abstract_count / total_count}')
                writer.writerow([folder_name, abstract_count / total_count])
