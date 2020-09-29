songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0])
print(songs[2])
print(songs[1:3])
songs[2] = "We Paid"
print(songs)
songs.extend(["Come & Go", "Martin & Gina", "bloody valentine"])
del songs[1]

animals = ["wolf", "lion", "shark"]
animals.append("bear")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)