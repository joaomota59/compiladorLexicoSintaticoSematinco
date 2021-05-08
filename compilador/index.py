#pip install sly
from sly import Lexer

class CalcLexer(Lexer):

    # Set of token names.   This is always required
    tokens = { ID, IF, ELSE, PRINT, WHILE, NUMBER, LE, LT ,GE, GT,EQ, NE, ASSIGN }#Nome dos tokens devem estar em maiusculo

    literals = { '+','-','*','/','(', ')', '{', '}', ';' } #caracteres literais o token é representado pelo proprio simbolo


    ###Caracteres Ignorados###

    ###As variáveis que começam com o nome ignore, serão ignoradas pelo analisador léxico
    # String containing ignored characters between tokens
    ignore = ' \t'
    # Other ignored patterns
    ignore_comment = r'\#.*' #ignora comentário de linha
    ignore_newline = r'\n+'  #ignora varias linhas vazias
    ####################################################

    # Regular expression rules for tokens -- Aqui será definido as expressoes regulares que caracterizam os tokens definidos antes
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    LE      = r'<='
    LT      = r'<'
    GE      = r'>='
    GT      = r'>'
    NUMBER  = r'\d+'
    EQ     = r'==' 
    ASSIGN  = r'='
    NE      = r'!='

    # Caracteres especiais
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['print'] = PRINT

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
    data = 'j = 3 + 42 * (if - t)'
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))