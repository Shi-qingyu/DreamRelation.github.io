import os


root = "benchmark"
for dir in os.listdir(root):
    dir_path = os.path.join(root, dir)
    if os.path.isdir(dir_path):
        for image_name in os.listdir(dir_path):
            old_image_name = image_name
            # if "JPG" in image_name:
            #     new_image_name = image_name.replace("JPG", "jpg")
            # elif "png" in image_name:
            #     new_image_name = image_name.replace("png", "jpg")
            # elif "jpeg":
            #     new_image_name = image_name.replace("jpeg", "jpg")
            # else:
            #     assert "jpg" in image_name, f"{dir_path}, {image_name} is unexpected"
            #     new_image_name = image_name
                
            # os.rename(os.path.join(dir_path, old_image_name), os.path.join(dir_path, new_image_name))
                
            if any([old_image_name in str(i) + ".jpg" for i in range(len(os.listdir(dir_path)))]):
                continue
            
            for i in range(len(os.listdir(dir_path))):
                new_image_path = os.path.join(dir_path, f"{i}.jpg")
                if os.path.exists(new_image_path):
                    continue
                else:              
                    os.rename(os.path.join(dir_path, old_image_name), new_image_path)
                    break