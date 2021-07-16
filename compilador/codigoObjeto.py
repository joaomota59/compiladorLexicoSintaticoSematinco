from goto import with_goto
@with_goto
def main():
	j=9
	k=10
	_t1=j%1.9
	k=_t1
	print("tk")
	_t2=5 > 4
	_t3=5 < 1
	_t4=_t2 and _t3
	if _t4 == False: goto ._l3
	_t5=3+2
	_t6=_t5+1
	_t7=_t6+3
	_t8=_t7+9
	_t9=4 < 3
	print(_t8,"oi",_t9)
	print("nice")
	_t10=3+5
	x=_t10
	a=input()
	a=float(a)
	print(a)
	_t11=5 > 2
	_t12= not _t11
	if _t12 == False: goto ._l1
	print("compiladores ou jubiladores?")
	label ._l1
	_t13=2 < 1
	if _t13 == False: goto ._l2
	print("ss")
	label ._l2
	label ._l3
	if msm == False: goto ._l4
	print("verdadeiro, deu bom")
	msm=True
	print(msm)
	goto ._l5
	label ._l4
	print("falso deu ruim")
	print("falso deu ruim")
	label ._l5
	label ._l7
	_t14=j <= 10
	_t15=5 > 2
	_t16=_t14 and _t15
	if _t16 == False: goto ._l6
	print(j)
	_t17=2+1
	j=_t17
	goto ._l7
	label ._l6
main()
