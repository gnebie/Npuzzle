
def copydbllist(lst):
	newlst = []
	for l in lst:
		newlst.append(list(l))
	return newlst




def test_tab_resolve_possibility(tabinitial, tabfinal):
	paires = 0
	tabfnbr = 0
	for t1 in tabfinal:
		tabinbr = 0
		if t1 == 0:
			continue ;
		for t2 in tabinitial:
			if t1 == t2:
				break
			if t1 < t2 and t2 != 0:
				# print("t1 ", t1, "    t2", t2)
				paires += 1
			tabinbr += 1
		tabfnbr += 1
	return ;
	if(paires & 1):
		print("find : ", paires)
		print("Taquin proposé impossible")
		exit(-1) #pair
	# else
	# impair
