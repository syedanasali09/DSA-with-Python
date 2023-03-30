tpl = ('item1', 'item2','item3')
len(tpl)
first_item = tpl[0]
second_item = tpl[1]

first_item = tpl[-2]
second_item = tpl[-3]

tpl2 = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4] 

all_items = tpl[0:]         
middle_two_items = tpl[1:3] 

tpl3 = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         
middle_two_items = tpl[-3:-1]  

print(tpl)