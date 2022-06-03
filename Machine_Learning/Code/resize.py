# This code is used to resize image to 300, 300
# Import Library
import os
from pathlib import Path
from PIL import Image

# Path File (Change if needed)
path_folder = "E:/Kuliah/bangkit/Project_Capstone/Dataset/pm"
path_train_Good = "E:/Kuliah/bangkit/Project_Capstone/Dataset/pm/Dataset/Good"
path_train_Moderate = "E:/Kuliah/bangkit/Project_Capstone/Dataset/pm/Dataset/Moderate"
path_train_Dangerous = "E:/Kuliah/bangkit/Project_Capstone/Dataset/pm/Dataset/Dangerous"
resize_str_good = "/resize/Good/"
resize_str_moderate = "/resize/Moderate/"
resize_str_dangerous = "/resize/Dangerous/"

# Resize Good quality image
for i in os.listdir(path_train_Good):
    im = Image.open(path_train_Good + "/" + i)
    im = im.convert("RGB")
    im = im.resize((300,300))
    im.save(path_folder + resize_str_good + Path(i).stem + ".jpg")

# Resize Moderate quality image
for i in os.listdir(path_train_Moderate):
    im = Image.open(path_train_Moderate + "/" + i)
    im = im.convert("RGB")
    im = im.resize((300,300))
    im.save(path_folder + resize_str_moderate + Path(i).stem + ".jpg")

# Resize Dangerous quality image
for i in os.listdir(path_train_Dangerous):
    im = Image.open(path_train_Dangerous + "/" + i)
    im = im.convert("RGB")
    im = im.resize((300,300))
    im.save(path_folder + resize_str_dangerous + Path(i).stem + ".jpg")