from goto import with_goto
@with_goto
def main():
	j=1
	p=3.3
	print("entao")
	_t1=3 > 2
	if _t1 == False: goto ._l1
	label ._l1
	label ._l5
	_t2=j <= 10
	_t3=5 > 2
	_t4=_t2 and _t3
	if _t4 == False: goto ._l4
	_t5=j < 4
	if _t5 == False: goto ._l2
	print(j)
	goto ._l3
	label ._l2
	print("outro",j)
	label ._l3
	_t6=j+1
	j=_t6
	goto ._l5
	label ._l4
main()
