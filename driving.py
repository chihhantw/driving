#輸入國家、年紀，再判斷是否可以開車
country = input('請問你在哪個國家?')
age = input('那麼你現在幾歲呢?')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你有資格考汽車駕照唷！')
	else:
		print('我想你還是等等吧！')
elif country == '美國':
	if age >= 16:
		print('你有資格考汽車駕照唷！')
	else:
		print('我想你還是等等吧！')
else:
	print('目前只提供查詢台灣或美國的資訊唷！')