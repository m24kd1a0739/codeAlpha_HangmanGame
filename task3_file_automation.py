# CodeAlpha Task 3: File Automation
# Move all JPG files from one folder to another

import os
import shutil

# Folder names
source_folder = "images"
destination_folder = "jpg_files"

# Create folders if they don't exist
if not os.path.exists(source_folder):
    os.makedirs(source_folder)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

print("======================================")
print("        JPG FILE AUTOMATION")
print("======================================")

# Find JPG files
jpg_files = []

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        jpg_files.append(file)

# Check if files are available
if len(jpg_files) == 0:
    print("No JPG files found in the images folder.")

else:
    print(f"Found {len(jpg_files)} JPG file(s).")

    # Move JPG files
    for file in jpg_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")

    print("\nAll JPG files moved successfully!")

print("======================================")
