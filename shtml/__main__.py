from tools.compiler import Compiler


def main():
    compiler = Compiler()
    compiler.compile('shtml/tests/index.shtml')

if __name__ == '__main__':
    main()