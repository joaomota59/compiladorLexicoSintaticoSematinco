# -*- coding: UTF-8 -*-
from sly import Lexer, Parser #pip install sly
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

    literals = {'+','-','*','/','^','(', ')', ',',':', '\\', '%',';'} #caracteres literais, o token é representado pelo proprio simbolo


    ###Caracteres Ignorados###

    ###As variáveis que começam com o nome ignore, serão ignoradas pelo analisador léxico
    # String containing ignored characters between tokens
    ignore = ' \t'#ignora espaços entre os tokens
    ignore_comment = r'(//.*)' #ignora as linhas que são comentários
    #ignore_newline = r'\n+'  #ignora varias linhas vazias
    ####################################################

    # Regular expression rules for tokens -- Aqui será definido as expressoes regulares que caracterizam os tokens definidos antes

    
    REAL = r'(real|[0-9]+[.][0-9]*)'#se for a palavra reservada ou (um conjunto de digitos . conjunto de digitos) é do tipo real
    INTEIRO = r'(inteiro|[0-9]+)' #se for a palavra reservada ou um conjunto de digitos é do tipo inteiro
    CARACTERE = r'(caractere|"[^\n]*")'#se for a palavra reservada ou qualquer coisa que n seja \n no texto entao é caracter
    ID      =   r'[a-zA-Z_][a-zA-Z0-9_]*' #variavel que começa com alguma letra maiuscula ou minuscula
    NE      = r'<>' #diferença - not equal
    ASSIGN  = r'<-' #atribuição
    LE      = r'<=' #menor que
    LT      = r'<'  #menor
    GE      = r'>=' #maior que
    GT      = r'>'  #maior
    EQ      = r'=' #comparação
    

    # Caracteres especiais / palavras reservadas / Definir todas aqui na parte de remapeamento de token
    ID['var'] = VAR
    ID['inicio'] = INICIO
    ID['fimalgoritmo'] = FIMALGORITMO
    ID['mod'] = MOD
    ID['algoritmo'] = ALGORITMO
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
    @_(r'\n+')#ignora linhas com \n
    def ignore_newline(self, t):#função que auxilia a funcao error(contando as linhas do algoritmo), no qual irá mostrar qual linha que dá erro lexico 
        self.lineno += t.value.count('\n')
    def error(self, t):#funçãoq que mostra erro lexico na linha do algoritmo dado como entrada
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


    @_(r'[0-9]+[.][0-9]*')
    def REAL(self,t):
        try:
            t.value = float(t.value)   # Converte para um valor real
        except ValueError:
            pass
        return t

    @_(r'[0-9]+')
    def INTEIRO(self, t):
        try:
            t.value = int(t.value)   # Converte para um valor inteiro
        except ValueError:
            pass
        return t


class VisualgParser(Parser):
    debugfile = 'parser.out' #arquivo de debugação do Parser
    tokens = VisualgLexer.tokens
    precedence = (#precedencia, os que ficam mais abaixo tem a maior precedencia
       ('nonassoc',NE,LE,LT,GE,GT,EQ),  # Nonassociative operators
       ('left', '+', '-'),#LEVEL 0
       ('left', '*','/','\\','%',MOD),#LEVEL 1
       ('right','^'),#LEVEL 2
       ('right', 'UMINUS','UPLUS'),#Operadores unários de maiores precedência
    )
    

    #Regras gramaticais:

    @_("ALGORITMO CARACTERE ';' VAR ';' declaracaoType INICIO ';'  blocoType FIMALGORITMO ';' ")
    def initial(self,p):
        return
        #return p.blocoType

    @_("bloco")
    def blocoType(self,p):
        return
        #return p.bloco
    
    @_("")
    def blocoType(self,p):
        return

    @_("declaracaoTypeAux")
    def declaracaoType(self,p):
        return

    @_("")
    def declaracaoType(self,p):
        return

    @_("declaracao ';' declaracaoTypeAux")
    def declaracaoTypeAux(self,p):
        return
    
    @_("declaracao ';' ")
    def declaracaoTypeAux(self,p):
        return
    
    @_("vartype ':' INTEIRO")
    def declaracao(self,p):
        return
    
    @_("vartype ':' REAL")
    def declaracao(self,p):
        return
    
    @_("vartype ':' CARACTERE")
    def declaracao(self,p):
        return
    
    @_("vartype ':' LOGICO")
    def declaracao(self,p):
        return
    

    @_("ID")
    def vartype(self,p):
        return

    @_("ID ',' vartype")
    def vartype(self,p):
        return

    @_('cmd ";" ')
    def bloco(self,p):
        return
        #return p.cmd 
    
    @_('cmd ";" bloco')
    def bloco(self,p):
        return
        #return p.bloco

    @_('cmdattrib')
    def cmd(self,p):
        return
        #return p.cmdattrib
    
    @_('cmdescrita')
    def cmd(self,p):
        return
        #return p.cmdescrita
    
    @_('cmdleitura')
    def cmd(self,p):
        return
        # return p.cmdleitura

    @_('cmdCondicao')
    def cmd(self,p):
        return

    @_('LIMPATELA')
    def cmd(self,p):
        return

    @_('cmdRepeticao')
    def cmd(self,p):
        return
    
    @_("ENQUANTO expressaoRelacional FACA ';' bloco FIMENQUANTO")
    def cmdRepeticao(self,p):
        return
    
    @_('LEIA "(" ID ")" ')
    def cmdleitura(self,p):
        return
    
    @_('SE expressaoRelacional ENTAO ";" bloco FIMSE')
    def cmdCondicao(self,p):
        return

    @_("SE expressaoRelacional ENTAO ';' bloco SENAO ';' bloco FIMSE")
    def cmdCondicao(self,p):
        return

    @_("expressaoRelacional OP_BOOL termoRelacional")
    def expressaoRelacional(self,p):
        return
    
    @_("termoRelacional")
    def expressaoRelacional(self,p):
        return

    @_("expr OP_REL expr")
    def termoRelacional(self,p):
        return

    @_("NAO termoRelacional")
    def termoRelacional(self,p):
        return
    
    @_("VERDADEIRO")
    def termoRelacional(self,p):
        return
    
    @_("FALSO")
    def termoRelacional(self,p):
        return

    @_(" '(' expressaoRelacional ')' ")
    def termoRelacional(self,p):
        return

    @_("E")
    def OP_BOOL(self,p):
        return
    
    @_("OU")
    def OP_BOOL(self,p):
        return

    @_("XOU")
    def OP_BOOL(self,p):
        return

    @_("NE")
    def OP_REL(self,p):
        return
    
    @_("LE")
    def OP_REL(self,p):
        return

    @_("LT")
    def OP_REL(self,p):
        return

    @_("GE")
    def OP_REL(self,p):
        return

    @_("GT")
    def OP_REL(self,p):
        return

    @_("EQ")
    def OP_REL(self,p):
        return

    @_('ID ASSIGN expr')#comando atribuição
    def cmdattrib(self,p):
        return
    
    @_('ID ASSIGN typeArgs')#comando atribuição
    def cmdattrib(self,p):
        return

    @_('ID ASSIGN "(" typeArgs ")"')#comando atribuição
    def cmdattrib(self,p):
        return

    @_('VERDADEIRO')
    def typeArgs(self,p):
        return

    @_('FALSO')
    def typeArgs(self,p):
        return
    
    @_('ESCREVA "(" typeArgsEscrita ")" ')#comando escrita
    def cmdescrita(self, p):
        return

    @_('ESCREVA "(" ")" ')#comando escrita
    def cmdescrita(self, p):
        return

    @_('expr')
    def typeArgsEscritaAux(self,p):
        return
    
    @_('typeArgs')
    def typeArgsEscritaAux(self,p):
        return

    @_('typeArgsEscrita "," typeArgsEscritaAux')
    def typeArgsEscrita(self,p):
        return

    @_('typeArgsEscritaAux')
    def typeArgsEscrita(self,p):
        return

    
    @_('ESCREVAL "(" typeArgsEscrita ")" ')#comando escrita
    def cmdescrita(self, p):
        return 

    @_('ESCREVAL "(" ")" ')#comando escrita
    def cmdescrita(self, p):
        return
    
    @_('"(" expr ")"')
    def expr(self, p):
        return

    @_('expr "+" expr')
    def expr(self, p):
        return
        #return p.expr0 + p.expr1

    @_('expr "-" expr')
    def expr(self, p):
        return
        #return p.expr0 - p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return
        #return p.expr0 * p.expr1

    @_('expr "/" expr')
    def expr(self, p):
        return
        #return p.expr0 / p.expr1
    
    @_('expr "\\" expr')
    def expr(self, p):
        return
        #return p.expr0//p.expr1
    
    @_('expr "%" expr')
    def expr(self, p):
        return
        #return p.expr0%p.expr1
    
    @_('expr MOD expr')
    def expr(self, p):
        return
        #return p.expr0%p.expr1
    
    @_('expr "^" expr')
    def expr(self, p):
        return
        #return p.expr0**p.expr1
    
    @_('"+" expr %prec UPLUS')
    def expr(self, p):
        return
        #return -p.expr

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return
        #return -p.expr

    @_('INTEIRO')
    def expr(self, p):
        return
        #return p.INTEIRO

    @_('REAL')
    def expr(self, p):
        return
        #return p.REAL
    
    @_('ID')
    def expr(self, p):
        return
    
    @_('CARACTERE')
    def expr(self, p):
        return
        #return p.ID

    def error(self, p):#só entra aqui se der algum erro de sintaxe
        if p:#se entrar aqui mostra o erro de sintaxe que deu, mostrando a linha do erro, dentre outras informações
            print("Syntax error at token", p)
            # Just discard the token and tell the parser it's okay.
            self.restart() # descarta toda a pilha de análise e redefine o analisador para seu estado inicial.
        else:
            print("Syntax error at EOF")



if __name__ == '__main__':
    arquivo = open('algoritmo.txt', 'r')
    #data = arquivo.read().lower() #converte o algoritmo.txt todo para minusuculo pois o Visual n diferencia maiuscula de minuscula
    data = ''
    linhas = arquivo.readlines()
    #print(linhas)
    for i in linhas:
        if i != '\n':#se nao for uma linha vazia
            if (i.find('//') != -1):#se a linha tiver comentario coloca o ponto e virgula antes do comentario, pq o comentario será ignorado pelo regex
                data += i[:i.find('//')].lower() + ";" + i[i.find('//'):].lower()
            elif i.lower()=='fimalgoritmo': #ultima linha do arquivo
                data += i.lower() + ";"
            else:#é pq a linha nao tem comentário entao adiciona o ; antes do \n
                data += i[:-1].lower() + ";" + "\n"
        else:#entao é uma linha vazia
            data += i
    #print(data)
    arquivo.close()
    lexer = VisualgLexer()
    parser = VisualgParser()
    resultado = parser.parse(lexer.tokenize(data))
    if resultado != None: 
        pprint.pprint(resultado)

    arquivo2 = open("tokens.txt","w")
    
    for tok in lexer.tokenize(data):
        arquivo2.write(str(tok)+"\n")
    arquivo2.close()