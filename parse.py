def DecToHex(x):
	result = ''
	while (x != 0):
		if ((x % 16) < 10):
			result = str(x % 16) + result
		else:
			temp = ''

			if (x % 16) == 10:
				temp = 'A'
			elif (x % 16) == 11:
				temp = 'B'
			elif (x % 16) == 12:
				temp = 'C'
			elif (x % 16) == 13:
				temp = 'D'
			elif (x % 16) == 14:
				temp = 'E'
			elif (x % 16) == 15:
				temp = 'F'

			result = temp + result;
		x = x / 16
	return result.zfill(4)

first_4_StudentID_Digits = raw_input("Input first 4 digits of your student number: ")
last_4_StudentID_Digits = raw_input("Input last 4 digits of your student number: ")

# first_4_StudentID_Digits = hex(int(first_4_StudentID_Digits))
# last_4_StudentID_Digits = hex(int(last_4_StudentID_Digits))

first_4_StudentID_Digits = DecToHex(int(first_4_StudentID_Digits))
last_4_StudentID_Digits = DecToHex(int(last_4_StudentID_Digits))

# print "First 4 digits to HEX: %s" % (first_4_StudentID_Digits)
# print "Last 4 digits to HEX: %s" % (last_4_StudentID_Digits)

first_part = "0x"
rest_part = "000000000000000051020000"

print "Your TCP/IP packet is %s%s%s%s" % (first_part,first_4_StudentID_Digits, last_4_StudentID_Digits, rest_part)