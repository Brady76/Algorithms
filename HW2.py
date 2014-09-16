from fractions import gcd
global p, q, x, e, d, i, N, privatekeyN, privatekeyNCopy, greatestcommondenominator

i = 0
p = int(raw_input("Please enter your p value: "))
q = int(raw_input("Please enter your q value: "))
x = int(raw_input("Please enter your x value: "))
e = int(raw_input("Please enter your e value: "))

N = p * q
privatekeyN = (p-1) * (q - 1)
privatekeyNCopy = privatekeyN
greatestcommondenominator = gcd(e,privatekeyN)
while(privatekeyNCopy != greatestcommondenominator):
	privatekeyNCopy = privatekeyNCopy - e 
	i = i + 1
i = -1 * i
d = i % privatekeyN	

StringN = str(N)
stringe = str(e)
stringd = str(d)

print "Your public key is: (" + StringN + "," + stringe + ")"
print "Your private key is: " + stringd

EncryptYes = raw_input("Would you like to Encrypt? ")
if(EncryptYes == "Yes"):
	y = pow(x, e) % N
	print y 
DecryptYes = raw_input("Would you like to Decrypt the previously used y value? ")
if(DecryptYes == "Yes"):
	x = pow(y, d) % N
	print x
	
	
	
