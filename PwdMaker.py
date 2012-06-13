#!/usr/bin/python
# encoding: cp932
import sys, getopt
import random 



#------------------------
# �p�X���[�h�쐬
#------------------------
def make_password(length, type):

	#����p�L�[
	left = []
	left_num = ["1","2","3","4","5"]
	left_small = ["q","w","e","r","t","a","s","d","f","g","z","x","c","v"]
	left_big = ["Q","W","E","R","T","A","S","D","F","G","Z","X","C","V"]
	
	left.append(left_num)
	left.append(left_small)
	left.append(left_big)

	#�E��p�L�[
	right = []
	right_num = ["6","7","8","9","0"]
#	right_small = ["y","u","i","o","p","h","j","k","l","b","n","m"]
	right_small = ["y","u","i","o","p","h","j","k","b","n","m"]		#�킩��ɂ���l�𖳂�����
#	right_big = ["Y","U","I","O","P","H","J","K","L","B","N","M"]
	right_big = ["Y","U","I","P","H","J","K","L","B","N","M"]		#�킩��ɂ���O�𖳂�����

	right.append(right_num)
	right.append(right_small)
	right.append(right_big)
	
	#��
	hands = [left, right]

	#�E�肩���肩���߂�
	hand_type = random.randint(0, 1)		#param1 <= N <= param2
	#print hand_type

	#�߂�l�i�[�p
	password = ""

	#�w�蒷����
	for i in range(length):
	
		hand = hands[hand_type]			#�g������擾
		w = ""
		
		if(type == 0):				#���l�̂�
			val = random.randrange(0, len(hand[0]))		#�����_����1�����I��
			w = hand[0][val]		#�����擾

		elif(type == 1):			#���l�ƃA���t�@�x�b�g������
			ele = 0
			while 1:
				ele = random.randrange(0, len(hand))		#�����_���ɕ�����ނ�I��
				if(ele != 2):
					break

			val = random.randrange(0, len(hand[ele]))		#�����_����1�����I��
			w = hand[ele][val]						#�����擾
		
		elif(type == 2):		#���l�ƃA���t�@�x�b�g�啶��
			ele = 0
			while 1:
				ele = random.randrange(0, len(hand))		#�����_���ɕ�����ނ�I��
				if(ele != 1):
					break

			val = random.randrange(0, len(hand[ele]))		#�����_����1�����I��
			w = hand[ele][val]						#�����擾

		else:					#MIX
			ele = random.randrange(0, len(hand))
			val = random.randrange(0, len(hand[ele]))		#�����_����1�����I��
			w = hand[ele][val]						#�����擾

		password = password + w		#�p�X���[�h����

		#������݂Ɏg��
		if(hand_type == 0):
			hand_type = 1
		else:
			hand_type = 0

	return password

#------------------------
# �g�p���@
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
		#�R�}���h���C���I�v�V�����̉��
		#��͂���R�}���h���C��,�I�v�V��������(�����t���ɂ�:),�����O�I�v�V��������(�����t���ɂ�=)
		#�߂�l��(option, value)�̃^�v���̃��X�g�ƁA�I�v�V�������X�g����������Ɏc�����������X�g
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
		
		#���ɑ��݂���p�X���[�h���ǂ���
		if passwd in pwd_list == True:
			same_cnt = same_cnt + 1
			continue
		else:
			pwd_list.append(passwd)

		#100�񂭂炢�p�X���[�h���o�b�e�B���O������~�߂Ă���
		if same_cnt >= 100:
			print("Make password failed")
			break

		print(passwd)
		i = i + 1

	print("Make password " + str(i) + " times.")


#------------------------
# �����J�n
#------------------------
if __name__ == '__main__':
	main()

