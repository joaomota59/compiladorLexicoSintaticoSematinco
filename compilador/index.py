# -*- coding: UTF-8 -*-
from typing import Type
from sly import Lexer, Parser #pip install sly
import pprint
import sys #leitura de arquivo


class VisualgLexer(Lexer):    

    # Set of token names.   This is always required
    tokens = {
    ALGORITMO,FIMALGORITMO,VAR,VERDADEIRO,FALSO,ID,REAL,INTEIRO,
    CARACTERE,LOGICO, SE, ENTAO,SENAO,FIMSE,ENQUANTO,FACA,
    FIMENQUANTO,ESCREVA,ESCREVAL,E,OU,NAO,LEIA, LIMPATELA,
    LE, LT ,GE, GT,EQ, NE, ASSIGN,MOD,INICIO
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
    CARACTERE = r'(caractere|(\'.*?\'|".*?"))'#se for a palavra reservada ou qualquer coisa que n seja \n no texto entao é caracter
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

def newTemp2():
    info = {"count": 0}
    def number():
        info["count"] += 1
        return info["count"]
    return number

newTemp = newTemp2()


code = []#lista global
symbol_table = {}
list_aux_decl = []
semantic_panic = False

class VisualgParser(Parser):
    debugfile = 'parser.out' #arquivo de debugação do Parser
    tokens = VisualgLexer.tokens

    precedence = (#precedencia, os que ficam mais abaixo tem a maior precedencia
       ('nonassoc',NE,LE,LT,GE,GT,EQ,'E','OU'),  # Nonassociative operators
       ('left', '+', '-'),#LEVEL 0
       ('left', '*','/','\\','%',MOD),#LEVEL 1
       ('right','^'),#LEVEL 2
       ('right', 'UMINUS','UPLUS'),#Operadores unários de maiores precedência
    )
    
    

    #Regras gramaticais:

    @_("ALGORITMO CARACTERE ; varAux INICIO ';'  blocoType FIMALGORITMO ';' ")
    def initial(self,p):
        if not semantic_panic:
            code.append("main()")
            code.insert(0,"def main():")
            code.insert(0,"@with_goto")
            code.insert(0,"from goto import with_goto")
    
            codigoObjeto = open("codigoObjeto.py","w")
            for i in code:
                codigoObjeto.write(i+"\n")
            codigoObjeto.close()
        return
    
    @_("")
    def varAux(self,p):
        return

    @_(" VAR ';' declaracaoType")
    def varAux(self,p):
        return

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
        self.single_decl_semantic_final(p.INTEIRO)
        return
    
    @_("vartype ':' REAL")
    def declaracao(self,p):
        self.single_decl_semantic_final(p.REAL)
        return
    
    @_("vartype ':' CARACTERE")
    def declaracao(self,p):
        self.single_decl_semantic_final(p.CARACTERE)
        return
    
    @_("vartype ':' LOGICO")
    def declaracao(self,p):
        self.single_decl_semantic_final(p.LOGICO)
        return
    
    @_("ID")
    def vartype(self,p):
        self.single_decl_semantic(p.ID)
        return p.ID

    @_("ID ',' vartype")
    def vartype(self,p):
        self.single_decl_semantic(p.ID)
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


    @_('LEIA "(" idAux ")" ')
    def cmdleitura(self,p):# AJUSTAR PARA CONVERTER PARA O TIPO CORRETO
        aux = p.idAux
        if(p.idAux.find(',')!=-1):
            k = "\t"+aux+"=[str(x) for x in input().split(',')]"
            code.append(k)
            auxVariaveis = p.idAux.split(',')
            for aux in auxVariaveis:
                if(symbol_table[aux]=="inteiro"):
                    code.append("\t"+aux+"=int("+aux+")")
                elif(symbol_table[aux]=="real"):
                    code.append("\t"+aux+"=float("+aux+")")
                elif(symbol_table[aux]=="caractere"):
                    code.append("\t"+aux+"=str("+aux+")")
                elif symbol_table[aux]=="logico":
                    code.append("\t"+aux+"=bool("+aux+")")
        else:
            k = "\t"+aux+"=input()"
            code.append(k)
            if(symbol_table[aux]=="inteiro"):
                code.append("\t"+aux+"=int("+aux+")")
            elif(symbol_table[aux]=="real"):
                code.append("\t"+aux+"=float("+aux+")")
            elif(symbol_table[aux]=="caractere"):
                code.append("\t"+aux+"=str("+aux+")")
            elif symbol_table[aux]=="logico":
                code.append("\t"+aux+"=bool("+aux+")") 
        return 
    
    @_('ID')
    def idAux(self,p):
        symbol_table[p.ID]#verifica se tem o elemento na tabela de simbolos
        return str(p.ID)

    @_('ID "," idAux')
    def idAux(self,p):
        symbol_table[p.ID]#verifica se tem o elemento na tabela de simbolos
        return str(p.ID)+','+str(p.idAux)


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
    
    @_("exprC OP_REL exprC")
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
        return p.E
    
    @_("OU")
    def OP_BOOL(self,p):
        return p.OU

    @_("NE")
    def OP_REL(self,p):
        return p.NE
    
    @_("LE")
    def OP_REL(self,p):
        return p.LE

    @_("LT")
    def OP_REL(self,p):
        return p.LT

    @_("GE")
    def OP_REL(self,p):
        return p.GE

    @_("GT")
    def OP_REL(self,p):
        return p.GT

    @_("EQ")
    def OP_REL(self,p):
        return p.EQ

    @_('ID ASSIGN expr')#comando atribuição
    def cmdattrib(self,p):
        global semantic_panic
        
        if p.ID not in symbol_table:
            print("Erro Semantico: Variavel " + p.ID + " nao declarada!")
            semantic_panic = True
        
        return
    
    @_('ID ASSIGN exprC')#comando atribuição
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
        return "True"

    @_('FALSO')
    def typeArgs(self,p):
        return "False"

    @_("expr OP_REL expr")
    def typeArgs(self,p):
        return str(p.expr0) + str(p.OP_REL) + str(p.expr1)
    
    @_("exprC OP_REL exprC")
    def typeArgs(self,p):
        return str(p.exprC0) + str(p.OP_REL) + str(p.exprC1)
    
    @_('ESCREVA "(" typeArgsEscrita ")" ')#comando escrita
    def cmdescrita(self, p):
        aux = p.typeArgsEscrita
        k = "\tprint("+aux+",end='')"
        code.append(k)
        return

    @_('ESCREVA "(" ")" ')#comando escrita
    def cmdescrita(self, p):
        code.append("\tprint(end='')")#print sem quebra de linha
        return

    @_('expr')
    def typeArgsEscritaAux(self,p):
        return p.expr
    
    @_('exprC')
    def typeArgsEscritaAux(self,p):
        return p.exprC
    
    @_('typeArgs')
    def typeArgsEscritaAux(self,p):
        return p.typeArgs

    @_('typeArgsEscrita "," typeArgsEscritaAux')
    def typeArgsEscrita(self,p):
        return p.typeArgsEscrita + "," + p.typeArgsEscritaAux

    @_('typeArgsEscritaAux')
    def typeArgsEscrita(self,p):
        return p.typeArgsEscritaAux

    
    @_('ESCREVAL "(" typeArgsEscrita ")" ')#comando escrita
    def cmdescrita(self, p):
        aux = p.typeArgsEscrita
        k = "\tprint("+aux+")"
        code.append(k)
        return

    @_('ESCREVAL "(" ")" ')#comando escrita
    def cmdescrita(self, p):
        code.append("\tprint()")#print com \n
        return
    
    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('expr "+" expr')
    def expr(self, p):#tipo, valor, nome da variavel temp
        a = p.expr0
        b= p.expr1
        var = "_t"+str(newTemp())
        code.append('\t'+var+"="+str(a)+"+"+str(b))
        return var
        '''
        try:
            return p.expr0 + p.expr1
        except Exception as e:#operadores que não são permitidos para somar cai aqui
            print(e)
            return
        '''


    @_('expr "-" expr')
    def expr(self, p):
        a = p.expr0
        b= p.expr1
        var = "_t"+str(newTemp())
        code.append('\t'+var+"="+str(a)+"-"+str(b))
        return var
        '''
        try:
            return p.expr0 - p.expr1
        except Exception as e:
            print(e)
            return
        '''

    @_('expr "*" expr')
    def expr(self, p):
        a = p.expr0
        b= p.expr1
        var = "_t"+str(newTemp())
        code.append('\t'+var+"="+str(a)+"*"+str(b))
        return var
        '''
        try:
            return p.expr0 * p.expr1
        except Exception as e:
            print(e)
            return
        '''

    @_('expr "/" expr')
    def expr(self, p):
        a = p.expr0
        b= p.expr1
        var = "_t"+str(newTemp())
        code.append('\t'+var+"="+str(a)+"/"+str(b))
        return var
        '''
        try:
            return p.expr0 / p.expr1
        except Exception as e:
            print(e)
            return
        '''
    
    @_('expr "\\" expr')
    def expr(self, p):
        a = p.expr0
        b= p.expr1
        var = "_t"+str(newTemp())
        code.append('\t'+var+"="+str(a)+"//"+str(b))#divisao inteira em python
        return var
        '''
        try:
            return p.expr0//p.expr1
        except Exception as e:
            print(e)
            return
        '''

    
    @_('expr "%" expr')
    def expr(self, p):
        a = p.expr0
        b= p.expr1
        var = "_t"+str(newTemp())
        code.append('\t'+var+"="+str(a)+"%"+str(b))#resto da divisao inteira em python
        return var
        '''
        try:
            return p.expr0%p.expr1
        except Exception as e:
            print(e)
            return
        '''
    
    @_('expr MOD expr')
    def expr(self, p):
        a = p.expr0
        b= p.expr1
        var = "_t"+str(newTemp())
        code.append('\t'+var+"="+str(a)+"%"+str(b))#resto da divisao inteira em python
        return var
        '''try:
            return p.expr0%p.expr1
        except Exception as e:
            print(e)
        '''
    
    @_('expr "^" expr')
    def expr(self, p):
        a = p.expr0
        b= p.expr1
        var = "_t"+str(newTemp())
        code.append('\t'+var+"="+str(a)+"**"+str(b))#exponenciação no python
        return var
        '''try:
            return p.expr0**p.expr1
        except Exception as e:
            print(e)
        '''
    
    @_('"+" expr %prec UPLUS')
    def expr(self, p):
        a = p.expr
        var = "_t"+str(newTemp())
        code.append('\t'+var+"=""+"+str(a))#operação unária no python com +
        return var
        '''try:
            return +p.expr
        except Exception as e:
            print(e)
        '''

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        a = p.expr
        var = "_t"+str(newTemp())
        code.append('\t'+var+"=""-"+str(a))#operação unária no python com -
        return var
        '''try:
            return -p.expr
        except Exception as e:
            print(e)
        '''

    @_('INTEIRO')
    def expr(self, p):
        return p.INTEIRO
        #return int(p.INTEIRO)

    @_('REAL')
    def expr(self, p):
        return p.REAL
        #return float(p.REAL)
    
    @_('ID')
    def expr(self, p):
        global semantic_panic
        
        if p.ID not in symbol_table:
            print("Erro Semantico: Variavel " + p.ID + " nao declarada!")
            semantic_panic = True
        
        return p.ID

    @_('"(" exprC ")"')
    def expr(self, p):
        return p.exprC

    @_("exprC '+' exprC ")
    def exprC(self,p):
        a = p.exprC0
        b= p.exprC1
        var = "_t"+str(newTemp())
        code.append('\t'+var+"="+str(a)+"+"+str(b))
        return var
    
    @_('CARACTERE')
    def exprC(self,p):
        return p.CARACTERE
    
    def error(self, p):#só entra aqui se der algum erro de sintaxe
        if p:#se entrar aqui mostra o erro de sintaxe que deu, mostrando a linha do erro, dentre outras informações
            print("Syntax error at token", p)
            # Just discard the token and tell the parser it's okay.
            self.restart() # descarta toda a pilha de análise e redefine o analisador para seu estado inicial.
        else:
            print("Syntax error at EOF")
    
    def single_decl_semantic(self, value):
        list_aux_decl.append(value)

    def single_decl_semantic_final(self, type):
        global semantic_panic

        for var in list_aux_decl:
            if var in symbol_table:
                print("Erro Semantico: Variavel " + var + " ja declarada")
                semantic_panic = True
            else:
                symbol_table[var] = type

        list_aux_decl.clear()




if __name__ == '__main__':
    entrada = sys.argv[1]
    arquivo = open(entrada, 'r')
    #data = arquivo.read().lower() #converte o algoritmo.txt todo para minusuculo pois o Visual n diferencia maiuscula de minuscula
    data = ''
    linhas = arquivo.readlines()
    #print(linhas)
    for i in linhas:
        if i != '\n':#se nao for uma linha vazia
            if (i.find('//') != -1 and i.find('//')!=0):#se a linha tiver comentario coloca o ponto e virgula antes do comentario, pq o comentario será ignorado pelo regex
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

    '''for tok in lexer.tokenize(data):
        print(tok.type, tok.value)'''

    
    resultado = parser.parse(lexer.tokenize(data))

    if resultado != None: 
        pprint.pprint(resultado)

    arquivo2 = open("tokens.txt","w")
    
    for tok in lexer.tokenize(data):
        arquivo2.write(str(tok)+"\n")
    arquivo2.close()