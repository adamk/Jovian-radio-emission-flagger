#!/usr/bin/env python
from __future__ import print_function, division
import math
print('Program to flag Jovian Decametric windows')
month = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
week = 42.46/360
pi = 3.141593
kr = pi / 180
form = "###  \ \ ##   ##.#     ###      ###    ##.##     \  \\"
num1 = open('jovrad.txt', 'w')
yy = int(raw_input(("Year for which predictions are required ")))
e = ((yy-1) / 100)
f = 2 - e + (e/4)
jd = (365.25 * (yy - 1)) + 1721423 + f + .5
d0 = jd - 2435108
incr = 0
dmax = 0
tx = 0
ty = 0
if yy / 400 - (yy / 400) == 0:
    incr = 1
    yyly = yy / 4 - (yy / 4)
    yylc = yy / 100 - (yy / 100)
if yyly == 0 and yylc != 0:
    incr = 1
    ty = 59 + incr
    dmax = 365 + incr
    tx = ty + .5
print("******************************************************", file=num1)
print("  JOVIAN IO-DECAMETRIC EMISSION PREDICTIONS FOR ",yy, file=num1)
print("******************************************************", file=num1)
print("\n", file=num1)
print("Day   Date   Hr(UT)  Io_Phase   CML   Dist(AU)  Source", file=num1)
print("\n", file=num1)
th = 0
def compute(d0, th, dmax):
    global U1, L3, dt, s
    d = d0 + th / 24
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
    xi = 150.4529 * (dl) + 870.4529 * (dl - (dl))
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
        outdat()
    th = th + .5

    while(((th / 24) + 1) < dmax or ((th / 24) + 1) == dmax):
        print("Program completed - results in file JOVRAD.TXT", file=num1)
compute(d0, th, dmax)

def outdat(th,tx,ty):
    dy = (th / 24) + 1
    h = th = (dy - 1) * 24
    if(dy > th):
        m = ((dy - tx) / 30.6) + 3
        da = dy - ty - ((m - 3) * 30.6 + .5)
    else:
        m = ((dy - 1) / 31) + 1
        da = dy - (m - 1) * 31
    m = int(m)
    mn = month[(m-1)*3+1:(m-1)*3-1+3]
    print(f, dy, mn, da, h, U1, L3, dt, s, file=num1)
outdat(th,tx,ty)
