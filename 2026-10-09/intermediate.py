​with open("song.txt", "w") as f:
    verses = int(input("How many verses?\n> "))
    for bottles in range(verses, 0, -1):
        bottles_str = "bottles" if bottles != 1 else "bottle"
        f.write(f"""{bottles} {bottles_str} of beer on the wall
{bottles} {bottles_str} of beer
Take one down, pass it around
{("No more" if bottles == 1 else bottles-1)} {("bottles" if bottles != 2 else "bottle")} of beer on the wall{("\n\n" if bottles != 1 else "")}""")