from sympy import *
from sympy.abc import x
import libnum

def f(r):
	p =  3 * r**2 +  2 * r + 7331
	q = 17 * r**2 + 18 * r + 1339
	n = p * q
	return [n]

n = 577080346122592746450960451960811644036616146551114466727848435471345510503600476295033089858879506008659314011731832530327234404538741244932419600335200164601269385608667547863884257092161720382751699219503255979447796158029804610763137212345011761551677964560842758022253563721669200186956359020683979540809
#r = solve([(3 * x**2 +  2 * x + 7331)*(17 * x**2 + 18 * x + 1339)-n],[x])
#print r
r = 57998468644974352708871490365213079390068504521588799445473981772354729547806
p = 3 * r**2 +  2 * r + 7331
q = 17 * r**2 + 18 * r + 1339
with open("flag.enc","r") as f:
	info = f.read()
	c = int(info.split("= ")[1])
assert p*q == n
assert p%4 == 3
assert q%4 == 3
m_p = pow(c,(p+1)/4,p)
m_q = pow(c,(q+1)/4,q)
y_p,y_q,temp = libnum.xgcd(p,q)
assert (y_p*p + y_q*q)%n == 1
m1 = (y_p*p*m_q+y_q*q*m_p) % n
m2 = (y_p*p*m_q-y_q*q*m_p) % n
m3 = n-m1
m4 = n-m2
print libnum.n2s(m1)
print libnum.n2s(m2)
print libnum.n2s(m3)
print libnum.n2s(m4)