import sys

def repeat(s, exclaim):
  """
  Returns a string 's' three times.
  If exclaim = true, add three exclamation marks.
  """
  result = s + s + s
  if exclaim == True:
    result = result + '!!!'
  return result

def main():
    myStr = sys.argv[1]
    myBool = sys.argv[2]
    print repeat(myStr, myBool)

if __name__ == '__main__':
    main()
