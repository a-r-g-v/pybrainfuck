import sys
sys.setrecursionlimit(3000)

def parse(code, code_ptr, buf, buf_ptr, loop):
    
    try:
        op = code[code_ptr]
    except IndexError:
        # finish
        return
    
    if op == '>':
        buf_ptr += 1

    elif op == '<':
        buf_ptr -= 1

    elif op == '+':
        buf[buf_ptr] += 1

    elif op == '-':
        buf[buf_ptr] -= 1
    
    elif op == '.':
        sys.stdout.write(chr(buf[buf_ptr]))

    elif op == ',':
        buf[buf_ptr] = sys.stdin.read(1)

    elif op == '[':
        if buf[buf_ptr] == 0:
            save_loop = loop
            while 1:
                if code[code_ptr] == '[':
                    loop += 1
                elif code[code_ptr] == ']':
                    loop -= 1
                    if save_loop == loop:
                        code_ptr += 1
                        break
                code_ptr += 1

    elif op == ']':
        if buf[buf_ptr] != 0:
            save_loop = loop
            while 1:
                if code[code_ptr] == ']':
                    loop += 1
                elif code[code_ptr] == '[':
                    loop -= 1
                    if save_loop == loop:
                        code_ptr -= 1
                        break
                code_ptr -= 1

    code_ptr += 1
    return parse(code, code_ptr, buf, buf_ptr, loop)


def run(code):
    parse(code, 0, [0]*30000, 0, 0)
