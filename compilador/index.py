# -*- coding: UTF-8 -*-
from typing import Type
from enum import Enum
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


def newLabel2():
    info = {"count": 0}
    def number():
        info["count"] += 1
        return info["count"]
    return number

newLabel = newLabel2()


code = []#lista global
symbol_table = {}
type_t_aux = {}
list_aux_decl = []
semantic_panic = False
tab = 0

class Types(Enum):
    INTEIRO = "inteiro"
    REAL = "real"
    Types_Exp = ["inteiro", "real"]
    CARACTERE = "caractere"
    LOGICO = "logico"

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
        return p.bloco
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
        return p.cmd
        #return p.cmd 
    
    @_('cmd ";" bloco')
    def bloco(self,p):
        return str(p.cmd) +';'+ str(p.bloco)
        #return p.bloco

    @_('cmdattrib')
    def cmd(self,p):
        return p.cmdattrib
    
    @_('cmdescrita')
    def cmd(self,p):
        return p.cmdescrita
    
    @_('cmdleitura')
    def cmd(self,p):
        return p.cmdleitura

    @_('cmdCondicao')
    def cmd(self,p):
        return p.cmdCondicao

    @_('LIMPATELA')
    def cmd(self,p):
        return p.LIMPATELA

    @_('cmdRepeticao')
    def cmd(self,p):
        return p.cmdRepeticao
    
    @_("ENQUANTO regraVazia expressaoRelacional FACA regraVazia bloco FIMENQUANTO")
    def cmdRepeticao(self,p):
        global code
        posExpRelacional = p.regraVazia0
        posEnquanto = p.regraVazia1 #tamanho do vetor antes do entao
        labelFalse = "_l"+str(newLabel())
        labelInicioLaco = "_l"+str(newLabel())
        code = code[:posExpRelacional]+['\tlabel .'+labelInicioLaco]+code[posExpRelacional:posEnquanto]+['\t'+"if "+p.expressaoRelacional+" == False: goto ."+labelFalse]+code[posEnquanto:]
        #insere o if depois da posicao do entao e o resto do vetor após a posicao do entao
        code.append('\tgoto .'+labelInicioLaco)
        code.append('\t'+'label'+' .'+labelFalse)
        return


    @_('LEIA "(" idAux ")" ')
    def cmdleitura(self,p):# AJUSTAR PARA CONVERTER PARA O TIPO CORRETO
        if not semantic_panic:
            auxVariaveis = p.idAux.split(',')
            for aux in auxVariaveis:
                k = "\t"+aux+"=input()"
                code.append(k)
                if(symbol_table[aux]==Types.INTEIRO.value):
                    code.append("\t"+aux+"=int("+aux+")")
                elif(symbol_table[aux]==Types.REAL.value):
                    code.append("\t"+aux+"=float("+aux+")")
                elif(symbol_table[aux]==Types.CARACTERE.value):
                    code.append("\t"+aux+"=str("+aux+")")
                elif symbol_table[aux]==Types.LOGICO.value:
                    code.append("\t"+aux+"=bool("+aux+")")
        return 
    
    @_('ID')
    def idAux(self,p):
        global semantic_panic
        
        if p.ID in symbol_table:
            return str(p.ID)
        
        print("Erro Semantico: Variavel " + p.ID + " nao declarada!")
        semantic_panic = True
        return 

    @_('ID "," idAux')
    def idAux(self,p):
        global semantic_panic
        
        if p.ID in symbol_table:
            return str(p.ID)+','+str(p.idAux)
        
        print("Erro Semantico: Variavel " + p.ID + " nao declarada!")
        semantic_panic = True
        return 

    @_(";")
    def regraVazia(self,p):#retorna o tamanho atual do vetor
        return len(code)#necessário para a regra semantica quando usa if

    @_('SE expressaoRelacional regraVazia ENTAO ";" bloco FIMSE')
    def cmdCondicao(self,p):
        global code
        posEntao = p.regraVazia #tamanho do vetor antes do entao
        labelFalse = "_l"+str(newLabel())

        code = code[:posEntao]+['\t'+"if "+p.expressaoRelacional+" == False: goto ."+labelFalse]+code[posEntao:]
        #insere o if depois da posicao do entao e o resto do vetor após a posicao do entao

        code.append('\t'+'label'+' .'+labelFalse)
        return

    @_("SE expressaoRelacional regraVazia ENTAO ';' bloco SENAO regraVazia bloco FIMSE")
    def cmdCondicao(self,p):
        global code
        posEntao = p.regraVazia0 #tamanho do vetor antes do entao
        posSenao = p.regraVazia1 #tamanho do vetor depois do senao [obs: podia ser antes tb]
        labelFalse = "_l"+str(newLabel())
        labelTrue = "_l"+str(newLabel())

        code = code[:posEntao]+['\t'+"if "+p.expressaoRelacional+" == False: goto ."+labelFalse]+code[posEntao:posSenao]+['\t'+'goto'+' .'+labelTrue]+['\t'+'label'+' .'+labelFalse]+code[posSenao:]+['\t'+'label'+' .'+labelTrue]
        return

    @_("expressaoRelacional OP_BOOL termoRelacional")
    def expressaoRelacional(self,p):
        a = p.expressaoRelacional
        b = p.termoRelacional
        var = "_t"+str(newTemp())
        if p.OP_BOOL == "e":
            code.append('\t'+var+"="+str(a)+" and "+str(b))
        elif p.OP_BOOL == "ou":
            code.append('\t'+var+"="+str(a)+" or "+str(b))
        return var
    
    @_("termoRelacional")
    def expressaoRelacional(self,p):
        return p.termoRelacional

    @_("expr OP_REL expr")
    def termoRelacional(self,p):
        type_t_aux.clear()
        a = p.expr0
        b = p.expr1
        var = "_t"+str(newTemp())
        if p.OP_REL == '<>':
            code.append('\t'+var+"="+str(a)+" != "+str(b))
        elif p.OP_REL == '=':
            code.append('\t'+var+"="+str(a)+" == "+str(b))
        else:
            code.append('\t'+var+"="+str(a)+" "+str(p.OP_REL)+" "+str(b))
        return var
    
    @_("exprC OP_REL exprC")
    def termoRelacional(self,p):
        type_t_aux.clear()
        a = p.exprC0
        b = p.exprC1
        var = "_t"+str(newTemp())
        if p.OP_REL == '<>':
            code.append('\t'+var+"="+str(a)+"!="+str(b))
        elif p.OP_REL == '=':
            code.append('\t'+var+"="+str(a)+"=="+str(b))
        else:
            code.append('\t'+var+"="+str(a)+" "+str(p.OP_REL)+" "+str(b))
        return var

    @_("NAO termoRelacional")
    def termoRelacional(self,p):
        var = "_t"+str(newTemp())
        if p.termoRelacional == "VERDADEIRO":
            code.append('\t'+var+"= not True")
            return var
        elif p.termoRelacional == "False":
            code.append('\t'+var+"= not False")
            return var
        else:
            code.append('\t'+var+"= not "+p.termoRelacional)
            return var



    @_("'(' termoRelacional ')'")
    def termoRelacional(self,p):
        return p.termoRelacional

    @_("ID")
    def termoRelacional(self,p):
        global semantic_panic
        if p.ID not in symbol_table:
            print("Erro Semantico: Variavel " + p.ID + " nao declarada!")
            semantic_panic = True
        return p.ID
    
    @_("VERDADEIRO")
    def termoRelacional(self,p):
        return "True"
    
    @_("FALSO")
    def termoRelacional(self,p):
        return "False"

    @_(" '(' expressaoRelacional ')' ")
    def termoRelacional(self,p):
        return p.expressaoRelacional

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

    @_('ID ASSIGN exprC')#comando atribuição para caractere
    def cmdattrib(self,p): 
        global semantic_panic

        typeExprC = self.get_type(p.exprC)
        type_t_aux.clear()

        if p.ID in symbol_table:
            typeID = self.get_type(p.ID)
            
            if typeID == typeExprC and typeID == Types.CARACTERE.value:
                code.append("\t"+p.ID+"="+str(p.exprC))
                return

            print("Erro Semantico: Variavel " + p.ID + " tem o tipo incompativel na operação!")
        else:  
            print("Erro Semantico: Variavel " + p.ID + " nao declarda!")

        semantic_panic = True
        return

    @_('ID ASSIGN expr')#comando atribuição para inteiro e real
    def cmdattrib(self,p):
        global semantic_panic

        typeExpr = self.get_type(p.expr)
        type_t_aux.clear()

        if p.ID in symbol_table:
            typeId = self.get_type(p.ID)
            
            if typeId == typeExpr or (typeId == Types.REAL.value and typeExpr == Types.INTEIRO.value):
                code.append("\t"+p.ID+"="+str(p.expr))
                return

            print("Erro Semantico: Variavel " + p.ID + " tem o tipo incompativel na operação!")

        else:  
            print("Erro Semantico: Variavel " + p.ID + " nao declarda!")

        semantic_panic = True
        return
    
    @_('ID ASSIGN expressaoRelacional')#comando atribuição para logico
    def cmdattrib(self,p):
        global semantic_panic
        if p.ID in symbol_table:
            type1 = self.get_type(p.ID)

            if type1 == Types.LOGICO.value:
                code.append("\t"+p.ID+"="+str(p.expressaoRelacional))
                return

            print("Erro Semantico: Variavel " + p.ID + " tem o tipo incompativel na operação!")
        else:  
            print("Erro Semantico: Variavel " + p.ID + " nao declarda!")

        semantic_panic = True
        return
        
    
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

    @_('exprC')
    def typeArgsEscritaAux(self,p):
        type_t_aux.clear()
        return p.exprC

    @_('expr')
    def typeArgsEscritaAux(self,p):
        type_t_aux.clear()
        return p.expr

    @_('expressaoRelacional')
    def typeArgsEscritaAux(self,p):
        return p.expressaoRelacional
    
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
        global semantic_panic
        a = p.expr0
        b = p.expr1
        type1 = self.get_type(a)
        type2 = self.get_type(b)
        
        if (type1 == type2) or (type1 in Types.Types_Exp.value and type2 in Types.Types_Exp.value):
            var = "_t"+str(newTemp())
            code.append('\t'+var+"="+str(a)+"+"+str(b))
            if type1 != type2:
                type1 = Types.REAL.value
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + str(a) + "+" + str(b) + "  de tipo incompativel!")
            semantic_panic = True
            return

    @_('expr "-" expr')
    def expr(self, p):
        global semantic_panic
        a = p.expr0
        b = p.expr1

        type1 = self.get_type(a)
        type2 = self.get_type(b)

        if type1 in Types.Types_Exp.value and type2 in Types.Types_Exp.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"="+str(a)+"-"+str(b))
            if type1 != type2:
                type1 = Types.REAL.value
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + str(a) + "+" + str(b) + "  de tipo incompativel!")
            semantic_panic = True
            return

    @_('expr "*" expr')
    def expr(self, p):
        global semantic_panic
        a = p.expr0
        b = p.expr1

        type1 = self.get_type(a)
        type2 = self.get_type(b)

        if type1 in Types.Types_Exp.value and type2 in Types.Types_Exp.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"="+str(a)+"*"+str(b))
            if type1 != type2:
                type1 = Types.REAL.value
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + str(a) + "*" + str(b) + "  de tipo incompativel!")
            semantic_panic = True
            return

    @_('expr "/" expr')
    def expr(self, p):
        global semantic_panic
        a = p.expr0
        b = p.expr1

        type1 = self.get_type(a)
        type2 = self.get_type(b)

        if type1 in Types.Types_Exp.value and type2 in Types.Types_Exp.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"="+str(a)+"/"+str(b))
            if type1 != type2:
                type1 = Types.REAL.value
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + str(a) + "/" + str(b) + "  de tipo incompativel!")
            semantic_panic = True
            return
    
    @_('expr "\\" expr')
    def expr(self, p):
        global semantic_panic
        a = p.expr0
        b = p.expr1

        type1 = self.get_type(a)
        type2 = self.get_type(b)

        if type1 in Types.Types_Exp.value and type2 in Types.Types_Exp.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"="+str(a)+"//"+str(b))
            if type1 != type2:
                type1 = Types.REAL.value
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + str(a) + "//" + str(b) + "  de tipo incompativel!")
            semantic_panic = True
            return
       
    @_('expr "%" expr')
    def expr(self, p):
        global semantic_panic
        a = p.expr0
        b = p.expr1

        type1 = self.get_type(a)
        type2 = self.get_type(b)

        if type1 in Types.Types_Exp.value and type2 in Types.Types_Exp.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"="+str(a)+"%"+str(b))
            if type1 != type2:
                type1 = Types.INTEIRO.value
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + str(a) + "%" + str(b) + "  de tipo incompativel!")
            semantic_panic = True
            return
    
    @_('expr MOD expr')
    def expr(self, p):
        global semantic_panic
        a = p.expr0
        b = p.expr1

        type1 = self.get_type(a)
        type2 = self.get_type(b)

        if type1 in Types.Types_Exp.value and type2 in Types.Types_Exp.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"="+str(a)+"%"+str(b))
            if type1 != type2:
                type1 = Types.INTEIRO.value
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + str(a) + "%" + str(b) + "  de tipo incompativel!")
            semantic_panic = True
            return
    
    @_('expr "^" expr')
    def expr(self, p):
        global semantic_panic
        a = p.expr0
        b = p.expr1

        type1 = self.get_type(a)
        type2 = self.get_type(b)

        if type1 in Types.Types_Exp.value and type2 in Types.Types_Exp.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"="+str(a)+"**"+str(b))
            if type1 != type2:
                type1 = Types.REAL.value
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + str(a) + "**" + str(b) + "  de tipo incompativel!")
            semantic_panic = True
            return
    
    @_('"+" expr %prec UPLUS')
    def expr(self, p):
        global semantic_panic
        a = p.expr

        type1 = self.get_type(a)

        if type1 in Types.Types_Exp.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"=""+"+str(a))
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + "+" + str(a) + "  de tipo incompativel!")
            semantic_panic = True
            return

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        global semantic_panic
        a = p.expr

        type1 = self.get_type(a)

        if type1 in Types.Types_Exp.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"=""-"+str(a))
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + "-" + str(a) + "  de tipo incompativel!")
            semantic_panic = True
            return

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
    def exprC(self, p):
        return p.exprC

    @_("exprC '+' exprC ")
    def exprC(self,p):
        global semantic_panic
        a = p.exprC0
        b = p.exprC1
        type1 = self.get_type(a)
        type2 = self.get_type(b)
        
        if type1 == type2 and type1 == Types.CARACTERE.value:
            var = "_t"+str(newTemp())
            code.append('\t'+var+"="+str(a)+"+"+str(b))
            type_t_aux[var] = type1
            return var
        else:
            print("Erro Semantico: Operacao" + str(a) + "+" + str(b) + "  de tipo incompativel!")
            semantic_panic = True
            return
        
    @_('ID')
    def exprC(self,p):
        global semantic_panic
        if p.ID not in symbol_table:
            print("Erro Semantico: Variavel " + p.ID + " nao declarada!")
            semantic_panic = True
        return p.ID
        
    
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

    def get_type(self, input):
        if input in symbol_table:#variavel declarada
            return symbol_table[input]
        else:
            if input in type_t_aux:
                return type_t_aux[input]
            elif type(input) == int:
                return Types.INTEIRO.value
            elif type(input) == float:
                return Types.REAL.value
            elif input == Types.CARACTERE.value: 
                return Types.CARACTERE.value



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
                auxiliar = i[:i.find('//')].lower() + ";" + i[i.find('//'):].lower()
                positionEntao = auxiliar.find('entao;')
                positionEnquanto = auxiliar.find('enquanto')
                if(positionEntao != -1):
                    data += auxiliar[:positionEntao]+';'+auxiliar[positionEntao:]
                elif(positionEnquanto!=-1):
                    data += auxiliar[:positionEnquanto]+';'+auxiliar[positionEnquanto:]
                else:
                    data+=auxiliar
            elif i.lower()=='fimalgoritmo': #ultima linha do arquivo
                data += i.lower() + ";"
            else:#é pq a linha nao tem comentário entao adiciona o ; antes do \n
                auxiliar = i[:-1].lower() + ";" + "\n"
                positionEnquanto = auxiliar.find('enquanto')+8
                if(auxiliar.find('entao;\n')!=-1):
                    data += auxiliar[:-7]+" ;"+auxiliar[-7:]
                elif(positionEnquanto!=-1 and auxiliar.find('faca;\n')!=-1 ):
                    data += auxiliar[:positionEnquanto]+';'+auxiliar[positionEnquanto:]
                else:
                    data+=auxiliar
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