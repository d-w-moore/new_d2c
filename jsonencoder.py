import json

class myClass (object):
  def __init__(self,i): self.i=i
  def __repr__(self,): return '{0}({1!r})'.format(self.__class__.__name__, self.i)

class myenc (json.JSONEncoder):
  def default(self,obj):
    if isinstance(obj, complex):
               return {'__complex__':True, 'real':obj.real, 'imag':obj.imag }
    if isinstance(obj, myClass):
               return {'myClass':True, 'i':obj.i}
    return json.JSONEncoder.default(self, obj)

def json_decode (dct, memo=[]):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    if 'myClass' in dct:
        already_seen = [d for d in memo if d[0]==dct]
        if not already_seen:
            new_obj = myClass(dct['i'])
            memo.append( [dct, new_obj] )
            return new_obj
        else:
            return already_seen[0][1]
    return dct

#----

dc=json.dumps( [{'b':3},3+3j,myClass(100),-2j,myClass(100)],cls=myenc)
print('----\n'+ str(dc) + '\n----\n')

#----
x = json.loads(dc, object_hook = json_decode)
print(repr(x))
print (x[2], x[4], (x[2] is x[4]) )
