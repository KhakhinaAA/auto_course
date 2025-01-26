import math

l = 8
s = l**2
p = 4*l
#d = math.sqrt(2)
d1 = l * math.sqrt(2)
print( l , s, p, d1)

a = 4
b = 9
c = 2
d_2 = b**2 - 4*a*c
x_1 = (-b - math.sqrt(d_2)) / (2*a)
x_2 = (-b + math.sqrt(d_2)) / (2*a)

print(round(x_1, 2),round(x_2, 2))


string_1 ='"Москва" - столица России'
string_2 ='"Ярославль" - славный город'
string_3 = string_2[:11] + string_1[7:] + '\n' + string_1[:7] + string_2[10:]
print(string_3)

string_11 ='"Москва" - столица России'
string_22 ='"Ярославль" - славный город'
string_33 = string_2[:2] + string_1[2:] + ' ' + string_1[:2] + string_2[2:]
print(string_3)

string_4 = 'C:\python project\second script.py'
list_put = string_4.split("\\")
list_end = list_put[-1].split('.')
list_cool = list_end[0]
print(list_cool)

aa = 66
bb = 88
cc = aa + bb
dd = aa * bb
result = f"""
Сумма %d + %d = %d произведение %d * %d = %d
""" % (aa, bb ,cc, aa , bb ,dd)
print(result)

string_chet = 'Орден фениксаc'
print(string_chet[::2])

string_7 = 'wtf'
string_77 = 'brick quz jmpy veldt whangs fox'
ind_w = string_77.find("w")
ind_t = string_77.find("t")
ind_f = string_77.find("f")

ind_max1 = (ind_w + ind_t + abs(ind_w - ind_t)) / 2
ind_max2 = (ind_max1 + ind_f + abs(ind_max1 - ind_f)) / 2
ind_max3 = int(ind_max2 + 1)
print(ind_max2)
ind_min1 = (ind_w + ind_t - abs(ind_w - ind_t)) / 2
ind_min2 = (ind_min1 + ind_f - abs(ind_min1 - ind_f)) / 2
ind_min3 = int(ind_min2)
print(ind_min2)
print(string_77[ind_min3:ind_max3:])