from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

janela = QWidget()
janela.setWindowTitle("Controle de Estoque")
label = QLabel("Sistema Iniciado!", parent=janela)
janela.showMaximized()

app.exec()
