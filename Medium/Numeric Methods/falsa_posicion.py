from math import exp

tol = 10**(-6)

def f(x):
    return (exp(-x) - x) 


def falsa_posicion(a, b):
    flag = True
    fa = f(a)
    fb = f(b)
    
    while flag:

        m_old = a - ((a-b) * fa) / fa - fb
        if f(a) * f(m_old) < 0:
            
            b = m_old
            m_new = a - ((a-b) * fa) / fa - fb
           
        else:
            a = m_old
            m_new = a - ((a-b) * fa) / fa - fb
            
        if abs((m_new - m_old) / m_new) < tol:
            flag = False
            
    return m_new

print(falsa_posicion(0,2))