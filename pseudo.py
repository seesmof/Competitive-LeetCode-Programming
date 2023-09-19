artists = {
    "radiohead": 156,
    "the black keys": 35,
    "the strokes": 61,
    "red hot chilli pepper": 231,
    "nirvana": 176,
}
res = []

while artists:
    maxValue = max(artists.values())
    res.append(maxValue)

    maxKey = [key for key, value in artists.items() if value == maxValue][0]

    del artists[maxKey]

print(res)
