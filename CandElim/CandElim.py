import csv
from itertools import combinations

v = 6
s = list()
g = list()
s0 = ['0'] * v
g0 = ['?'] * v
lev = 0
s.append(s0)
g.append(g0)

print(s)


def in_consistant_with(d):
    global g
    for h in g:

        for (attr_d, attr_h) in zip(d, h):
            print("inconsistant", attr_h,":",attr_d)
            if attr_h == '?':
                continue
            if attr_h != attr_d:
                g.remove(h)
                break


def minimal_generalization(d):
    global g, s
    newhypo = list()

    for h in s:
        for (attr_d, attr_h) in zip(d, h):
            print("(", attr_d, ",", attr_h, ")")
            if attr_d == '?':
                newhypo.append('?')
                continue
            elif attr_h == '0':
                newhypo.append(attr_d)

            elif attr_d != attr_h:
                newhypo.append('?')
            else:
                newhypo.append(attr_h)

        s.remove(h)
        s.append(newhypo)



def minimal_specialization(d):
    global lev, g, s
    diffhypo = list()
    print("senti",d)
    for shypo in s:
       for (attr_s, attr_d) in zip(shypo, d):
           print(attr_s,attr_d)
           if attr_s == '?':
               diffhypo.append("?")

           elif attr_d == attr_s:
               diffhypo.append("?")

           else:
                diffhypo.append(attr_s)

    lev = lev + 1
    new_slist=list()
    if lev > v:
        lev = v
    l = []
    l.extend(range(0, v))
    comb = combinations(l, lev)

    # Print the obtained combinations
    for i in list(comb):
        hypo = ['?'] * v
        for element in i:
            hypo[element]=diffhypo[element]
        new_slist.append(hypo)
    g0=['?']*v
    g = [i for i in new_slist if i != g0]
    g = list(set( tuple(sub) for sub in g))
    g = list(list(tup) for tup in g)
    print("G LIST-",g)

#f = open("C:\\Users\\Student\\Desktop\\403\\car.csv")
f=open("/home/xfce/Desktop/403/tennis.csv")
data = csv.reader(f)

for d in data:
    if d[-1] == 'Yes':
        # positive example
        print("*****Positive Example", d)
        minimal_generalization(d)
        print(d,"-YES-", s)
        in_consistant_with(d)
        print("Glist:",g)

    if d[-1] == 'no':
        print("*****Negative Example", d)
        minimal_specialization(d)
        print(d, "-NO-", g)

print("S:",s)
print("G:",g)
