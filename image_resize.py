import os
from PIL import Image

# === Settings ===
input_folder = "images"        
output_folder = "resized"     
new_size = (800, 600)         
output_format = "JPEG"         

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    # Process only image files
    try:
        with Image.open(file_path) as img:
            # Resize image
            resized_img = img.resize(new_size)

            # Create output file name
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

            # Save in chosen format
            resized_img.save(output_path, output_format)
            print(f"✅ Saved: {output_path}")
    except Exception as e:
        print(f"❌ Skipped {filename} (Error: {e})")

print("🎯 Batch image processing complete!")
