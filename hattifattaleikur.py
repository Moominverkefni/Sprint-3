from random import randint

hnitakerfi = []

for x in range(6):
    hnitakerfi.append(["O"] * 6)

def print_hnitakerfi(hnitakerfi):
    for row in hnitakerfi:
        print((" ").join(row))

print("Spilum Hattífattaleikinn! \nHattífattarnir eru að fela sig undir moldinni og þú átt að giska á reiti og reyna að finna þá. \nÞú getur unnið leikinn með því að finna hattífattann. \nÞú hefur þó aðeins 10 tilraunir til að giska á staðsetningu hattífattanna.")
print_hnitakerfi(hnitakerfi)

def random_row(hnitakerfi):
    return randint(0, len(hnitakerfi) - 1)
def random_col(hnitakerfi):
    return randint(0, len(hnitakerfi[0]) - 1)

hattifatta_lina1 = random_row(hnitakerfi)
hattifatta_dalkur1 = random_col(hnitakerfi)
#hattifatta_lina2 = random_row(hnitakerfi)
#hattifatta_dalkur2 = random_col(hnitakerfi)

for turn in range(11):
    print ("Reyndu aftur"), turn
    guess_row = int(input("Giskið á línu (línur 0-5):"))
    guess_col = int(input("Giskið á dálk (dálkar 0-5):"))

    if (guess_row == hattifatta_lina1 and guess_col == hattifatta_dalkur1):
        print("Til hamingju, þú náðir hattífattanum og vannst leikinn!")
        hnitakerfi[guess_row][guess_col] = "H"
        print_hnitakerfi(hnitakerfi)
        #her kemur gif af moomin ad vinna....
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("Obbosí, þú hittir út fyrir reitinn")
        elif(hnitakerfi[guess_row][guess_col] == "X"):
            print("Þú hefur nú þegar giskað á þennan reit.")
        else:
            print("Þú hittir engan hattífatta")
            hnitakerfi[guess_row][guess_col] = "X"
    if turn == 10:
        print("Þú tapaðir leiknum :(")
        hnitakerfi[hattifatta_lina1][hattifatta_dalkur1] == "H"
        print_hnitakerfi(hnitakerfi)
        #her kemur gif af moomin ad tapa...
        break
        turn =+ 1
    print_hnitakerfi(hnitakerfi)
