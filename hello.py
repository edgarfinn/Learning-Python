import sys

def main():
    print sys.argv
    argumentsLength = len(sys.argv)
    print 'argumentLength:', argumentsLength
    if argumentsLength > 1:
        print 'first argument:', sys.argv[1]

if __name__ == '__main__':
    main()
