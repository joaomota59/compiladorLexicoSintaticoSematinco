from goto import with_goto
@with_goto
def main():
	j=9
	k=10
	n=k
	print("tk")
	_t1=5 > 4
	_t2=5 < 1
	_t3=_t1 and _t2
	if _t3 == False: goto ._l3
	print("nice")
	a=input()
	a=float(a)
	_t4=5 > 2
	_t5= not _t4
	if _t5 == False: goto ._l1
	print("compiladores ou jubiladores?")
	label ._l1
	_t6=2 < 1
	if _t6 == False: goto ._l2
	print("ss")
	label ._l2
	label ._l3
	_t7=4 > 2
	_t8=5 < 6
	_t9=_t7 and _t8
	if _t9 == False: goto ._l4
	print("verdadeiro, deu bom")
	print(msm)
	goto ._l5
	label ._l4
	print("falso deu ruim")
	print("falso deu ruim")
	label ._l5
main()
