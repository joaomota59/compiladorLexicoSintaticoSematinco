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
	ks=3
	j=34
	_t4=j+1
	j=_t4
	print("tk")
	_t5=5 > 4
	_t6=5 < 1
	_t7=_t5 and _t6
	if _t7 == False: goto ._l3
	_t8=3+2
	_t9=_t8+1
	_t10=_t9+3
	_t11=_t10+9
	_t12=4 < 3
	print(_t11,"oi",_t12)
	print("nice")
	_t13=3+5
	x=_t13
	a=input()
	a=float(a)
	print(a)
	_t14=5 > 2
	_t15= not _t14
	if _t15 == False: goto ._l1
	print("compiladores ou jubiladores?")
	label ._l1
	_t16=2 < 1
	if _t16 == False: goto ._l2
	print("ss")
	label ._l2
	label ._l3
	_t17=4 > 2
	_t18=5 < 6
	_t19=_t17 and _t18
	if _t19 == False: goto ._l4
	print("verdadeiro, deu bom")
	msm=True
	print(msm)
	goto ._l5
	label ._l4
	print("falso deu ruim")
	print("falso deu ruim")
	label ._l5
	label ._l7
	_t20=j <= 10
	_t21=5 > 2
	_t22=_t20 and _t21
	if _t22 == False: goto ._l6
	print(j)
	_t23=2+1
	j=_t23
	goto ._l7
	label ._l6
main()
