#!/usr/bin/python
# encoding: cp932
import sys, getopt
import random 



#------------------------
# パスワード作成
#------------------------
def make_password(length, type):

	#左手用キー
	left = []
	left_num = ["1","2","3","4","5"]
	left_small = ["q","w","e","r","t","a","s","d","f","g","z","x","c","v"]
	left_big = ["Q","W","E","R","T","A","S","D","F","G","Z","X","C","V"]
	
	left.append(left_num)
	left.append(left_small)
	left.append(left_big)

	#右手用キー
	right = []
	right_num = ["6","7","8","9","0"]
#	right_small = ["y","u","i","o","p","h","j","k","l","b","n","m"]
	right_small = ["y","u","i","o","p","h","j","k","b","n","m"]		#わかりにくいlを無くした
#	right_big = ["Y","U","I","O","P","H","J","K","L","B","N","M"]
	right_big = ["Y","U","I","P","H","J","K","L","B","N","M"]		#わかりにくいOを無くした

	right.append(right_num)
	right.append(right_small)
	right.append(right_big)
	
	#手
	hands = [left, right]

	#右手か左手か決める
	hand_type = random.randint(0, 1)		#param1 <= N <= param2
	#print hand_type

	#戻り値格納用
	password = ""

	#指定長さ分
	for i in range(length):
	
		hand = hands[hand_type]			#使う手を取得
		w = ""
		
		if(type == 0):				#数値のみ
			val = random.randrange(0, len(hand[0]))		#ランダムに1文字選ぶ
			w = hand[0][val]		#文字取得

		elif(type == 1):			#数値とアルファベット小文字
			ele = 0
			while 1:
				ele = random.randrange(0, len(hand))		#ランダムに文字種類を選ぶ
				if(ele != 2):
					break

			val = random.randrange(0, len(hand[ele]))		#ランダムに1文字選ぶ
			w = hand[ele][val]						#文字取得
		
		elif(type == 2):		#数値とアルファベット大文字
			ele = 0
			while 1:
				ele = random.randrange(0, len(hand))		#ランダムに文字種類を選ぶ
				if(ele != 1):
					break

			val = random.randrange(0, len(hand[ele]))		#ランダムに1文字選ぶ
			w = hand[ele][val]						#文字取得

		else:					#MIX
			ele = random.randrange(0, len(hand))
			val = random.randrange(0, len(hand[ele]))		#ランダムに1文字選ぶ
			w = hand[ele][val]						#文字取得

		password = password + w		#パスワード生成

		#手を交互に使う
		if(hand_type == 0):
			hand_type = 1
		else:
			hand_type = 0

	return password

#------------------------
# 使用方法
#------------------------
def usage():
	print 'usage:'
	print 'version 0.0.1'
	print 'Make password strings.'
	print 'Arguments: '
	print '    -l=password length'
	print '    -t=password type'
	print '         0:NUMBER_ONLY'
	print '         1:NUM_SMALL_LETTER'
	print '         2:NUM_BIG_LETTER'
	print '         3:ALL_MIX'
	print '    -n=number of password string'
	print 'python PwdMaker.py -l 8 -t 3 -n 5'


#------------------------
# Main
#------------------------
def main():

	if(len(sys.argv) == 1):
		usage()
		sys.exit()

	try:
		#コマンドラインオプションの解析
		#解析するコマンドライン,オプション文字(引数付きには:),ロングオプション文字(引数付きには=)
		#戻り値は(option, value)のタプルのリストと、オプションリストを除いた後に残った引数リスト
		opts, args = getopt.getopt(sys.argv[1:], "l:t:n:h", ["length=","type=","num=","help"])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	pwd_len = -1
	pwd_type = -1
	num_of_pwd = 1
	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit()
			
		if o in ("-l", "--length"):
			pwd_len = int(a)

		if o in ("-t", "--type"):
			pwd_type = int(a)

		if o in ("-n", "--num"):
			num_of_pwd = int(a)

	if(pwd_len < 0 or pwd_type < 0):
		usage()
		sys.exit()

	i = 0
	pwd_list = []
	same_cnt = 0
#	for i in range(num_of_pwd):
	while i<num_of_pwd:
		passwd = make_password(pwd_len, pwd_type)
		
		#既に存在するパスワードかどうか
		if passwd in pwd_list == True:
			same_cnt = same_cnt + 1
			continue
		else:
			pwd_list.append(passwd)

		#100回くらいパスワードがバッティングしたら止めておく
		if same_cnt >= 100:
			print("Make password failed")
			break

		print(passwd)
		i = i + 1

	print("Make password " + str(i) + " times.")


#------------------------
# 処理開始
#------------------------
if __name__ == '__main__':
	main()

