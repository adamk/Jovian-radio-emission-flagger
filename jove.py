#!/usr/bin/env python

import math

print('Program to flag Jovian Decametric windows')
month = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
week = 42.46/360
pi = math.pi
kr = pi / 180
num1 = open('jovrad.txt', 'w')
yy = int(input(("Year for which predictions are required ")))
e = math.trunc(((yy-1) / 100))
print(e)
f = 2 - e + math.trunc(e/4)
print(f)
jd = math.trunc(365.25 * (yy - 1)) + 1721423 + f + .5
print(jd)
d0 = jd - 2435108
print(d0)
incr = 0
dmax = 0
tx = 0
ty = 0
yyly = 0
yylc = 0
if yy / 400 - math.trunc((yy / 400)) == 0:
    incr = 1
    print("in if-1")
yyly = yy / 4 - math.trunc((yy / 4))
yylc = yy / 100 - math.trunc((yy / 100))
if yyly == 0 and yylc != 0:
    print("in if-2")
    incr = 1
ty = 59 + incr
dmax = 365 + incr
tx = ty + .5
num1.write("******************************************************\n")
pout = "  JOVIAN IO-DECAMETRIC EMISSION PREDICTIONS FOR " + str(yy) + "\n"
num1.write(pout)
num1.write("******************************************************\n")
num1.write("\n")
num1.write("Day   Date   Hr(UT)  Io_Phase   CML   Dist(AU)  Source")
num1.write("\n")
th = 0

while int(th / 24) + 1 <= dmax:
    d = d0 + (th / 24)
    v = (157.0456 + .0011159 * d) % 360
    m = (357.2148 + .9856003 * d) % 360
    n = (94.3455 + .0830853 * d + .33 * math.sin(kr * v)) % 360
    j = (351.4266 + .9025179 * d - .33 * math.sin(kr * v)) % 360
    a = 1.916 * math.sin(kr * m) + .02 * math.sin(kr * 2 * m)
    b = 5.552 * math.sin(kr * n) + .167 * math.sin(kr * 2 * n)
    k = j + a - b
    r = 1.00014 - .01672 * math.cos(kr * m) - .00014 * math.cos(kr * 2 * m)
    re = 5.20867 - .25192 * math.cos(kr * n) - .0061 * math.cos(kr * 2 * n)
    dt = math.sqrt(re * re + r * r - 2 * re * r * math.cos(kr * k))
    sp = r * math.sin(kr * k) / dt
    ps = sp / .017452
    dl = d - dt / 173
    pb = ps - b
    xi = 150.4529 * math.trunc((dl)) + 870.4529 * (dl - math.trunc((dl)))
    L3 = (274.319 + pb + xi + .01016 * 51) % 360
    U1 = 101.5265 + 203.405863 * dl + pb
    U2 = 67.81114 + 101.291632 * dl + pb
    z = (2 * (U1 - U2)) % 360
    U1 = U1 + .472 * math.sin(kr * z)
    U1 = (U1 + 180) % 360
    s = ""
    if L3 < 255 and L3 > 200 and U1 < 250 and U1 > 220:
        s = "Io-A"
    if L3 < 180 and L3 > 105 and U1 < 100 and U1 > 80:
        s = "Io-B"
    if L3 < 350 and L3 > 300 and U1 < 250 and U1 > 230:
        s = "Io-C"
    if s != "":
        dy = math.trunc((th / 24)) + 1
        h = th - (dy - 1) * 24
        if(dy > th):
            m = math.trunc((dy - tx) / 30.6) + 3
            da = dy - ty - math.trunc((m - 3) * 30.6 + .5)
        else:
            m = math.trunc((dy - 1) / 31) + 1
            da = dy - (m - 1) * 31
        mn = month[(m-1)]
#        mn = month[(m-1)*3+1:(m-1)*3-1+3]
        outstring = "%s  %i  %2.1f  %i  %i  %1.2f  %s\n" % (mn, da, h, U1, L3, dt, s)
        num1.write(outstring)
    th = th + .5

num1.close()
print("Program Complete  - results in file JOVRAD.TXT")
