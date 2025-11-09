import os
import json
import re

def build_song_index():
    """
    Scans the Songwriting directory for .chordpro files, parses them for metadata,
    and builds a JSON index file based on the slug.
    """
    songwriting_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    song_index = []
    
    directive_regex = re.compile(r'\{([^:]+):\s*(.*?)\s*\}', re.IGNORECASE)
    desired_keys = {'title', 'artist', 'composer', 'lyricist', 'copyright', 'key', 'tempo', 'tag', 'slug', 'meta'}

    for root, _, files in os.walk(songwriting_dir):
        if '.gemini' in root:
            continue

        for file in files:
            if file.lower().endswith('.chordpro'):
                file_path = os.path.join(root, file)
                
                song_data = {
                    "folder": os.path.basename(root),
                    "slug": "",
                    "title": "",
                    "artist": "",
                    "composer": "",
                    "lyricist": "",
                    "copyright": "",
                    "key": "",
                    "tempo": "",
                    "tags": []
                }

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            match = directive_regex.match(line)
                            if match:
                                key = match.group(1).strip().lower()
                                value = match.group(2).strip()

                                if key in desired_keys:
                                    if key == 'tag' or key == 'tags':
                                        if value:
                                            tags = [tag.strip() for tag in value.split(',')]
                                            song_data["tags"].extend(tags)
                                    # The slug is now the primary identifier
                                    elif key == 'meta' and value.lower().startswith('slug '):
                                        song_data['slug'] = value[5:].strip()
                                    elif key == 'slug': # Also handle a direct {slug: ...}
                                         song_data['slug'] = value
                                    else:
                                        song_data[key] = value
                
                except Exception as e:
                    print(f"Error reading or parsing {file_path}: {e}")
                    continue

                # Only add songs that have a slug
                if song_data["slug"]:
                    song_index.append(song_data)

    song_index.sort(key=lambda x: x['slug'])
    output = {"songs": song_index}
    output_path = os.path.join(songwriting_dir, '.gemini', 'song_index.json')

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2)
        print(f"Successfully created song index at {output_path}")
    except Exception as e:
        print(f"Error writing JSON index file: {e}")

if __name__ == "__main__":
    build_song_index()
