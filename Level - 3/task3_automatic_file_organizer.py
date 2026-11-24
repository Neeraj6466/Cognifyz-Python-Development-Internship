
# Cognifyz Internship
# Level 3 - Task 3
# Automatic File Organizer

import shutil
from pathlib import Path

print("===== AUTOMATIC FILE ORGANIZER =====")

# Get folder path from user
folder_path = input("Enter folder path to organize: ")

folder = Path(folder_path)

# Check whether folder exists
if not folder.exists() or not folder.is_dir():
    print("Invalid folder path!")

else:
    # File categories
    categories = {
        "PDF Files": [".pdf"],
        "Images": [".jpg", ".jpeg", ".png"],
        "Text Files": [".txt"],
        "Documents": [".doc", ".docx"],
        "Others": []
    }

    # Create destination folders
    for category in categories:
        (folder / category).mkdir(exist_ok=True)

    # Organize files
    for file in folder.iterdir():

        if file.is_file():

            extension = file.suffix.lower()

            destination_folder = "Others"

            for category, extensions in categories.items():
                if extension in extensions:
                    destination_folder = category
                    break

            destination = folder / destination_folder / file.name

            # Avoid overwriting files with the same name
            counter = 1

            while destination.exists():
                new_name = f"{file.stem}_{counter}{file.suffix}"
                destination = folder / destination_folder / new_name
                counter += 1

            shutil.move(str(file), str(destination))

            print("Moved:", file.name, "to", destination_folder)

    print("\nFile organization completed!")
