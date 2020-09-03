from PIL import Image
import os, glob
import numpy as np
 
folder_Afghan_Hound = ["./drive/My Drive/0/Afghan Hound"]
folder_Chihuahua = ["./drive/My Drive/0/Chihuahua"]
folder_Cookie = ["./drive/My Drive/0/Cookie"]
folder_Fried_Chicken = ["./drive/My Drive/0/Fried Chicken"]
folder_Labradoodle = ["./drive/My Drive/0/Labradoodle"]
folder_Mop = ["./drive/My Drive/0/Mop"]
folder_Muffin = ["./drive/My Drive/0/Muffin"]
folder_Puppy = ["./drive/My Drive/0/Puppy"]
folder_Saruman = ["./drive/My Drive/0/Saruman"]
folder_Sheepdog = ["./drive/My Drive/0/Sheepdog"]
folder_Teddy_Bear = ["./drive/My Drive/0/Teddy Bear"]
image_size = 224
 
X_Afghan_Hound = []
X_Chihuahua = []
X_Cookie = []
X_Fried_Chicken = []
X_Labradoodle = []
X_Mop  = []
X_Muffin = []
X_Puppy = []
X_Saruman = []
X_Sheepdog = []
X_Teddy_Bear = []
#1
for index, name in enumerate(folder_Afghan_Hound):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Afghan_Hound.append(data)
 
X_Afghan_Hound = np.array(X_Afghan_Hound)
#2
for index, name in enumerate(folder_Chihuahua):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Chihuahua.append(data)
 
X_Chihuahua = np.array(X_Chihuahua)
#3
for index, name in enumerate(folder_Cookie):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Cookie.append(data)
 
X_Cookie = np.array(X_Cookie)
#4
for index, name in enumerate(folder_Fried_Chicken):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Fried_Chicken.append(data)
 
X_Fried_Chicken = np.array(X_Fried_Chicken)
#5
for index, name in enumerate(folder_Labradoodle):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Labradoodle.append(data)
 
X_Labradoodle = np.array(X_Labradoodle)
#6
for index, name in enumerate(folder_Mop):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Mop.append(data)
 
X_Mop = np.array(X_Mop)
#7
for index, name in enumerate(folder_Muffin):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Muffin.append(data)
 
X_Muffin = np.array(X_Muffin)
#8
for index, name in enumerate(folder_Puppy):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Puppy.append(data)
 
X_Puppy = np.array(X_Puppy)
#9
for index, name in enumerate(folder_Saruman):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Saruman.append(data)
 
X_Saruman = np.array(X_Saruman)
#10
for index, name in enumerate(folder_Sheepdog):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Sheepdog.append(data)
 
X_Sheepdog = np.array(X_Sheepdog)
#11
for index, name in enumerate(folder_Teddy_Bear):
    dir = "./" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
 
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X_Teddy_Bear.append(data)
 
X_Teddy_Bear = np.array(X_Teddy_Bear)
