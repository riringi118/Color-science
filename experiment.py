#/usr/local/bin python3
# experiment.py


from psychopy import visual, core, event, gui
import random
import numpy as np
import time
import os
import datetime
import openpyxl


sub_info = {'参加者':'', '年齢':'', '性別':['男性', '女性'], '国籍':''}

info_dlg = gui.DlgFromDict(sub_info)

if not info_dlg.OK:
	core.quit()

subID = sub_info['参加者']
age = sub_info['年齢']
sex = sub_info['性別']
country = sub_info['国籍']

time_now = datetime.datetime.now().strftime('%Y.%m.%d %H.%M.%S')

file = openpyxl.Workbook()

sheet = file.active

sheet['J1'] = subID
sheet['J2'] = 'age:' + age
sheet['J3'] = 'gender:' + sex
sheet['J4'] = 'country:' + country

sheet['A1'] = 'typical_1'
sheet['B1'] = 'typical_2'
sheet['C1'] = 'typical_3'
sheet['D1'] = 'typical_4'
sheet['E1'] = 'atypical_1'
sheet['F1'] = 'atypical_2'
sheet['G1'] = 'atypical_3'
sheet['H1'] = 'atypical_4'
 
sheet.column_dimensions['A'].width = 12
sheet.column_dimensions['B'].width = 12
sheet.column_dimensions['C'].width = 12
sheet.column_dimensions['D'].width = 12
sheet.column_dimensions['E'].width = 12
sheet.column_dimensions['F'].width = 12
sheet.column_dimensions['G'].width = 12
sheet.column_dimensions['H'].width = 12

#############################

posList = [1, 2, 3, 4, 5, 6, 7, 8]

colorList = [[181, 24, 79], [205, 31, 66], [221, 55, 55],
			 [229, 81, 37], [230, 109, 0], [242, 149, 0],
			 [238, 172, 0], [226, 197, 0], [200, 187, 0],
			 [164, 179, 0], [74, 163, 21], [0, 154, 85],
			 [0, 140, 105], [0, 126, 119], [0, 124, 140],
			 [0, 107, 147], [0, 90, 145], [0, 86, 156],
			 [0, 80, 157], [71, 71, 152], [102, 62, 140],
			 [121, 53, 128], [137, 44, 113], [171, 38, 100]]

unfit_word_list = ['売却','自然','特別','解明','依然','直接','政府','首相','姿勢','問題',
				   '機会','疑問','徹底','調査','図書','舞踊','中華','料理','寄生','断る','内職','鉛筆','録画',
				   '睡眠','不足','独立','未来','弓道','病院','効率','診察','内臓','快楽','微小']

fit_color_textList = [['上品', [121, 53, 128]],
					  ['健康', [74, 163, 21]],
					  ['冷静', [0, 86, 156]],
					  ['危機', [205, 31, 66]],
					  ['地味', [164, 179, 0]],
					  ['安全', [0, 154, 85]],
					  ['平凡', [164, 179, 0]],
					  ['平和', [0, 154, 85]],
					  ['幸福', [226, 197, 0]],
					  ['恐怖', [71, 71, 152]],
					  ['新鮮', [0, 154, 85]],
					  ['暑い', [221, 55, 55]],
					  ['柔和', [238, 172, 0]],
					  ['正式', [0, 107, 147]],
					  ['派手', [221, 55, 55]],
					  ['清潔', [0, 90, 145]],
					  ['渋い', [164, 179, 0]],
					  ['火事', [221, 55, 55]],
					  ['無垢', [238, 172, 0]],
					  ['甘い', [221, 55, 55]],
					  ['甘美', [171, 38, 100]],
					  ['簡素', [164, 179, 0]],
					  ['繊細', [0, 107, 147]],
					  ['美容', [171, 38, 100]],
					  ['貴重', [226, 197, 0]],
					  ['賢明', [0, 107, 147]],
					  ['軽い', [226, 197, 0]],
					  ['陽気', [242, 149, 0]],
					  ['青春', [74, 163, 21]],
					  ['静か', [0, 90, 145]],
					  ['魅力', [137, 44, 113]],
					  ['鮮烈', [205, 31, 66]]
					  ]

#################


def get_Pos(num):
	list_ = np.linspace(7/8*np.pi, -7/8*np.pi, 8)
	return [450+480*np.cos(list_[num-1]), 480*np.sin(list_[num-1])]

def mainTask(condition, num_of_fitcolor):     #典型色刺激の数を設定する
  #windowの生成
	mouse = event.Mouse(visible=True, newPos=[0, 0], win=win)  #mouse objectiveの生成

	kwargs = {'win': win, 							
		'font': 'Hiragino Kaku Gothic Pro W3',
		'colorSpace': 'rgb255',
		'units': 'pix',
		'height': 40
		}						#刺激のキーワード引数

	unfit_word_list2 = random.sample(unfit_word_list, 24)
	unfit_color_textList = list(zip(unfit_word_list2, colorList))

	target_letter_stim = visual.TextStim(**kwargs) 			#刺激生成
	letter_stim1 = visual.TextStim(**kwargs)
	letter_stim2 = visual.TextStim(**kwargs)
	letter_stim3 = visual.TextStim(**kwargs)
	letter_stim4 = visual.TextStim(**kwargs)
	letter_stim5 = visual.TextStim(**kwargs)
	letter_stim6 = visual.TextStim(**kwargs)
	letter_stim7 = visual.TextStim(**kwargs)
	foc_stim = visual.TextStim(text='+', pos=(480, 0), **kwargs)

	main_task_rect = visual.Rect(win=win, 
	lineWidth=0,
	size=(250, 100), 
	fillColor=[255, 0, 0], 
	fillColorSpace='rgb255',
	units='pix',
	opacity=0)

	stimList = [letter_stim1, letter_stim2, letter_stim3, letter_stim4, letter_stim5, letter_stim6, letter_stim7]

	circle_stim = visual.Circle(win, radius=480, pos=[0, 0])

	stopwatch = core.Clock()

	fct = fit_color_textList
	uct = unfit_color_textList
	
	pos_list = [1, 2, 3, 4, 5, 6, 7, 8]

	tpo = random.choice(pos_list)
	pos_list.remove(tpo)

	stim_list = [letter_stim1, letter_stim2, letter_stim3, letter_stim4, letter_stim5, letter_stim6, letter_stim7]

	if condition == 'fit':
		target = random.choice(fct)
		fct.remove(target)
		text_with_target = random.sample(fct, num_of_fitcolor-1)
		stim_with_target = random.sample(stim_list, num_of_fitcolor-1)
		pos_with_target = random.sample(pos_list, num_of_fitcolor-1)
		text_not_with_target = random.sample(uct, 8 - num_of_fitcolor)

	elif condition == 'unfit':
		target = random.choice(uct)
		uct.remove(target)
		text_with_target = random.sample(uct, num_of_fitcolor-1)
		stim_with_target = random.sample(stim_list, num_of_fitcolor-1)
		pos_with_target = random.sample(pos_list, num_of_fitcolor-1)
		text_not_with_target = random.sample(fct, 8 - num_of_fitcolor)

	for i in pos_with_target:
		pos_list.remove(i)
	for i in stim_with_target:
		stim_list.remove(i)


	loop_fit = zip(text_with_target, stim_with_target, pos_with_target)
	loop_unfit = zip(text_not_with_target, stim_list, pos_list)

	mouse.clickReset()

	target_letter_stim.setText(target[0])
	target_letter_stim.setPos([450, 100])
	target_letter_stim.setColor([0, 0, 0])
	target_letter_stim.draw()
	win.flip()

	core.wait(1)

	foc_stim.draw()
	win.flip()
	core.wait(0.5)

	mouse.setPos([0, 0])

	while True:
		target_letter_stim.setColor(target[1])
		target_letter_stim.setText(target[0])
		target_letter_stim.setPos(get_Pos(tpo))
		main_task_rect.setPos([get_Pos(tpo)[0]-450, get_Pos(tpo)[1]])

		for text, stim, pos in loop_fit:
			stim.setText(text[0])
			stim.setColor(text[1])
			stim.setPos(get_Pos(pos))
			

		for text, stim, pos in loop_unfit:
			stim.setText(text[0])
			stim.setColor(text[1])
			stim.setPos(get_Pos(pos))
			
		for i in stim_list:
			i.draw()

		for i in stim_with_target:
			i.draw()
		target_letter_stim.draw()
		main_task_rect.draw()

		win.flip()

		
		if mouse.isPressedIn(main_task_rect):
			press, times = mouse.getPressed(getTime=True)
			core.wait(0.5)
			break

	if condition == 'fit':
		fct.append(target)
	elif condition == 'unfit':
		uct.append(target)

	return times[0]


win = visual.Window(size=(1680, 1050), fullscr=True,
						screen=0, allowGUI=True,
						color=[0, 0, 0], units='pix')    #windowの生成

mouse = event.Mouse(visible=True, newPos=[0, 0], win=win)  #mouse objectiveの生成

kwargs = {'win': win, 							
		'font': 'Hiragino Kaku Gothic Pro W3',
		'colorSpace': 'rgb255',
		'units': 'pix',
		}						#刺激のキーワード引数

target_letter_stim = visual.TextStim(**kwargs) 			#刺激生成
letter_stim1 = visual.TextStim(**kwargs)
letter_stim2 = visual.TextStim(**kwargs)
letter_stim3 = visual.TextStim(**kwargs)
letter_stim4 = visual.TextStim(**kwargs)
letter_stim5 = visual.TextStim(**kwargs)
letter_stim6 = visual.TextStim(**kwargs)
letter_stim7 = visual.TextStim(**kwargs)

intro_1_text1 = visual.TextStim(text='実験にご参加いただき、ありがとうございます。', pos=(-70, 0), height=40, **kwargs)

intro_1_text2 = visual.TextStim(text='ーー次へ', pos=(1000, -450), height=20, **kwargs)

intro_1_rect = visual.Rect(win=win, 
	lineWidth=0,
	pos=(1000-450, -450), 
	size=(250, 100), 
	fillColor=[255, 0, 0], 
	fillColorSpace='rgb255',
	units='pix',
	opacity=0)

while True:											### welcome画面1
	if intro_1_rect.contains(mouse.getPos()):
		intro_1_text2.setColor([255, 10, 10])
	if not intro_1_rect.contains(mouse.getPos()):
		intro_1_text2.setColor([0, 0, 0])
	elif mouse.isPressedIn(intro_1_rect):
		break
	intro_1_text1.draw()
	intro_1_text2.draw()
	intro_1_rect.draw()

	win.flip() 

intro_2_text = visual.TextStim(text='実験の説明と練習課題へ', pos=(240, 0), height=40, **kwargs) ###説明に入る

intro_2_text.draw()

win.flip()

core.wait(2)                     ###ページ1終わり

intro_3_text1 = visual.TextStim(text='"目標"', pos=(450, 100), **kwargs, height=40) ##ページ2始まり
intro_3_text2 = visual.TextStim(text='ランダムな単語が1秒ほど呈示されます、あとでこの単語を探します。', pos=(475, 0), **kwargs)

intro_3_circl = visual.Circle(win=win, radius=80, pos=(20, 100), edges=60, lineWidth=6, lineColor='red')
intro_3_text1.draw()
win.flip()
core.wait(2)

si = 0
while True:
	
	si += 0.05
	opa = np.sin(si)
	if opa < 0:
		opa = -opa
	intro_3_circl.opacity = opa

	intro_3_text1.draw()
	intro_3_text2.draw()
	intro_3_circl.draw()

	if intro_1_rect.contains(mouse.getPos()):
		intro_1_text2.setColor([255, 10, 10])
	if not intro_1_rect.contains(mouse.getPos()):
		intro_1_text2.setColor([0, 0, 0])
	elif mouse.isPressedIn(intro_1_rect):
		break

	intro_1_text2.draw()
	intro_1_rect.draw()

	win.flip()												#####ページ2終わり

cir_list = np.linspace(np.pi, -np.pi, 202)
line_obj_list = []
cir_text_list = [round(7/8*np.pi, 1), round(5/8*np.pi, 1), round(3/8*np.pi, 1), round(1/8*np.pi, 1), round(-1/8*np.pi, 1),
 				round(-3/8*np.pi, 1), round(-5/8*np.pi, 1), round(-7/8*np.pi, 1)]
cir_word_list = random.sample(unfit_word_list, 8)
cir_color_list = [[190, 0, 40], [255, 0, 0], [0, 113, 40], [0, 34, 40], [255, 0, 0], [110, 0, 0], [255, 0, 0], [0, 0, 110]]

loopNum = 1
for pi_cir in cir_list:
	line_obj = visual.Line(win=win, start=(480*np.cos(pi_cir), 480*np.sin(pi_cir)), end=(480*np.cos(pi_cir-0.05), 480*np.sin(pi_cir-0.05)))
	line_obj_list.append(line_obj)
	if loopNum%25 == 0:
		text_obj = visual.TextStim(height=40, **kwargs)
		text_obj.setText(random.choice(unfit_word_list))
		text_obj.setColor(cir_color_list[int(loopNum/25) - 1])
		text_obj.setPos(get_Pos(posList[int(loopNum/25) - 1]))
		line_obj_list.insert(0, text_obj)
	for line in line_obj_list:
		line.draw()

	loopNum += 1
	if loopNum != 203:
		win.flip()
	elif loopNum == 203:
		time.sleep(2)
		while True:
			intro_4_text = visual.TextStim(text='''
													円形上8の位置の中で、先ほどの目標単語を探す。
													見つかったら目標単語の上でマウスの左クリックをしてくだい。
																									''', pos=(450, 0), **kwargs)

			if intro_1_rect.contains(mouse.getPos()):
				intro_1_text2.setColor([255, 10, 10])
			if not intro_1_rect.contains(mouse.getPos()):
				intro_1_text2.setColor([0, 0, 0])
			elif mouse.isPressedIn(intro_1_rect):
				break
			for line in line_obj_list:
				line.draw()

			intro_4_text.draw()
			intro_1_text2.draw()
			intro_1_rect.draw()

			win.flip()	


for i in range(8):
	mainTask(condition=random.choice(['fit', 'unfit']), num_of_fitcolor=random.randint(1, 8))


start_text = visual.TextStim(**kwargs, text='実験開始[space]', pos=(330, 0), height=40)

start_text.draw()

win.flip()

event.waitKeys(keyList= ['space'])


pre_loopList = []

for i in range(1, 5):
	sub_list1 = [['fit', i]]*10
	sub_list2 = [['unfit', i]]*10
	for a in sub_list1:
		pre_loopList.append(a)
	for b in sub_list2:
		pre_loopList.append(b)

loopList = random.sample(pre_loopList, 80)

line_num1 = 2
line_num2 = 2
line_num3 = 2
line_num4 = 2
line_num5 = 2
line_num6 = 2
line_num7 = 2
line_num8 = 2

for condition, num in loopList:
	reaction_time = mainTask(condition=condition, num_of_fitcolor=num)
	if condition == 'fit' and num == 1:
		sheet['A'+str(line_num1)] = reaction_time
		line_num1 += 1
	if condition == 'fit' and num == 2:
		sheet['B'+str(line_num2)] = reaction_time
		line_num2 += 1
	if condition == 'fit' and num == 3:
		sheet['C'+str(line_num3)] = reaction_time
		line_num3 += 1
	if condition == 'fit' and num == 4:
		sheet['D'+str(line_num4)] = reaction_time
		line_num4 += 1
	if condition == 'unfit' and num == 1:
		sheet['E'+str(line_num5)] = reaction_time
		line_num5 += 1
	if condition == 'unfit' and num == 2:
		sheet['F'+str(line_num6)] = reaction_time
		line_num6 += 1
	if condition == 'unfit' and num == 3:
		sheet['G'+str(line_num7)] = reaction_time
		line_num7 += 1
	if condition == 'unfit' and num == 4:
		sheet['H'+str(line_num8)] = reaction_time
		line_num8 += 1

sheet['A13'] = '=AVERAGE(A2:A11)'
sheet['B13'] = '=AVERAGE(B2:B11)'
sheet['C13'] = '=AVERAGE(C2:C11)'
sheet['D13'] = '=AVERAGE(D2:D11)'
sheet['E13'] = '=AVERAGE(E2:E11)'
sheet['F13'] = '=AVERAGE(F2:F11)'
sheet['G13'] = '=AVERAGE(G2:G11)'
sheet['H13'] = '=AVERAGE(H2:H11)'

ref_obj = openpyxl.chart.Reference(sheet, min_col=1, min_row=13, max_col=8, max_row=13)
series_obj = openpyxl.chart.Series(ref_obj, title='Average')
chart_obj = openpyxl.chart.BarChart()
chart_obj.append(series_obj)
chart_obj.x = 1500
chart_obj.y = 800
chart_obj.w = 500
chart_obj.h = 400

sheet.add_chart(chart_obj)


file.save('/Users/kawabata/Documents/Sublime/experiment_project/data/{} _{}.xlsx'.format(subID, time_now))


core.quit()