from goto import with_goto
@with_goto
def main():
	_t1= not False
	_t2=4 < 3
	_t3=_t1 or _t2
	msm=_t3
	print(msm)
	_t4=4%3
	_t5=55/2
	_t6=_t4+_t5
	_t7=_t6-55
	print(_t7,end='')
	_t8=4//3
	_t9=_t8%3
	_t10=_t9%4
	print(_t10)
	print("oi")
	_t11=-2
	print(_t11)
	_t12=+2
	print(_t12)
	_t13=4**2
	_t14=5+_t13
	_t15="oi"+"s"
	_t16=_t15+"joao"
	print(_t14,_t16)
	print(True,False)
	x=input()
	x=int(x)
	a=input()
	a=str(a)
	n=input()
	n=float(n)
main()
