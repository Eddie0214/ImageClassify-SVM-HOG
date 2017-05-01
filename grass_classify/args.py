#use on 函數定義 跟函數調用
def test_kwargs(first,*args,**kwargs):
    print 'fitst' , first
    for v in args:
        print 'args' , v
    for k,v in kwargs.items():
        print' args %s   kwargs %s:' %(k,v)

test_kwargs(1,2,3,4,k1=5,k2=6)