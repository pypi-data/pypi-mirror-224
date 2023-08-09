_vis_ = []
_prime_=[]
def init(n):
    _prime_.append(1)
    for i in range(n+1):
        _vis_.append(1)
    _vis_[0]=0;
    _vis_[1]=0;
    j=2
    while (j*j)<=n:
        if _vis_[j]:
            k=j*j
            while k<=n:
                _vis_[k]=0
                k+=j
        j+=1
    for i in range(n+1):
        if _vis_[i]:_prime_.append(i);
def is_prime(n):
    return _vis_[n]
def factor(x):
    l=[]
    for i in range(1,x+1):
        if not(x%i):
            l.append(i)
    return l
def gcd(a,b):
    if not(a%b):
        return b
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return int(a*b/gcd(a,b))
def cut_factor(a):
    l=[]
    i=1
    while _prime_[i]<=a:
        while not(a%_prime_[i]):
            l.append(_prime_[i])
            a/=_prime_[i]
            a=int(a)
        i+=1
    return l