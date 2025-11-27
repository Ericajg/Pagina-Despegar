from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QMessageBox
import sqlite3, sys
from ventana_calendario import VentanaCalendario
from ventana_pasajeros import VentanaPasajeros
from ventana_reservas import VentanaReservas


DB = "Despegar_BD.db"

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_principal.ui", self)

        self.cmbDesde = self.findChild(QComboBox, "cmbDesde")
        self.cmbHacia = self.findChild(QComboBox, "cmbHacia")

        self.lblcalendario.mousePressEvent = lambda _: self.seleccionar_fecha(self.lblcalendario)
        self.lblcalendario2.mousePressEvent = lambda _: self.seleccionar_fecha(self.lblcalendario2)

        self.cmbPasajeros.mousePressEvent = lambda _: self.abrir_pasajeros()

        self.tipo_viaje = None
        self.btnSoloIda.clicked.connect(lambda: self.set_tipo_viaje("Solo Ida"))
        self.btnIdaVuelta.clicked.connect(lambda: self.set_tipo_viaje("Ida y Vuelta"))

        self.btnBuscar.clicked.connect(self.guardar_reserva)
        self.btnVerReservas.clicked.connect(self.abrir_reservas)

        self.cargar_aeropuertos()

    def set_tipo_viaje(self, tipo):
        self.tipo_viaje = tipo

    def db_query(self, query, params=(), fetch=True):
        con = sqlite3.connect(DB)
        cur = con.cursor()
        cur.execute(query, params)
        con.commit()
        data = cur.fetchall() if fetch else None
        con.close()
        return data

    def cargar_aeropuertos(self):
        datos = self.db_query("""
            SELECT AeropuertoID, p.Nombre, c.Nombre, a.Nombre
            FROM Pais p
            JOIN Ciudad c ON c.PaisID = p.PaisID
            JOIN Aeropuerto a ON a.CiudadID = c.CiudadID
        """)

        self.cmbDesde.clear()
        self.cmbHacia.clear()
        self.aeropuertos = {}

        for id, pais, ciudad, aeropuerto in datos:
            texto = f"{pais} - {ciudad} - {aeropuerto}"
            self.cmbDesde.addItem(texto)
            self.cmbHacia.addItem(texto)
            self.aeropuertos[texto] = id

    def seleccionar_fecha(self, label):
        ventana = VentanaCalendario()
        if ventana.exec() == 1:
            label.setText(ventana.get_fecha())

    def abrir_pasajeros(self):
        ventana = VentanaPasajeros()
        if ventana.exec() == 1:
            self.cmbPasajeros.setText(ventana.get_resumen())

    def guardar_reserva(self):
        if not self.tipo_viaje:
            return QMessageBox.warning(self, "Error", "Seleccioná un tipo de viaje.")

        valores = (
            self.aeropuertos.get(self.cmbDesde.currentText()),
            self.aeropuertos.get(self.cmbHacia.currentText()),
            self.lblcalendario.text(),
            self.lblcalendario2.text(),
            "Economy",
            self.cmbPasajeros.text(),
            self.tipo_viaje
        )

        self.db_query("""
            INSERT INTO Reserva (Origen, Destino, FechaIda, FechaVuelta, Clase, Pasajeros, TipoViaje)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, valores, fetch=False)

        QMessageBox.information(self, "Guardado", "Reserva registrada correctamente.")

    def abrir_reservas(self):
        VentanaReservas().exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())





