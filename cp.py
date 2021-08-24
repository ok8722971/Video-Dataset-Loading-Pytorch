import shutil
import os


# video src dir
src = "../../HMDB/test3"

# video dst dir
dst = "../../HMDB_IMG/test"

# video type
file_extension = ".avi"

# video file name template
video_file_template = '{:05d}' + file_extension


dirs = os.listdir(src)
for directory in dirs:
    dir_path = os.path.join(src, directory)
    files = os.listdir(dir_path)
    # check if the dst folder exists
    # if not then create one
    dst_dir_path = os.path.join(dst, directory)
    if not os.path.isdir(dst_dir_path):
        print("destination directory not exist creating one")
        os.mkdir(dst_dir_path)
        print("created")
        idx = 1
    else:
        print("destination directory already exists")
        # findout the max number in destination directory
        idx = int(max(os.listdir(dst_dir_path))[:5]) + 1

    
    
    for file in files:
        file_path = os.path.join(dir_path, file)
        dst_file_path = os.path.join(dst_dir_path, video_file_template.format(idx))
        shutil.copyfile(file_path, dst_file_path)
        idx += 1
    print("done " + directory)        
    
