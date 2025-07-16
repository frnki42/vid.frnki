# vid.frnki

A minimalist, always-on-top YouTube search and player application built with PyQt6. Features a sleek frameless design with Gruvbox dark theme.

![vid.frnki](https://img.shields.io/badge/version-1.0.0-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

## Features

- 🎥 **YouTube Search & Play**: Search and play YouTube videos in an embedded player
- 🖼️ **Frameless Design**: Clean, borderless window with custom controls
- 📌 **Always On Top**: Toggle-able always-on-top functionality
- 🎨 **Gruvbox Theme**: Dark, hacker-style aesthetic with green accents
- 🖱️ **Draggable Interface**: Click and drag anywhere to move the window
- ⌨️ **Keyboard Navigation**: ESC key for intuitive back navigation
- 🔄 **Translucent Background**: Semi-transparent design for desktop integration
- 📱 **Resizable**: Custom resize grips for window management

## Download

### Pre-built Binaries

Download the latest release for your platform:

- **Windows**: `vid.frnki.exe` or `vid.frnki_installer.exe`
- **Linux**: `vid.frnki` (AppImage or binary)

[**Download Latest Release →**](https://github.com/yourusername/vid.frnki/releases/latest)

## Installation

### Option 1: Pre-built Executables (Recommended)
1. Download the appropriate executable for your platform
2. Run the application directly (no installation required)

### Option 2: From Source
```bash
# Clone the repository
git clone https://github.com/yourusername/vid.frnki.git
cd vid.frnki

# Create virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install dependencies
pip install PyQt6 PyQt6-WebEngine youtube-search-python

# Run the application
python vid.frnki.py
```

## Usage

1. **Search**: Enter a YouTube search query and press Enter or click "Search"
2. **Browse Results**: Double-click any video in the results list to play
3. **Navigation**: Use ESC key or back buttons to navigate between screens
4. **Window Controls**: 
   - `T` - Toggle always-on-top
   - `−` - Minimize window
   - `X` - Close application
5. **Move Window**: Click and drag anywhere on the window to reposition

## Building from Source

### Requirements
- Python 3.12+
- PyQt6
- PyQt6-WebEngine
- youtube-search-python
- PyInstaller (for building executables)

### Build Executable
```bash
# Activate virtual environment
source myenv/bin/activate

# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller vid_frnki.spec
```

The executable will be created in the `dist/` directory.

## Technical Details

- **Framework**: PyQt6 with WebEngine for video playback
- **Architecture**: Single-file application with container-based UI states
- **Theme**: Gruvbox color scheme (#282828, #b8bb26, #ebdbb2)
- **Window Management**: Frameless with custom controls and rounded corners

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [PyQt6](https://www.riverbankcomputing.com/software/pyqt/)
- YouTube integration via [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)
- Inspired by the [Gruvbox](https://github.com/morhetz/gruvbox) color scheme

---

**Note**: This application requires an internet connection for YouTube search and video playback.