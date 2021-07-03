from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout)
import sys


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Video Player")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        self.playButton = QPushButton("Play")
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile("C:/Users/ASUS/Desktop/My Own Real Time Plotting Application/timer.mp4")))

        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(self.playButton)

        widget.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()


app = QApplication(sys.argv)
videoplayer = VideoPlayer()
videoplayer.resize(250, 250)
videoplayer.show()
sys.exit(app.exec_())
