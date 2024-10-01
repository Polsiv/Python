from math import exp

tol = 10**(-6)

def f(x):
    return (exp(-x) - x) 


def biseccion(a, b):
    flag = True
    
    while flag:

        m_old = (a + b) / 2
        if f(a) * f(m_old) < 0:
            
            b = m_old
            m_new = (a + b) / 2
           
        else:
            a = m_old
            m_new = (a + b) / 2
            
        if abs((m_new - m_old) / m_new) < tol:
            flag = False
            
    return m_new

print(biseccion(0, 100))