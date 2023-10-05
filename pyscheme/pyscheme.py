# scheme.py
#
# Challenge: Can you implement a scheme interpreter in Python that's
# capable of executing the following procedure?

# A procedure definition for:
#
#   (define fact
#      (lambda (n) (if (= n 1)
#                   1
#                   (* n (fact (- n 1))))))
#
# It's represented in Python using the following tuple:

fact = ('define', 'fact', 
        ('lambda', ('n',), ('if', ('=', 'n', 1),
                            1,
                            ('*', 'n', ('fact', ('-', 'n', 1))))))

def pon_en_env(x,y):
    global env
    env[x] = y

env = {'+': lambda x,y: x+y , 'define': pon_en_env
    }



# You will define the following procedure for evaluating an expression
def seval(sexp):
    if isinstance(sexp,int):
        return sexp
    elif isinstance(sexp, str):
        return env.get(sexp,sexp) 
    elif isinstance(sexp, tuple):
        func = env[sexp[0]]
        args = [seval(e) for e in sexp[1:]]
        return func(*args)

# In writing seval, you are ONLY allowed to use the rules of Scheme
# evaluation that you currently know about.  So far, this includes the
# substitution model and the notion of special forms.
    
# Some basic tests
assert seval(42) == 42
assert seval(('+', ('+', 2,1), 3)) == 6
seval(('define', 'n', 5))

assert seval('n') == 5

# Now the ultimate test--can you run your procedure?
#seval(fact)
#assert seval(('fact', 'n')) == 120
