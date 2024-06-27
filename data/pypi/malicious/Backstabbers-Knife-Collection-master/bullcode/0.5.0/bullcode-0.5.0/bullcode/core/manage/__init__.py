def main(argv=None):
    from bullcode.cmp import Compiler
    import sys

    comp = Compiler(config=sys.argv[sys.argv.index("--config") + 1])
    comp.run(open(sys.argv[1]).read())