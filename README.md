# Hello World Animation for IronOS

A custom boot animation for IronOS-based devices featuring a typewriter effect. The animation displays a message with a cursor moving across the screen, creating an engaging typewriter-style boot sequence.

![Animation Preview](out/loop.gif)

## Download & Install

1. **Download the firmware**: Pre-built animations are available in the [bin](bin/) folder.

2. **Connect your device in DFU mode**: Follow your device manufacturer's instructions to enter DFU (Device Firmware Update) mode

3. **Move the `.hex` file**: Transfer the downloaded hex file to your device using your device's firmware update tool or method

## Variants

The animation is available in multiple speed presets:

| Name | Duration | Loop | Image |
|------|----------|------|-------|
| 1 Second | 1s | ❌ | ![1s](out/write_1s.gif) |
| 2 Seconds | 2s | ❌ | ![2s](out/write_2s.gif) |
| 3 Seconds | 3s | ❌ | ![3s](out/write_3s.gif) |
| 4 Seconds | 4s | ✅ | ![4s](out/write_4s.gif) |
| Looping | ∞ | ✅ | ![loop](out/loop.gif) |
| Fast | Rapid | ❌ | ![fast](out/fast.gif) |

## Build

To create your own custom animation frames, use the provided Python script:

```bash
cd src/
python generate_frames.py
```

### Workflow

The build process works as follows:

1. **Input Images**: The script uses two PNG images:
   - `message.png`: The base message/text to display
   - `cursor.png`: The cursor graphic that animates across the screen

2. **Frame Generation**: The Python script:
   - Positions the `cursor.png` at different x-coordinates for each frame
   - Merges the cursor over the message using the configured offsets
   - Saves each result as `frame_000.png`, `frame_001.png`, etc.
   
   **Note**: The cursor's x-position for each frame is hard-coded in the script (the `cursor_offsets` list). If you want to create a fork or another project based on this, modify those values to customize the cursor animation pattern.

3. **Animation Creation**: Convert the frames to an animated GIF using one of:

   **ImageMagick** (various durations):
   ```bash
   # 1 second animation
   magick -delay 7 frames_generated/frame_*.png -loop 1 write_1s.gif
   
   # 2 second animation
   magick -delay 13 frames_generated/frame_*.png -loop 1 write_2s.gif
   
   # 3 second animation
   magick -delay 20 frames_generated/frame_*.png -loop 1 write_3s.gif
   ```

   **FFmpeg** (with palette optimization for better quality):
   ```bash
   # Generate palette for better color quality
   ffmpeg -framerate 10 -i frames_generated/frame_%03d.png -vf "palettegen" palette.png
   
   # Create one-time playback GIF
   ffmpeg -loop -1 -i frames_generated/frame_%03d.png -i palette.png -filter_complex "paletteuse" typewriter_once.gif
   ```

4. **Firmware Compilation**: To compile the frames into an IronOS firmware hex file for your device, follow the instructions in the [IronOS-Meta Bootup Logos guide](https://github.com/Ralim/IronOS-Meta/tree/main/Bootup%20Logos)

## Contributing

Feel free to open issues or submit PRs. All contributions are welcome.

**If you find this animation useful, please consider giving it a star. ⭐**

## Credits

This project builds upon the awesome [IronOS](https://github.com/Ralim/IronOS) firmware project. Created and maintained by [Segilmez06](https://github.com/Segilmez06). Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA-4.0).
