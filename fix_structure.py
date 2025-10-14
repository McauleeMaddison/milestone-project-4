import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Move internal icedinsights/ folder up if needed
def fix_nested_icedinsights():
    nested = os.path.join(BASE_DIR, "icedinsights", "icedinsights")
    if os.path.exists(nested):
        for file in os.listdir(nested):
            shutil.move(os.path.join(nested, file), os.path.join(BASE_DIR, "icedinsights", file))
        os.rmdir(nested)
        print("✅ Flattened nested icedinsights folder.")

# Move templates/ from dashboard to root if needed
def move_templates_to_root():
    old_templates = os.path.join(BASE_DIR, "dashboard", "templates")
    new_templates = os.path.join(BASE_DIR, "templates")
    if os.path.exists(old_templates) and not os.path.exists(new_templates):
        shutil.move(old_templates, new_templates)
        print("✅ Moved templates to root.")

# Move static/ from dashboard to root if needed
def move_static_to_root():
    old_static = os.path.join(BASE_DIR, "dashboard", "static")
    new_static = os.path.join(BASE_DIR, "static")
    if os.path.exists(old_static) and not os.path.exists(new_static):
        shutil.move(old_static, new_static)
        print("✅ Moved static to root.")

# Ensure media/ exists
def ensure_media_folder():
    media_dir = os.path.join(BASE_DIR, "media")
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)
        print("✅ Created media/ folder.")

# Run all
fix_nested_icedinsights()
move_templates_to_root()
move_static_to_root()
ensure_media_folder()

print("✅ Folder structure cleanup complete.")