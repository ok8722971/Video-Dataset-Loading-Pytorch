import os

src = "../../HMDB_IMG/train_img"

txt_path = os.path.join(src, "annotations.txt")

with open(txt_path, 'w') as f:
    class_names = sorted(os.listdir(src))
    label = 0
    for c in class_names:
        class_path = os.path.join(src, c)
        if not os.path.isdir(class_path) :
            continue
        files = sorted(os.listdir(class_path))
        for file in files:
            file_path = os.path.join(class_path, file)
            file_root = c + '/' + file
            last_idx = len([name for name in os.listdir(file_path)]) - 1
            f.write(file_root + " 0 " + str(last_idx) + " " + str(label) + '\n')
        print("done " + c + " annotations")
        label += 1

