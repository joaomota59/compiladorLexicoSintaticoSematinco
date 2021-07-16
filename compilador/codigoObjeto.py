from goto import with_goto
@with_goto
def main():
	j=9
	k=10
	_t1=j+2
	_t2=_t1+j
	_t3=_t2+k
	j=_t3
	print("tk")
	_t4=5 > 4
	_t5=5 < 1
	_t6=_t4 and _t5
	if _t6 == False: goto ._l3
	print("nice")
	a=input()
	a=float(a)
	_t7=5 > 2
	_t8= not _t7
	if _t8 == False: goto ._l1
	print("compiladores ou jubiladores?")
	label ._l1
	_t9=2 < 1
	if _t9 == False: goto ._l2
	print("ss")
	label ._l2
	label ._l3
	_t10=4 > 2
	_t11=5 < 6
	_t12=_t10 and _t11
	if _t12 == False: goto ._l4
	print("verdadeiro, deu bom")
	msm=True
	print(msm)
	goto ._l5
	label ._l4
	print("falso deu ruim")
	print("falso deu ruim")
	label ._l5
main()
