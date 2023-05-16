from PIL import Image

def create_sprite_sheet(image_path, output_path):
    # Load the input image
    image = Image.open(image_path)

    # Calculate the width and height of each frame
    frame_width = 50
    frame_height = 50

    # Create a new sprite sheet image
    sprite_sheet_width = 600
    sprite_sheet_height = 50
    sprite_sheet = Image.new('RGBA', (sprite_sheet_width, sprite_sheet_height))

    # Generate sprite sheet frames
    for i in range(9):
        # Calculate the x-coordinate of the current frame
        x = i * frame_width

        # Copy the frame to the sprite sheet
        frame = image.crop((x, 0, x + frame_width, frame_height))
        frame = frame.resize((int(sprite_sheet_width / 9), sprite_sheet_height))
        sprite_sheet.paste(frame, (i * int(sprite_sheet_width / 9), 0))

    # Flip the last 3 frames to face west
    for i in range(9, 12):
        frame = sprite_sheet.crop((i * int(sprite_sheet_width / 9), 0, (i + 1) * int(sprite_sheet_width / 9), sprite_sheet_height))
        flipped_frame = frame.transpose(Image.FLIP_LEFT_RIGHT)
        sprite_sheet.paste(flipped_frame, (i * int(sprite_sheet_width / 9), 0))

    # Save the sprite sheet
    sprite_sheet.save(output_path)

    print(f"Sprite sheet created successfully at '{output_path}'.")

# Usage example
input_image_path = '601.png'
output_sprite_sheet_path = 'output_sprite_sheet.png'
create_sprite_sheet(input_image_path, output_sprite_sheet_path)
