import os
from PIL import Image

# Get the directory where the script itself is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configuration using absolute paths
WIDTH, HEIGHT = 96, 16
MSG_FILE = os.path.join(BASE_DIR, "message.png")
CURSOR_FILE = os.path.join(BASE_DIR, "cursor.png")
OUTPUT_DIR = os.path.join(BASE_DIR, "frames_generated")

cursor_offsets = [4, 14, 22, 26, 30, 38, 42, 47, 59, 67, 75, 79, 88, 91, 96]

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def create_frames():
    if not os.path.exists(MSG_FILE) or not os.path.exists(CURSOR_FILE):
        print(f"--- ERROR ---")
        print(f"Looking in: {BASE_DIR}")
        print(f"Found files: {os.listdir(BASE_DIR)}")
        print(f"Missing: {'message.png' if not os.path.exists(MSG_FILE) else ''} "
              f"{'cursor.png' if not os.path.exists(CURSOR_FILE) else ''}")
        return

    message = Image.open(MSG_FILE).convert("RGBA")
    cursor = Image.open(CURSOR_FILE).convert("RGBA")

    for i, x_pos in enumerate(cursor_offsets):
        frame = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 255))
        frame.paste(message, (0, 0), message)
        # Paste cursor at the specific x_pos
        frame.paste(cursor, (x_pos, 0), cursor)
        
        final_frame = frame.convert("1")
        filename = os.path.join(OUTPUT_DIR, f"frame_{i:03d}.png")
        final_frame.save(filename)
        print(f"Saved: {filename}")

if __name__ == "__main__":
    create_frames()
