
import brainfuck 


brainfuck.run("+" * 49 + ".")

brainfuck.run(".[.[-.].].")

hello_world = """
+++++++++[>++++++++>+++++++++++>+++++<<<-]>.>++.+++++++..+++.>-.
------------.<++++++++.--------.+++.------.--------.>+.
"""

brainfuck.run(hello_world)
