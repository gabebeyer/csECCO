def main():
	print binaryToDecimal('100111011')
	print decimalToBinary(7652)

#wants a string 
def binaryToDecimal(binaryNumber):

	positional = len(binaryNumber) - 1
	decimal = 0

	for x in binaryNumber:
		decimal += int(x) * (2**positional)
		positional -= 1

	return int(decimal)


#wants an integer 
def decimalToBinary(decimalNumber): 
	
	if decimalNumber == 0:
		return '0'
	else:
		return decimalToBinary(decimalNumber/2) + str(decimalNumber%2)

if __name__ == '__main__':
	main()