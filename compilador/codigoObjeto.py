from goto import with_goto
@with_goto
def main():
	msm=True
	_t1=4 == 3
	_t2=5 > 3
	_t3=_t1 and _t2
	_t4=3 < 1
	_t5=_t3 or _t4
	print(_t5)
	print(msm)
	_t6=4%3
	_t7=55/2
	_t8=_t6+_t7
	_t9=_t8-55
	print(_t9,end='')
	_t10=4//3
	_t11=_t10%3
	_t12=_t11%4
	print(_t12)
	print("oi")
	_t13=-2
	print(_t13)
	_t14=+2
	print(_t14)
	_t15=4**2
	_t16=5+_t15
	_t17="oi"+"s"
	_t18=_t17+"joao"
	print(_t16,_t18)
	print(True,False)
	x=input()
	x=int(x)
	a=input()
	a=str(a)
	n=input()
	n=float(n)
main()
