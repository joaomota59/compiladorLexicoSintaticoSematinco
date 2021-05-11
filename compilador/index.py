#pip install sly
from sly import Lexer, Parser
import pprint


class VisualgLexer(Lexer):    

    # Set of token names.   This is always required
    tokens = {
    ALGORITMO,FIMALGORITMO,VAR,VERDADEIRO,FALSO,FUNCAO,FIMFUNCAO,ID,REAL,INTEIRO,
    CARACTERE,LOGICO, SE, ENTAO,SENAO,FIMSE,ENQUANTO,FACA,REPITA,FIMREPITA,
    FIMENQUANTO,ESCREVA,ESCREVAL,E,OU,NAO,LEIA, LIMPATELA, PROCEDIMENTO,
    FIMPROCEDIMENTO, ESCOLHA, FIMESCOLHA, VETOR, ASC, TIMER, CARAC, ECO,
    LE, LT ,GE, GT,EQ, NE, ASSIGN,MOD, RETORNE, POS, XOU, CRONOMETRO,INICIO
    }#Nome dos tokens devem estar em maiusculo
    #O valor de cada chave desse dicionario sera definido durante a execução

    literals = {'+','-','*','/','^','(', ')', ',',':', '\\', '%'} #caracteres literais, o token é representado pelo proprio simbolo


    ###Caracteres Ignorados###

    ###As variáveis que começam com o nome ignore, serão ignoradas pelo analisador léxico
    # String containing ignored characters between tokens
    ignore = ' \t'#ignora espaços entre os tokens
    ignore_comment = r'([//].+)' #ignora as linhas que são comentáriosc
    ignore_newline = r'\n+'  #ignora varias linhas vazias
    ####################################################

    # Regular expression rules for tokens -- Aqui será definido as expressoes regulares que caracterizam os tokens definidos antes
    REAL = r'(real|[0-9]+[.][0-9]*)'#se for a palavra reservada ou (um conjunto de digitos . conjunto de digitos) é do tipo real
    INTEIRO = r'(inteiro|[0-9]+)' #se for a palavra reservada ou um conjunto de digitos é do tipo inteiro
    CARACTERE = r'(caractere|"[^\n]+"|"")'#se for a palavra reservada ou qualquer coisa que n seja \n no texto entao é caracter
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*' #variavel que começa com alguma letra maiuscula ou minuscula
    NE      = r'<>' #diferença - not equal
    ASSIGN  = r'<-' #atribuição
    LE      = r'<=' #menor que
    LT      = r'<'  #menor
    GE      = r'>=' #maior que
    GT      = r'>'  #maior
    EQ     = r'==' #comparação
    

    # Caracteres especiais / palavras reservadas / Definir todas aqui na parte de remapeamento de token
    ID['Var'] = VAR
    ID['Inicio'] = INICIO
    ID['Fimalgoritmo'] = FIMALGORITMO
    ID['MOD'] = MOD
    ID['Algoritmo'] = ALGORITMO
    ID['verdadeiro'] = VERDADEIRO
    ID['falso'] = FALSO
    ID['funcao'] = FUNCAO
    ID['fimfuncao'] = FIMFUNCAO
    ID['procedimento'] = PROCEDIMENTO
    ID['fimprocedimento'] = FIMPROCEDIMENTO
    ID['escolha'] = ESCOLHA
    ID['fimescolha'] = FIMESCOLHA
    ID['repita'] = REPITA
    ID['fimrepita'] = FIMREPITA
    ID['enquanto'] = ENQUANTO
    ID['faca'] = FACA
    ID['fimenquanto'] = FIMENQUANTO
    ID['limpatela'] = LIMPATELA
    ID['se'] = SE
    ID['entao'] = ENTAO
    ID['senao'] = SENAO
    ID['fimse'] = FIMSE
    ID['escreva'] = ESCREVA
    ID['escreval'] = ESCREVAL
    ID['logico'] = LOGICO
    ID['e'] = E 
    ID['ou'] = OU
    ID['nao'] = NAO
    ID['leia'] = LEIA
    ID['vetor'] = VETOR
    ID['retorne'] = RETORNE
    ID['pos'] = POS
    ID['xou'] = XOU
    ID['cronometro'] = CRONOMETRO
    ID['asc'] = ASC
    ID['timer'] = TIMER
    ID['carac'] = CARAC
    ID['eco'] = ECO

    # Define a rule so we can track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):#função que auxilia a funcao error(contando as linhas do algoritmo), no qual irá mostrar qual linha que dá erro lexico 
        self.lineno += len(t.value)
    def error(self, t):#funçãoq que mostra erro lexico na linha do algoritmo dado como entrada
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


    @_(r'[0-9]+[.][0-9]*')
    def REAL(self,t):
        t.value = float(t.value)   # Converte para um valor real
        return t

    @_(r'[0-9]+')
    def INTEIRO(self, t):
        t.value = int(t.value)   # Converte para um valor inteiro
        return t


class VisualgParser(Parser):
    tokens = VisualgLexer.tokens

 #Regras gramaticais para numeros inteiros
    @_('expr "+" term')
    def expr(self, p):
        #return
        return p.expr + p.term

    @_('expr "-" term')
    def expr(self, p):
        #return
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        #return
        return p.term

    @_('factor')
    def term(self, p):
        #return
        return p.factor

    @_('REAL')
    def factor(self, p):
        #return
        return p.REAL
    @_('INTEIRO')
    def factor(self, p):
        #return
        return p.INTEIRO
    @_('"(" expr ")"')
    def factor(self, p):
        return p.expr
###OBS FALTA DIVISAO ENTRE REAL!!




if __name__ == '__main__':
    arquivo = open('algoritmo.txt', 'r')
    data = arquivo.read()
    arquivo.close()
    lexer = VisualgLexer()
    parser = VisualgParser()
    resultado = parser.parse(lexer.tokenize(data))
    pprint.pprint(resultado)
    #for tok in lexer.tokenize(data):
    #    print('type=%r, value=%r' % (tok.type, tok.value))
    