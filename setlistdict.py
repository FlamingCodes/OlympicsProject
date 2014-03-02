list = ("english", "deutsch","deutsch", "deutsch", "english")
set = set(list)
di = {}

for s in set:
    a = str(s)
    b = str(list.count(str(s)))
    print a + ", " + b
    di[a] = b
print di

for key, value in sorted(di.iteritems(), key=lambda (v,k): (k,v), reverse=True):
    print "%s: %s" % (key, value)
