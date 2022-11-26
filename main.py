plus = '+'
minus = '-'
mult = '*'
div = '/'
exp = '^'
opening = '('
closing = ')'
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

current = ''
current_index = 0
inp = ''
running_e = 0


def update_current():
    global current
    global current_index
    current_index += 1
    if current_index >= len(inp):
        current = ''
        print('Reached end of input')
    else:
        current = inp[current_index]
        print('Update current to ' + current)


def e():
    global running_e
    running_e += 1
    print("E -> TE'")
    t_val = t()
    e_prime_val = e_prime(t_val)
    if current == '':
        return e_prime_val
    if current == ')' and running_e > 1:
        return e_prime_val
    raise Exception("Could not resolve E -> ? " + inp, current)


def e_prime(prev_val):
    if current == plus:
        print("E' -> +TE'")
        update_current()
        t_val = t()
        e_prime_val = e_prime(t_val)
        return str(float(prev_val) + float(e_prime_val))
    elif current == minus:
        print("E' -> -TE'")
        update_current()
        t_val = t()
        e_prime_val = e_prime(t_val)
        return str(float(prev_val) - float(e_prime_val))
    else:
        print("E' -> empty")
        return prev_val


def t():
    print("T -> PT'")
    p_val = p()
    t_prime_val = t_prime(p_val)
    return t_prime_val


def t_prime(prev_val):
    if current == mult:
        print("T' -> *PT'")
        update_current()
        p_val = p()
        p_val = str(float(prev_val) * float(p_val))
        t_prime_val = t_prime(p_val)
        return t_prime_val
    elif current == div:
        print("T' -> /PT'")
        update_current()
        p_val = p()
        p_val = str(float(prev_val) / float(p_val))
        t_prime_val = t_prime(p_val)
        return t_prime_val
    else:
        print("T' -> empty")
        return prev_val


def p():
    print("P -> RQ")
    r_val = r()
    q_val = q(r_val)
    return q_val


def q(prev_val):
    if current == exp:
        print("Q -> ^P")
        update_current()
        p_val = p()
        print('Prev: ', prev_val, 'p_val:', p_val)
        return str(float(prev_val) ** float(p_val))
    else:
        print("Q -> empty")
        return prev_val


def r():
    if current == minus:
        print("R -> -F")
        update_current()
        f_val = f()
        return str(-float(f_val))
    else:
        print("R -> F")
        f_val = f()
        return f_val


def f():
    if current == opening:
        print("F -> (E)")
        update_current()
        e_val = e()
        if current == closing:
            update_current()
            return e_val
    elif current in numbers:
        print("F -> number")
        temp = current
        update_current()
        while current in numbers:
            temp += current
            update_current()
        return temp
    raise Exception("Could not resolve F -> ? " + inp)


if __name__ == "__main__":
    while True:
        current_index = 0
        print("Enter your equation: ")
        inp = input()
        inp = inp.replace(' ', '')
        current = inp[current_index]
        print(e())
        print('\n\n\n\n')
