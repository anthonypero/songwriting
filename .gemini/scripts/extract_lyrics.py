import re
import argparse
import os

def extract_lyrics_from_chordpro(input_file_path: str, output_file_path: str):
    """
    Extracts lyrics from a ChordPro file, removing all ChordPro-specific elements,
    and writes the clean lyrics to a new text file.

    Args:
        input_file_path: Path to the input ChordPro file.
        output_file_path: Path to the output text file for lyrics.
    """
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            chordpro_content = f.read()

        lines = chordpro_content.strip().split('\n')
        lyrics_lines = []

        for i, line in enumerate(lines):
            # First, handle comment tags: {comment: Some Header} -> [Some Header]
            comment_match = re.search(r'\{comment:\s*(.*?)\}', line)
            if comment_match:
                comment_text = comment_match.group(1).strip()
                processed_line = f"[{comment_text}]"
            else:
                # Remove other ChordPro metadata tags (e.g., {title: ...}, {artist: ...})
                processed_line = re.sub(r'\{[^}]*\}', '', line)
                # Remove ChordPro chord notations [C]
                processed_line = re.sub(r'\[[^\]]*\]', '', processed_line)
            
            processed_line = processed_line.strip()

            if processed_line:
                # Add a newline before headings, unless it's the very first line
                # A heading is identified as a line starting with '[' and ending with ']'
                is_heading = processed_line.startswith('[') and processed_line.endswith(']') and len(processed_line) > 2
                
                # Check if it's a heading, not the first line, and the last appended line isn't already empty
                if is_heading and lyrics_lines and not (lyrics_lines[-1].strip() == ''):
                    lyrics_lines.append('') # Add an empty line before the heading
                
                lyrics_lines.append(processed_line)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lyrics_lines))
        
        print(f"Successfully extracted lyrics from '{input_file_path}' to '{output_file_path}'")

    except FileNotFoundError:
        print(f"Error: File not found at '{input_file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract lyrics from a ChordPro file.')
    parser.add_argument('input_file', type=str, help='Path to the input ChordPro file.')
    parser.add_argument('output_file', type=str, help='Path to the output lyrics file.')
    
    args = parser.parse_args()

    # Ensure the output directory exists
    output_dir = os.path.dirname(args.output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    extract_lyrics_from_chordpro(args.input_file, args.output_file)
