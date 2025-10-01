# File Organizer Script

# ---------- Modules ----------
import os # for file handling
import shutil # for moving files

# ---------- Categories ----------
Categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".cs"],
}

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("\n---------- ❌ Folder path does not exist. ----------")
        return
    else:
        print(f"\n---------- 📂 Organizing files in {folder_path} ----------\n")

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # skip if it's a folder
            if os.path.isdir(file_path):
                continue

            # separate file name and its extension
            ext = os.path.splitext(filename)[1].lower()

            moved = False # it's a flag variable

            # find category
            for category, extensions in Categories.items():
                if ext in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)

                    #file move
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"✅ {filename} -> {category}/")
                    moved = True
                    break

            # if ext in not ion extensions
            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"✅ {filename} -> Others/")

        print("\n🎉 Organizing complete!")

# ---------- Run ----------
if __name__ == "__main__":
   print("\n---------- 📂File Organizer Script ----------\n")
   folder = input("Enter the folder path to organize: ").strip() # remove starting and ending spaces
   confirm = input(f"Do you want to organize files in '{folder}'? (y/n) ").lower()
   if confirm == "y":
       organize_folder(folder)
   else:
    print("\n---------- ❌ Operation cancelled. ----------")

