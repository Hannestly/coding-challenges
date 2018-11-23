import numpy as np

'''
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

'''
wordspace = [['F', 'A', 'C', 'I'],
             ['O', 'B', 'Q', 'P'],
             ['A', 'N', 'O', 'B'],
             ['M', 'A', 'S', 'S']]

word = list('FOAM')
wordspace = np.array(wordspace)


def find(wordspace, word):

    def match_vertical(wordspace, row, col, word):
        try:
            for i in range(len(word)):
                if wordspace[row+i, col] != word[i]:
                    return False
        except:
            return False
        return True

    def match_horizontal(wordspace, row, col, word):
        try:
            for i in range(len(word)):
                if wordspace[row, col+i] != word[i]:
                    return False
        except:
            return False
        return True

    for row_num in range(len(wordspace)):
        for col_num in range(len(wordspace[row_num])):
            if wordspace[row_num, col_num] == word[0]:
                if match_horizontal(wordspace, row_num, col_num, word):
                    return True
                if match_vertical(wordspace, row_num, col_num, word):
                    return True
    return False


print(find(wordspace, word))
