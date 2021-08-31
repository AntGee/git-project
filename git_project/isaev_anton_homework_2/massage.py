def get_sign(x):
    if x[0] in '+-':
        return x[0]


msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(msg):
    sign = get_sign(msg[i])
    if msg[i].isdigit() or (sign and msg[i][1:].isdigit()):
        if sign:
            msg[i] = sign + msg[i][1:].zfill(2)
        else:
            msg[i] = msg[i].zfill(2)
        msg.insert(i, '"')
        msg.insert(i + 2, '"')
        i += 2
    i += 1

print(msg)
new_msg = ' '.join(msg)
print(new_msg)
