# Using EPIC-KITCHENS-100
This directory contains pre-made annotation files to use the [EPIC-KITCHENS-100](https://epic-kitchens.github.io/2021) dataset with this 
repository's VideoFrameDataset dataloader. The two `.txt` files in this directory are the training and validation annotation files that you can use for EPIC-KITCHENS-100 with VideoFrameDataset. That's it! Reading `(1) Dataset Overview` below can also help you understand the EPIC-KITCHENS-100 files.

If you need/want to recreate these processed annotation files yourself, read the rest of this README below.

### 1. Dataset Overview
When you download the EPIC-KITCHENS-100 dataset, it comes in the following format:
- A folder containing jpeg RGB frames for each video
- A `.csv` file for the training annotations and the validation annotations

To use VideoFrameDataset with EPIC-KITCHENS-100, we need to
1. Turn the `.csv` file into an `annotations.txt` file, as described in the main README of this repository.

### 2. Processing
Doing (1) from above, is very easy if you use the python script provided in this directory.
- For (1), run the script `original_annotations_to_processed_annotations.py` and make sure that you
set the file paths correctly inside of the script. Run this script once for training and once for validation 
annotations.

### 3. Done
That's it! You should then have a folder on your disk `RGB` that contains all videos in individual RGB
frames, and the two annotation files. This is all you need to use VideoFrameDataset and start training
on EPIC-KITCHENS-100!
