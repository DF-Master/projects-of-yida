import cdblib
with open('AI/AI_in_chem/YGO-AI/cdbopen/cards.cdb','rb') as f:
    data=f.read()
reader = cdblib.Reader(data)
print(reader,type(reader),reader.iteritems())
for key, value in reader.iteritems():
    print('+{},{}:{}->{}'.format(len(key), len(value), key, value))