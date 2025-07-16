# vid.frnki

```
┌─────────────────────────────────────────────────────────────┐
│ A minimalist, frameless YouTube client for terminal dwellers │
│ Built with PyQt6 • Gruvbox aesthetic • Always-on-top        │
└─────────────────────────────────────────────────────────────┘
```

[![version](https://img.shields.io/badge/version-1.0.0-b8bb26?style=flat-square&labelColor=282828)](https://github.com/yourusername/vid.frnki/releases)
[![platform](https://img.shields.io/badge/platform-linux%20%7C%20windows-ebdbb2?style=flat-square&labelColor=282828)](https://github.com/yourusername/vid.frnki)
[![license](https://img.shields.io/badge/license-MIT-98971a?style=flat-square&labelColor=282828)](LICENSE)
[![language](https://img.shields.io/badge/python-3.12+-83a598?style=flat-square&labelColor=282828)](https://python.org)

## Features

- **Frameless Architecture**: Zero window chrome, maximum content
- **YouTube Integration**: Direct video search and embedded playback  
- **Always-on-Top**: Persistent overlay mode with toggle control
- **Gruvbox Colorscheme**: Dark terminal-inspired aesthetic (#282828/#b8bb26)
- **Drag Interface**: Click-and-drag window positioning
- **Keyboard Navigation**: ESC-driven back navigation
- **Translucent Rendering**: Semi-transparent background composition
- **Custom Window Controls**: Minimize/close/resize grip implementations

## Installation

### Binary Releases

**Download from:** [**v1.0.0 Release**](https://github.com/frnki42/vid.frnki/releases/tag/v1.0.0)

**Windows:**
- `vid.frnki.exe` - Portable version (run directly, no installation needed)
- `vid.frnki_installer.exe` - Installer version

**Linux:**
- `vid.frnki` - Executable binary (run directly, no installation needed)

**Requirements:** Internet connection, modern OS (Windows 10+ or Linux with Qt support)

### Source Build

```bash
# Clone repository
git clone https://github.com/frnki42/vid.frnki.git && cd vid.frnki

# Setup environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies  
pip install PyQt6 PyQt6-WebEngine youtube-search-python

# Execute
python vid.frnki.py
```

## Usage

```
Search → Results → Playback
   ↑        ↑         ↑
  Enter   Double    ESC
  query   click     back
```

**Controls:**
- `T` → Toggle always-on-top mode
- `−` → Minimize to taskbar  
- `X` → Terminate process
- `ESC` → Navigate backwards
- `Click+Drag` → Window positioning

## Build System

**Dependencies:**
- `python>=3.12`
- `PyQt6` + `PyQt6-WebEngine`  
- `youtube-search-python`
- `pyinstaller` (executable generation)

**Compile Binary:**
```bash
# Install build tools
pip install pyinstaller

# Generate executable
pyinstaller vid_frnki.spec

# Output: dist/vid_frnki[.exe]
```

## Architecture

```
vid.frnki.py
├── VidFrnki(QMainWindow)
│   ├── search_container    # Query input state
│   ├── results_container   # Search results list  
│   └── video_container     # Embedded player
└── PyQt6.QtWebEngineView   # YouTube iframe
```

**Stack:**
- **GUI**: PyQt6 + QtWebEngine
- **Theming**: Gruvbox (#282828/#b8bb26/#ebdbb2)  
- **Window**: Frameless + translucent + custom controls
- **State**: Container-based UI switching

## Contributing

Fork → Branch → Commit → PR

## License

MIT License - see [LICENSE](LICENSE)

## Dependencies

- [PyQt6](https://riverbankcomputing.com/software/pyqt/) - GUI framework
- [youtube-search-python](https://github.com/alexmercerind/youtube-search-python) - YouTube API
- [Gruvbox](https://github.com/morhetz/gruvbox) - Color scheme inspiration

---

**Runtime requirement:** Active internet connection