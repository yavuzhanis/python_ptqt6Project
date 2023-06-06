import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolTip


def window():
    # bu kod uygulamamızı çalıştırmamıza yarıyor.
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("İlk Projemiz")
    win.setGeometry(200, 200, 500, 500)

    lblName = QtWidgets.QLabel(win)
    lblName.move(50, 30)
    lblName.setText("İsim: ")

    lblSurname = QtWidgets.QLabel(win)
    lblSurname.move(50, 70)
    lblSurname.setText("Soysim: ")

    txtName = QtWidgets.QLineEdit(win)
    txtName.move(120, 30)

    txtSurname = QtWidgets.QLineEdit(win)
    txtSurname.move(120, 70)

    def yazdir():
        lblSonuc.setText(txtName.text() + " " + txtSurname.text())

    btnYaz = QtWidgets.QPushButton(win)
    btnYaz.move(120, 110)
    btnYaz.setText("Kaydet")
    btnYaz.clicked.connect(yazdir)

    lblSonuc = QtWidgets.QLabel(win)
    lblSonuc .move(120, 140)
    win.show()
    sys.exit(app.exec())


window()
