
import brainfuck 


hello_world = """
+++++++++[>++++++++>+++++++++++>+++++<<<-]>.>++.+++++++..+++.>-.
------------.<++++++++.--------.+++.------.--------.>+.
"""

brainfuck.run(hello_world)

code = brainfuck.unrolling(hello_world)
code.remove("\n")
code = "".join(code)

brainfuck.run(hello_world)


