

def test_switch(tab, controle):
	tab.printtab()
	controle.switch_right(tab.lines)
	tab.printtab()
	controle.switch_down(tab.lines)
	tab.printtab()
	controle.switch_right(tab.lines)
	tab.printtab()
	controle.switch_down(tab.lines)
	tab.printtab()
	controle.switch_right(tab.lines)
	tab.printtab()
	controle.switch_down(tab.lines)
	tab.printtab()
	controle.switch_right(tab.lines)
	tab.printtab()
	controle.switch_down(tab.lines)
	tab.printtab()
	controle.switch_left(tab.lines)
	tab.printtab()
	controle.switch_up(tab.lines)
	tab.printtab()
	controle.switch_left(tab.lines)
	tab.printtab()
	controle.switch_up(tab.lines)
	tab.printtab()
	controle.switch_left(tab.lines)
	tab.printtab()
	controle.switch_up(tab.lines)
	tab.printtab()
	controle.switch_left(tab.lines)
	tab.printtab()
	controle.switch_up(tab.lines)

def test_get(tab, controle):
	tab.printtab()
	print(controle.get_indexnbr(0, tab.lines))
	print(controle.get_indexnbr(1, tab.lines))
	print(controle.get_indexnbr(2, tab.lines))
	print(controle.get_indexnbr(3, tab.lines))
	print(controle.get_indexnbr(4, tab.lines))
	print("next test")
	controle.printtab(tab.listsort)
	tab.printtab()
	print(controle.next_diff_indexnbr(tab.lines, tab.lines))
	print(controle.next_diff_indexnbr(tab.lines, tab.listsort))
