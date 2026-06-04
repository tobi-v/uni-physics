import os

def change_extension(directory, old_ext, new_ext):
    """Change file extensions from old_ext to new_ext in the specified directory."""
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            new_filename = filename.replace(old_ext, new_ext)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)