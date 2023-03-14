def is_letter_aeiou(letter):
    if letter == 'a':
        return True
    elif letter == 'e':
        return True
    elif letter == 'i':
        return True
    elif letter == 'o':
        return True
    elif letter == 'u':
        return True
    else:
        return False


def abanibi_song(song):
    new_song = ''
    for i in range(len(song)):
        new_song = new_song + song[i]
        if is_letter_aeiou(song[i]):
            new_song = new_song + 'b' + song[i]
    return new_song

def abanibi_fancy(song):
    if 'a' in song:
        song=song.replace('a','aba')
    if 'e' in song:
        song = song.replace('e', 'ebe')
    if 'i' in song:
        song = song.replace('i', 'ibi')
    if 'o' in song:
        song = song.replace('o', 'obo')
    if 'u' in song:
        song = song.replace('u', 'ubu')
    return song



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    song = input("enter your song man:\n")
    new_song = abanibi_song(song)
    print(new_song)
    new_song = abanibi_song(song)
    print(new_song)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
