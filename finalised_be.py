import os
import sys
from os.path import join, splitext
from PIL import Image

import torch
from ultralytics import YOLO  # we’re using YOLOv11 for face detection

# Valid file types we're gonna allow
VALID_EXTENSIONS = ['.jpg', '.jpeg', '.png']

# Load up your YOLOv11 model — make sure the path is right!
model = YOLO(r"C:\Users\farra\Downloads\hfdyolov11\runs\weights\best.pt")

# Load your panda face overlay and make sure it supports transparency
overlay = Image.open("overlay.png").convert("RGBA")

# This function takes an image + detected face boxes and pastes the overlay on each face
def overlay_on_faces(image_pil, detections):
    image_pil = image_pil.convert("RGBA")  # Make sure we support transparency

    for det in detections:
        x1, y1, x2, y2 = map(int, det['box'])  # Get bounding box
        w, h = x2 - x1, y2 - y1  # Width and height of the face

        # Resize panda to match face size
        resized_overlay = overlay.resize((w, h))

        # Paste it right on the face with alpha (transparency) mask
        image_pil.paste(resized_overlay, (x1, y1), resized_overlay)

    return image_pil.convert("RGB")  # Convert back to standard RGB for saving

# YOLO does its magic here — detects faces and returns their boxes
def detect_faces(image_path):
    results = model(image_path, verbose=False)[0]
    detections = []

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, conf, cls_id = result
        label = results.names[int(cls_id)]
        if label.lower() == "humanface":  # Only go for faces, not other stuff
            detections.append({'label': label, 'box': (x1, y1, x2, y2)})

    return detections

# This one loops through the whole folder of images and handles each file
def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Make the output folder if it doesn’t exist

    for filename in os.listdir(input_folder):
        name, ext = splitext(filename)
        if ext.lower() not in VALID_EXTENSIONS:
            continue  # Skip files that aren’t images

        input_path = join(input_folder, filename)
        output_path = join(output_folder, filename)

        try:
            detections = detect_faces(input_path)
            if not detections:
                print(f"🙈 No faces found in {filename}")
                continue  # Move on if we didn’t find a face

            # Load the image, overlay panda(s), save the result
            image_pil = Image.open(input_path).convert("RGB")
            result_image = overlay_on_faces(image_pil, detections)
            result_image.save(output_path)
            print(f"✅ Saved: {output_path}")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

# Main function just handles the input/output folders from command line
def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py input_folder output_folder")
# we are using command line argumets here so make sure to enter the folder paths after the name of the file at command line while running this file

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    process_folder(input_folder, output_folder)

# Let’s get it rolling if this script is being run directly
if __name__ == "__main__":
    main()
