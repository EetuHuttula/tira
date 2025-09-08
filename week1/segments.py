### HUOM!! TEHTÄVÄ ON JAKAA SEGMENTTEIHIN, LASKEA SEGMENTIN PITUUS JA ALOITTAA UUSI SEGMENTTI KIRJAIMEN VAIHDUTUESSA SIKSI OUTPUT MMZXZJ FAILAA 
### DICTIONARY EI TOIMI TÄMÄN TAKIA TÄSSÄ TEHTÄVÄSSÄ SILLÄ SIIHEN KELPAA VAIN UNIIKIT AVAIN VALUET.

def find_segments(data):
    list = []
    lenght = 0
    previus_charr = data[0]
    for char in data:
            if char!= previus_charr:
                list.append((lenght, previus_charr))
                lenght = 1       
                previus_charr = char
            else:
                lenght += 1
    list.append((lenght, previus_charr))
    return list

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]
    print(find_segments("rwlssxfykm"))
    # [(1, 'r'), (1, 'w'), (1, 'l'), (2, 's'), (1, 'x'), (1, 'f'), (1, 'y'), (1, 'k'), (1, 'm')]