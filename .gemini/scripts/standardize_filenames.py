import os
import re
import argparse
import shutil

def get_song_dirs(root_dir):
    """Get all immediate subdirectories that are song folders."""
    song_dirs = []
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        if os.path.isdir(path) and not item.startswith('.') and item != 'audio':
            song_dirs.append(path)
    return song_dirs

def generate_slug(title):
    """Generate a standardized slug from a song title."""
    # Convert to lowercase
    slug = title.lower()
    # Remove non-alphanumeric characters (except spaces and dashes)
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    # Replace spaces and multiple dashes with a single dash
    slug = re.sub(r'[\s-]+', '-', slug)
    # Remove leading/trailing dashes
    slug = slug.strip('-')
    return slug

def get_title_from_chordpro(chordpro_file):
    """Extract the title from a .chordpro file."""
    try:
        with open(chordpro_file, 'r', encoding='utf-8') as f:
            for line in f:
                line_s = line.strip()
                if line_s.lower().startswith('{title:') or line_s.lower().startswith('{t:'):
                    content = line_s[line_s.find(':')+1:]
                    title = content.rstrip('}').strip()
                    return title
    except FileNotFoundError:
        return None
    return None

def plan_song_directory_updates(song_dir):
    """Analyzes a song directory and returns a plan of operations."""
    operations = {
        "dir_rename": None,
        "file_renames": [],
        "meta_update": None
    }

    # Find the .chordpro file
    chordpro_file = None
    for item in os.listdir(song_dir):
        if item.lower().endswith('.chordpro'):
            chordpro_file = os.path.join(song_dir, item)
            break
    
    if not chordpro_file:
        print(f"\nSkipping: {os.path.basename(song_dir)} (No .chordpro file found)")
        return None

    # Get title and generate new slug
    title = get_title_from_chordpro(chordpro_file)
    if not title:
        print(f"\nSkipping: {os.path.basename(song_dir)} (Could not find title)")
        return None
    
    new_slug = generate_slug(title)
    old_slug_from_file = os.path.basename(chordpro_file).replace('.chordpro', '')
    
    print(f"\nProcessing: {os.path.basename(song_dir)}")
    print(f"  - Title: '{title}' -> Slug: '{new_slug}'")

    # --- Plan File Renames ---
    if new_slug != old_slug_from_file:
        for filename in os.listdir(song_dir):
            if filename.startswith(old_slug_from_file):
                suffix = filename[len(old_slug_from_file):]
                new_filename = new_slug + suffix
                old_path = os.path.join(song_dir, filename)
                new_path = os.path.join(song_dir, new_filename)
                if old_path != new_path:
                    operations["file_renames"].append((old_path, new_path))

    # --- Plan Meta Slug Update ---
    # We need to determine the final path of the chordpro file after renaming
    final_chordpro_path = chordpro_file
    for old_p, new_p in operations["file_renames"]:
        if old_p == chordpro_file:
            final_chordpro_path = new_p
            break
    operations["meta_update"] = (final_chordpro_path, new_slug)

    # --- Plan Directory Rename ---
    old_dir_path = song_dir
    new_dir_path = os.path.join(os.path.dirname(song_dir), new_slug)
    if old_dir_path != new_dir_path:
        operations["dir_rename"] = (old_dir_path, new_dir_path)
        
    return operations

def execute_plan(plan, dry_run=True):
    """Executes the planned operations."""
    # 1. Execute file renames
    if plan.get("file_renames"):
        for old_path, new_path in plan["file_renames"]:
            print(f"  - RENAME FILE: {os.path.basename(old_path)} -> {os.path.basename(new_path)}")
            if not dry_run:
                try:
                    os.rename(old_path, new_path)
                except Exception as e:
                    print(f"    - ERROR: {e}")

    # 2. Execute meta slug update
    if plan.get("meta_update"):
        chordpro_file, new_slug = plan["meta_update"]
        # In case the file was renamed, we need to use its new path for the update
        if not dry_run:
             for old_p, new_p in plan.get("file_renames", []):
                if old_p == chordpro_file:
                    chordpro_file = new_p
                    break
        
        try:
            with open(chordpro_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            updated = False
            for i, line in enumerate(lines):
                if line.strip().lower().startswith('{meta: slug'):
                    old_slug_line = line.strip()
                    new_slug_line = f"{{meta: slug {new_slug}}}"
                    if old_slug_line != new_slug_line:
                        print(f"  - UPDATE META: {os.path.basename(chordpro_file)} -> {new_slug_line}")
                        if not dry_run:
                            lines[i] = new_slug_line + '\n'
                            updated = True
                    break
            
            if updated and not dry_run:
                with open(chordpro_file, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
        except Exception as e:
            print(f"  - ERROR updating meta in {os.path.basename(chordpro_file)}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Standardize song filenames and directories based on .chordpro title.")
    parser.add_argument("root_dir", help="The root directory containing all the song folders.")
    parser.add_argument("--execute", action="store_true", help="Execute the renames. Default is a dry run.")
    args = parser.parse_args()

    if not args.execute:
        print("--- DRY RUN MODE ---")
        print("No files will be renamed or moved. Run with --execute to apply changes.")

    song_dirs = get_song_dirs(args.root_dir)
    all_plans = []
    for song_dir in sorted(song_dirs):
        plan = plan_song_directory_updates(song_dir)
        if plan:
            all_plans.append(plan)

    # Execute file-level changes first
    for plan in all_plans:
        execute_plan(plan, dry_run=not args.execute)

    # Execute directory renames last
    print("\n--- Directory Renames ---")
    for plan in all_plans:
        if plan.get("dir_rename"):
            old_dir, new_dir = plan["dir_rename"]
            print(f"  - RENAME DIR: {os.path.basename(old_dir)} -> {os.path.basename(new_dir)}")
            if not args.execute:
                # Dry run check for existing target
                if os.path.exists(new_dir) and old_dir.lower() != new_dir.lower():
                     print(f"    - WARNING: Target '{os.path.basename(new_dir)}' already exists. Rename would fail.")
            else:
                # Execute run
                try:
                    # Handle case-only renames on case-insensitive filesystems
                    if old_dir.lower() == new_dir.lower() and old_dir != new_dir:
                        temp_dir = old_dir + "_temp_rename"
                        shutil.move(old_dir, temp_dir)
                        shutil.move(temp_dir, new_dir)
                    else:
                        shutil.move(old_dir, new_dir)
                except Exception as e:
                    print(f"    - ERROR: {e}")

    print("\n--- Finished ---")

if __name__ == "__main__":
    main()