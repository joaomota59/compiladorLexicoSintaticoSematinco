from goto import with_goto
@with_goto
def main():
	xc="ola"
	_t1="sd"+xc
	_t2=_t1+"asdasdas"
	y=_t2
	_t3=5.23+3.4
	a=_t3
	b=4.3
	print("tk")
	_t4=5 > 4
	_t5=5 < 1
	_t6=_t4 and _t5
	if _t6 == False: goto ._l3
	_t7=3+2
	_t8=_t7+1
	_t9=_t8+3
	_t10=_t9+9
	_t11=4 < 3
	print(_t10,"oi",_t11)
	print("nice")
	_t12=3+5
	x=_t12
	a=input()
	a=float(a)
	print(a)
	_t13=5 > 2
	_t14= not _t13
	if _t14 == False: goto ._l1
	print("compiladores ou jubiladores?")
	label ._l1
	_t15=2 < 1
	if _t15 == False: goto ._l2
	print("ss")
	label ._l2
	label ._l3
	_t16=4 > 2
	_t17=5 < 6
	_t18=_t16 and _t17
	if _t18 == False: goto ._l4
	print("verdadeiro, deu bom")
	msm=True
	print(msm)
	goto ._l5
	label ._l4
	print("falso deu ruim")
	print("falso deu ruim")
	label ._l5
main()
