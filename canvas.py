import sys
import csv
import random
from datetime import datetime
from itertools import count
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, QElapsedTimer
from PyQt5.QtWidgets import QApplication, QWidget,  QVBoxLayout, QPushButton
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aexki Application - Real time plotting')
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile("C:/Users/ASUS/Desktop/My Own Real Time Plotting Application/timer.mp4")))
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        self.playButton = QPushButton("Play")
        self.playButton.clicked.connect(self.record)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.canvas = FigureCanvas(plt.Figure(figsize=(10, 3)))
        layout.addWidget(self.canvas)
        layout.addWidget(self.videoWidget)
        layout.addWidget(self.playButton)

        self.ax = self.canvas.figure.subplots()
        self.ax.set_ylim([0, 100])
        self.ax.set_xlim([0, 1])
        self.bar = None

        self.x_vals = []
        self.y_vals = []
        self.index = count()
        self.writevalue = False

        self.interval = 0
        self.update_chart()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start()

        self.t = QElapsedTimer()

    def notify(self, receiver, event):
        self.t.start()
        ret = QApplication.notify(self, receiver, event)
        if(self.t.elapsed() > 10):
            print(f"processing event type {event.type()} for object {receiver.objectName()} "
                  f"took {self.t.elapsed()}ms")
        return ret

    def update_chart(self):
        curve = 500

        x = next(self.index)
        y = random.randint(300, 500)

        self.x_vals.append(x)
        self.y_vals.append(y)
        self.ax.cla()

        if x > curve:
            self.ax.plot(self.x_vals[-curve:],
                         self.y_vals[-curve:], color="black")
        else:
            self.ax.plot(self.x_vals, self.y_vals, color="black")

        self.canvas.draw()
        if self.writevalue:
            self.write(y)

    def initialise(self):
        fieldnames = ["x_value"]
        with open('data.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()

    def record(self):
        self.mediaPlayer.play()
        self.initialise()
        self.writevalue = True
        self.sleep5sec()
        self.timenow = datetime.now()

    def write(self, x_value):
        fieldnames = ["x_value"]

        with open('data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {"x_value": x_value}
            csv_writer.writerow(info)

    def sleep5sec(self):
        self.playButton.setEnabled(False)
        QtCore.QTimer.singleShot(
            5000, self.disable)

    def disable(self):
        self.playButton.setDisabled(False)
        self.playButton.setText('Retake')
        self.writevalue = False


def main():
    # import cProfile
    # import pstats

    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()

    # with cProfile.Profile() as pr:

    # stats = pstats.Stats(pr)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
