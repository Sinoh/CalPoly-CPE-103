import sys
from linked_list import *
#from array_list import *

class song():
    def __init__(self, title, artist, album, number):
        self.title = title
        self.artist = artist
        self.album = album
        self.number = number

    def __repr__ (self):
        return "%s, %s, %s, %s" % (self.title, self.artist, self.album, self.number)

    def __eq__(self, other):
        if isinstance(other, song):
            return self.title == other.title and self.artist == other.artist and self.album  == other.album and self.number == other.number
        else:
            return False



def main():
    # Opens the text file
    input1 = open(sys.argv[1], 'r')

    # Add songs from a text file into an empty list
    list = empty_list()
    index = 0
    linenumber = 1
    error = False
    for line in input1:
        line2 = line.rstrip().split('--')
        if len(line2) != 3:
            if error == False:
                print('Catalog input errors:')
                error = True
            if line2 != ['']:
                print('line', linenumber,': malformed song information')
            linenumber += 1
            continue
        _song = song(line2[0],line2[1],line2[2], index)
        list = add(list, index, _song)
        linenumber += 1
        index += 1

    input1.close()

    catalog(list)

# The menu the user can choose from
# Asks for an input, and brings up functions depending on that input
def catalog(list, key = None):
    Quit = False
    while Quit == False:
        print('\nSong Catalog')
        print('   1) Print Catalog')
        print('   2) Song Information')
        print('   3) Sort')
        print('   4) Add Songs')
        print('   0) Quit')
        sys.stdout.write('Enter selection: ')
        sys.stdout.flush()
        choice = int(sys.stdin.readline())

        # Prints list of songs to screen
        if choice == 1:
            for i in range(length(list)):
                line = get(list, i)
                print(str(line.number) + '--' + line.title + '--' + line.artist + '--' + line.album)

        # Ask for Song number to bring up the information about a song
        # Prints song information onto screen
        elif choice == 2:
            sys.stdout.write('Enter song number: ')
            sys.stdout.flush()
            snum = int(sys.stdin.readline())

            if length(list)-1 < snum or snum < 0:
                print('\n... Invalid song number')

            for i in range(length(list)):
                line = get(list, i)
                if line.number == snum:
                    print('\nSong information ...')
                    print('   Number:', line.number)
                    print('   Title:', line.title)
                    print('   Artist:', line.artist)
                    print('   Album:', line.album)

        # Prompts another input
        # Sorts the song based on that input
        elif choice == 3:
            print('\nSort songs')
            print('   0) Number')
            print('   1) Title')
            print('   2) Artist')
            print('   3) Album')
            sys.stdout.write('\nSort by: ')
            sys.stdout.flush()
            key = int(sys.stdin.readline())
            order = find_key(key)
            temp = (sort(list, func_test), key)
            list = temp[0]
            key = temp[1]

        # Adds more songs based on an input
        # Requires a file name within the same directory
        elif choice == 4:
            list = add_song(list,key)

        # Exits the program
        elif choice == 0:
            exit()
        else:
            print('\nInvalid Option')

def add_song(list, key = None):
    sys.stdout.write('Enter name of file to load: ')
    sys.stdout.flush()
    newinput = sys.stdin.readline().rstrip()
    try:
        newfile = open(newinput)
    except IOError:
        print("\n'%s'" % newinput + ': No such file or directory')
        return catalog(list, key)
    for line in newfile:
        line2 = line.rstrip().split('--')
        if len(line2) != 3:
            continue
        _song = song(line2[0], line2[1], line2[2], index)
        list = add(list, index, _song)
        index += 1
    newfile.close()
    if key == None:
        return list
    else:
        order = find_key(key)
        return sorting(list, order)


if __name__ == '__main__':
    main()

