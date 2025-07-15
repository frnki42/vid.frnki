import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget, QLabel, QHBoxLayout, QSizeGrip
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt, QPoint, QRectF, QEvent
from PyQt6.QtGui import QPainterPath, QRegion, QCursor, QFont
from urllib.parse import urlparse, parse_qs
from youtubesearchpython import VideosSearch

class VidFrnki(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("vid.frnki")
        self.setGeometry(100, 100, 640, 480)  # Initial size
        
        # Set always on top and frameless from the start
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        
        # Enable translucent background
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # For dragging the frameless window
        self.old_pos = None
        
        # Toggle state for always on top
        self.on_top = True
        
        # Set hacker-style font (monospace)
        font = QFont("Monospace", 10)
        self.setFont(font)
        
        # Central widget and layout
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: rgba(40, 40, 40, 204); border-radius: 10px;")  # Uniform semi-transparent background
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(8, 8, 8, 5)  # Increased margins for space around edges, reduced bottom
        
        # Search container
        self.search_container = QWidget()
        self.search_container.setStyleSheet("background-color: transparent;")
        self.search_layout = QVBoxLayout(self.search_container)
        self.search_layout.setContentsMargins(0, 0, 0, 0)
        self.search_layout.setSpacing(5)
        
        self.search_layout.addStretch()  # Add stretch for vertical centering
        
        # Search input
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter YouTube search query")
        self.search_input.returnPressed.connect(self.search_videos)
        self.search_input.setMaximumHeight(25)
        self.search_input.setFixedWidth(360)  # 75% of previous 480
        self.search_layout.addWidget(self.search_input, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        # Load button (smaller width)
        self.load_button = QPushButton("Search")
        self.load_button.clicked.connect(self.search_videos)
        self.load_button.setMaximumHeight(25)
        self.load_button.setMaximumWidth(100)
        self.search_layout.addWidget(self.load_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.search_layout.addStretch()  # Existing bottom stretch
        
        # Controls for search (no back button needed)
        self.search_controls = QHBoxLayout()
        self.search_controls.setContentsMargins(0, 0, 0, 0)
        self.search_controls.setSpacing(10)
        
        # Subtle "vid.frnki" label
        self.search_bg_label = QLabel("vid.frnki - v1.0.0")
        self.search_bg_label.setStyleSheet("color: rgba(184, 187, 38, 50); font-size: 10px;")
        self.search_controls.addWidget(self.search_bg_label)
        
        self.search_controls.addStretch()
        
        # Toggle on top button (more minimal: "T")
        self.search_toggle = QPushButton("T")
        self.search_toggle.setFixedSize(15, 15)
        self.search_toggle.setCheckable(True)
        self.search_toggle.setChecked(True)
        self.search_toggle.clicked.connect(self.toggle_on_top)
        self.search_controls.addWidget(self.search_toggle)
        
        # Minimize button
        self.search_minimize = QPushButton("−")
        self.search_minimize.setFixedSize(15, 15)
        self.search_minimize.clicked.connect(self.showMinimized)
        self.search_controls.addWidget(self.search_minimize)
        
        # Close button
        self.search_close = QPushButton("X")
        self.search_close.setFixedSize(15, 15)
        self.search_close.clicked.connect(self.close)
        self.search_controls.addWidget(self.search_close)
        
        # Resize grip
        self.search_grip = QSizeGrip(self)
        self.search_grip.setFixedSize(15, 15)
        self.search_controls.addWidget(self.search_grip)
        
        self.search_layout.addLayout(self.search_controls)
        
        self.main_layout.addWidget(self.search_container)
        
        # Results container
        self.results_container = QWidget()
        self.results_container.setStyleSheet("background-color: transparent;")
        self.results_layout = QVBoxLayout(self.results_container)
        self.results_layout.setContentsMargins(0, 0, 0, 0)
        self.results_layout.setSpacing(5)
        
        # Results list
        self.results_list = QListWidget()
        self.results_list.setWordWrap(True)
        self.results_layout.addWidget(self.results_list)
        self.results_layout.setStretchFactor(self.results_list, 1)
        self.results_list.itemDoubleClicked.connect(self.play_selected)
        
        # Controls for results
        self.results_controls = QHBoxLayout()
        self.results_controls.setContentsMargins(0, 0, 0, 0)
        self.results_controls.setSpacing(10)
        
        # Back button
        self.results_back = QPushButton("←")
        self.results_back.setFixedSize(15, 15)
        self.results_back.clicked.connect(self.go_to_search)
        self.results_controls.addWidget(self.results_back)
        
        # Subtle "vid.frnki" label
        self.results_bg_label = QLabel("vid.frnki")
        self.results_bg_label.setStyleSheet("color: rgba(184, 187, 38, 50); font-size: 10px;")
        self.results_controls.addWidget(self.results_bg_label)
        
        self.results_controls.addStretch()
        
        # Toggle on top button (more minimal: "T")
        self.results_toggle = QPushButton("T")
        self.results_toggle.setFixedSize(15, 15)
        self.results_toggle.setCheckable(True)
        self.results_toggle.setChecked(True)
        self.results_toggle.clicked.connect(self.toggle_on_top)
        self.results_controls.addWidget(self.results_toggle)
        
        # Minimize button
        self.results_minimize = QPushButton("−")
        self.results_minimize.setFixedSize(15, 15)
        self.results_minimize.clicked.connect(self.showMinimized)
        self.results_controls.addWidget(self.results_minimize)
        
        # Close button
        self.results_close = QPushButton("X")
        self.results_close.setFixedSize(15, 15)
        self.results_close.clicked.connect(self.close)
        self.results_controls.addWidget(self.results_close)
        
        # Resize grip
        self.results_grip = QSizeGrip(self)
        self.results_grip.setFixedSize(15, 15)
        self.results_controls.addWidget(self.results_grip)
        
        self.results_layout.addLayout(self.results_controls)
        
        self.main_layout.addWidget(self.results_container)
        self.results_container.hide()
        
        # Video container
        self.video_container = QWidget()
        self.video_container.setStyleSheet("background-color: transparent;")
        self.video_layout = QVBoxLayout(self.video_container)
        self.video_layout.setContentsMargins(1, 1, 1, 0)  # Even smaller frame on top/left/right
        
        self.web_view = QWebEngineView()
        self.web_view.setStyleSheet("background-color: #000000;")  # Opaque black background for video
        self.video_layout.addWidget(self.web_view)
        self.video_layout.setStretchFactor(self.web_view, 1)
        
        # Controls bar at bottom for video
        self.video_controls = QHBoxLayout()
        self.video_controls.setContentsMargins(0, 0, 0, 0)
        self.video_controls.setSpacing(10)
        
        # Back button
        self.back_button = QPushButton("←")
        self.back_button.setFixedSize(15, 15)
        self.back_button.clicked.connect(self.go_back)
        self.video_controls.addWidget(self.back_button)
        
        # Subtle "vid.frnki" label
        self.video_bg_label = QLabel("vid.frnki")
        self.video_bg_label.setStyleSheet("color: rgba(184, 187, 38, 50); font-size: 10px;")
        self.video_controls.addWidget(self.video_bg_label)
        
        self.video_controls.addStretch()
        
        # Toggle on top button (more minimal: "T")
        self.video_toggle = QPushButton("T")
        self.video_toggle.setFixedSize(15, 15)
        self.video_toggle.setCheckable(True)
        self.video_toggle.setChecked(True)
        self.video_toggle.clicked.connect(self.toggle_on_top)
        self.video_controls.addWidget(self.video_toggle)
        
        # Minimize button
        self.video_minimize = QPushButton("−")
        self.video_minimize.setFixedSize(15, 15)
        self.video_minimize.clicked.connect(self.showMinimized)
        self.video_controls.addWidget(self.video_minimize)
        
        # Close button
        self.video_close = QPushButton("X")
        self.video_close.setFixedSize(15, 15)
        self.video_close.clicked.connect(self.close)
        self.video_controls.addWidget(self.video_close)
        
        # Resize grip
        self.video_grip = QSizeGrip(self)
        self.video_grip.setFixedSize(15, 15)
        self.video_controls.addWidget(self.video_grip)
        
        self.video_layout.addLayout(self.video_controls)
        
        self.main_layout.addWidget(self.video_container)
        self.video_container.hide()
        
        # Store video results
        self.video_results = []
        
        # Apply Gruvbox dark theme: #282828 bg, subtle green #b8bb26 highlights
        self.setStyleSheet("""
            QMainWindow {
                background-color: transparent;
            }
            QWidget {
                background-color: transparent;
                color: #ebdbb2;
            }
            QLineEdit {
                background-color: #1d2021;
                border: 1px solid #b8bb26;
                color: #ebdbb2;
                padding: 2px;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border: 1px solid #98971a;
            }
            QPushButton {
                background-color: #1d2021;
                border: 1px solid #b8bb26;
                color: #ebdbb2;
                padding: 2px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #32302f;
            }
            QPushButton:checked {
                background-color: #b8bb26;
                color: #282828;
            }
            QListWidget {
                background-color: #1d2021;
                border: 1px solid #b8bb26;
                color: #ebdbb2;
                border-radius: 5px;
                margin-top: 5px;  # Added top margin to prevent overlap
            }
            QListWidget::item:selected {
                background-color: #32302f;
            }
            QLabel {
                background: transparent;
                color: #b8bb26;
            }
            QSizeGrip {
                background: transparent;
                width: 15px;
                height: 15px;
            }
        """)
        
        # Set initial mask for curved edges
        self.updateMask()
        
    def search_videos(self):
        query = self.search_input.text().strip()
        if not query:
            return
        
        results = VideosSearch(query, limit=20).result()['result']
        self.video_results = results
        self.results_list.clear()
        for res in results:
            self.results_list.addItem(f"{res['title']} - {res['channel']['name']}")
        
        self.search_container.hide()
        self.results_container.show()
        self.updateMask()
    
    def play_selected(self, item):
        index = self.results_list.row(item)
        video_id = self.video_results[index]['id']
        embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&rel=0&showinfo=0&controls=1"
        self.web_view.setUrl(QUrl(embed_url))
        
        self.results_container.hide()
        self.video_container.show()
        # No opacity change
        self.updateMask()
    
    def go_back(self):
        self.video_container.hide()
        self.web_view.setUrl(QUrl("about:blank"))
        self.results_container.show()
        self.updateMask()
    
    def go_to_search(self):
        self.results_container.hide()
        self.search_container.show()
        self.updateMask()
    
    def toggle_on_top(self):
        self.on_top = not self.on_top
        flags = self.windowFlags()
        if self.on_top:
            flags |= Qt.WindowType.WindowStaysOnTopHint
        else:
            flags &= ~Qt.WindowType.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.show()
        
        # Sync all toggle buttons
        self.search_toggle.setChecked(self.on_top)
        self.results_toggle.setChecked(self.on_top)
        self.video_toggle.setChecked(self.on_top)
    
    def start_drag(self, event, handle):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
            handle.setCursor(QCursor(Qt.CursorShape.ClosedHandCursor))
    
    def do_drag(self, event):
        if self.old_pos is not None:
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()
    
    def end_drag(self, event, handle):
        self.old_pos = None
        handle.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
    
    def updateMask(self):
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), 10, 10)  # 10px radius
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateMask()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            if self.video_container.isVisible():
                self.go_back()
            elif self.results_container.isVisible():
                self.go_to_search()
            self.updateMask()
            event.accept()
        else:
            super().keyPressEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VidFrnki()
    window.show()
    sys.exit(app.exec())