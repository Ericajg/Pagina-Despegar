from PyQt6.QtWidgets import QDialog, QCalendarWidget, QPushButton, QVBoxLayout

class VentanaCalendario(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleccionar Fecha")

        self.calendario = QCalendarWidget()
        self.btnAceptar = QPushButton("Aceptar")

        layout = QVBoxLayout()
        layout.addWidget(self.calendario)
        layout.addWidget(self.btnAceptar)
        self.setLayout(layout)

        self.btnAceptar.clicked.connect(self.aceptar)

        self.fechaSeleccionada = None

    def aceptar(self):
        self.fechaSeleccionada = self.calendario.selectedDate().toString("dd/MM/yyyy")
        self.accept()

    def get_fecha(self):
        return self.fechaSeleccionada
