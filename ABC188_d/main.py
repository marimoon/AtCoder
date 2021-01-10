N, CC = list( map(int, input().split()) )
As, Bs, Cs = [], [], []
st_day = 0
ed_day = 0
for _ in range(N):
    a,b,c = list( map(int, input().split()) )
    As.append(a)
    Bs.append(b)
    Cs.append(c)

days = sorted(list(set(As+Bs)))

def get_charge(a, b, c, day):
    if (a <= day) and (day <= b):
        return c
    else:
        return 0

amount = 0
for j in range(len(days)-1):
    st = days[j]
    ed = days[j+1]

    if st != ed-1:
        day_fee = 0
        for i in range(N):
            day_fee += get_charge(As[i], Bs[i], Cs[i], ed-1)
        if day_fee > CC:
            amount += CC*(ed-st-1)
        else:
            amount += day_fee*(ed-st-1)

    day_fee = 0
    for i in range(N):
        day_fee += get_charge(As[i], Bs[i], Cs[i], ed)
    if day_fee > CC:
        amount += CC
    else:
        amount += day_fee

    if j == 0:
        day_fee = 0
        for i in range(N):
            day_fee += get_charge(As[i], Bs[i], Cs[i], st)
        if day_fee > CC:
            amount += CC
        else:
            amount += day_fee


print(amount)
