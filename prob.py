import sys
import collections

def main():
    '''
    Read's each line and obtains the words, separated by spaces and
    places in dictionary (wordcount).
    Case and punctuation are distinct.
    '''
    with open(sys.argv[1],"r") as f:
        words = collections.Counter(f.read().split())
    print(words)

    f.close()

if __name__ == '__main__':
   main()
