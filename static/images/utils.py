import os
import shutil
import numpy as np


with open("mvimgnet_category.txt", "r") as file:
    lines = file.read().splitlines()

idx2name = {}
for line in lines:
    idx, name = line.split(",")
    idx2name[idx] = name.lower()


def recurssive_extract(dir):
    if os.path.isdir(dir) and os.path.basename(dir) == "images":
        image_names = os.listdir(dir)
        image_ids = np.random.choice(len(image_names), size=2, replace=False)
        picked_image_names = [image_names[int(image_idx)] for image_idx in image_ids]
        for image_name in image_names:
            if image_name not in picked_image_names:
                image_path = os.path.join(dir, image_name)
                os.remove(image_path)
    elif os.path.isdir(dir) and os.path.basename(dir) == "sparse":
        shutil.rmtree(dir)
    elif os.path.isdir(dir):
        for sub in os.listdir(dir):
            recurssive_extract(os.path.join(dir, sub))
    else:
        return None

def move_dir(src_root, dst_root):
    for dir in os.listdir(src_root):
        src_dir_path = os.path.join(src_root, dir)
        tar_dir_path = os.path.join(dst_root, dir)
        if not os.path.exists(tar_dir_path):
            os.makedirs(tar_dir_path)
        for subdir in os.listdir(src_dir_path):
            src_path = os.path.join(src_dir_path, subdir)
            tar_path = os.path.join(tar_dir_path, subdir)
            shutil.move(src_path, tar_path)

move_dir("mvi_42", "mvi_26")