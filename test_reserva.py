from PyQt6.QtWidgets import QApplication
import sys
from ventana_reservas import VentanaReservas

app = QApplication(sys.argv)
v = VentanaReservas()
v.show()
sys.exit(app.exec())
