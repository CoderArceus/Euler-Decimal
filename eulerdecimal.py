from math import e

while True:
	
	while True:
		dp = (int(input('E upto what decimal places?  ')))
		if dp > 15:
			print()
			print('(✓Max Limit is 15✓)')
			print()
			continue
		else:
			print()
			print('-->' , round( e, dp))
			print()
			break

		
	while True:
		ch = input('Do You Want To Restart? Y/N ')
		if ch not in ('n', 'N', 'Y', 'y'):
			print()
			print('Invalid Input')
			print()
			continue
		elif ch in ('y', 'Y'):
			break
		else:
			quit()
		

