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

print_debug = False


def update_current():
    global current
    global current_index
    current_index += 1
    if current_index >= len(inp):
        current = ''
        if print_debug:
            print('Reached end of input')
    else:
        current = inp[current_index]
        if print_debug:
            print('Update current to ' + current)


def e():
    global running_e
    running_e += 1
    if print_debug:
        print("E -> TE'")
    t_val = t()
    e_prime_val = e_prime(t_val)
    if current == '':
        return e_prime_val
    if current == ')' and running_e > 1:
        running_e -= 1
        return e_prime_val
    raise Exception("Could not parse '" + inp + "'; Reading: " + current)


def e_prime(prev_val):
    if current == plus:
        if print_debug:
            print("E' -> +TE'")
        update_current()
        t_val = t()
        e_prime_val = e_prime(t_val)
        return str(float(prev_val) + float(e_prime_val))
    elif current == minus:
        if print_debug:
            print("E' -> -TE'")
        update_current()
        t_val = t()
        e_prime_val = e_prime(t_val)
        return str(float(prev_val) - float(e_prime_val))
    else:
        if print_debug:
            print("E' -> empty")
        return prev_val


def t():
    if print_debug:
        print("T -> PT'")
    p_val = p()
    t_prime_val = t_prime(p_val)
    return t_prime_val


def t_prime(prev_val):
    if current == mult:
        if print_debug:
            print("T' -> *PT'")
        update_current()
        p_val = p()
        p_val = str(float(prev_val) * float(p_val))
        t_prime_val = t_prime(p_val)
        return t_prime_val
    elif current == div:
        if print_debug:
            print("T' -> /PT'")
        update_current()
        p_val = p()
        p_val = str(float(prev_val) / float(p_val))
        t_prime_val = t_prime(p_val)
        return t_prime_val
    else:
        if print_debug:
            print("T' -> empty")
        return prev_val


def p():
    if print_debug:
        print("P -> RQ")
    r_val = r()
    q_val = q(r_val)
    return q_val


def q(prev_val):
    if current == exp:
        if print_debug:
            print("Q -> ^P")
        update_current()
        p_val = p()
        return str(float(prev_val) ** float(p_val))
    else:
        if print_debug:
            print("Q -> empty")
        return prev_val


def r():
    if current == minus:
        if print_debug:
            print("R -> -F")
        update_current()
        f_val = f()
        return str(-float(f_val))
    else:
        if print_debug:
            print("R -> F")
        f_val = f()
        return f_val


def f():
    if current == opening:
        if print_debug:
            print("F -> (E)")
        update_current()
        e_val = e()
        if current == closing:
            update_current()
            return e_val
    elif current in numbers:
        if print_debug:
            print("F -> number")
        temp = current
        update_current()
        while current in numbers:
            temp += current
            update_current()
        return temp
    raise Exception("Can't parse '" + current + "'! Input: " + inp)


if __name__ == "__main__":
    # Parse arguments
    import argparse

    parser = argparse.ArgumentParser(description='Run arithmetic parser.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # general arguments
    parser.add_argument('--debug', help='Whether to show debug printing or not.', nargs='?', const=True)

    args = parser.parse_args()
    print_debug = args.debug
    while True:
        current_index = 0
        running_e = 0
        print("Enter your equation: ")
        inp = input()
        inp = inp.replace(' ', '')
        current = inp[current_index]
        print('Result: ' + e())
        print('\n')
