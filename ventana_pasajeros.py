
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class VentanaPasajeros(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_pasajeros.ui", self)

        # Conectar botones y cambios
        self.btnAplicar.clicked.connect(self.aplicar)
        self.spinMayores.valueChanged.connect(self.actualizar_mayores)
        self.spinMenores.valueChanged.connect(self.actualizar_menores)

        # Inicializar combobox edades
        edades = ["Seleccionar..."] + [str(i) for i in range(1, 18)]
        self.comboEdadMenor1.addItems(edades)
        self.comboEdadMenor2.addItems(edades)

        self.actualizar_menores()  # Para ocultar o mostrar combos de edad

    def actualizar_mayores(self):
        self.myr.setText(str(self.spinMayores.value()))
        self.lblmyredad.setText("Mayor de 18")

    def actualizar_menores(self):
        cant = self.spinMenores.value()
        self.mnr.setText(str(cant))
        self.lblEdadMenor1.setVisible(cant >= 1)
        self.comboEdadMenor1.setVisible(cant >= 1)
        self.lblEdadMenor2.setVisible(cant >= 2)
        self.comboEdadMenor2.setVisible(cant >= 2)
        self.lblmyredad.setText("Hasta 17 años")

    def aplicar(self):
        mayores = self.spinMayores.value()
        menores = self.spinMenores.value()
        total = mayores + menores
        clase = self.comboClase.currentText()

        resumen = f"{total} pasajeros, clase {clase}"
        self.resumen = resumen
        self.accept()  # Cierra la ventana y devuelve Accepted

    def get_resumen(self):
        return getattr(self, 'resumen', '')

