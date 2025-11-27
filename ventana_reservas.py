from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt6 import uic
import sqlite3

DB = "Despegar_BD.db"

class VentanaReservas(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_reservas.ui", self)

        self.btnEliminar.clicked.connect(self.eliminar_reserva)
        self.btnModificar.clicked.connect(self.modificar_reserva)
        self.btnActualizar.clicked.connect(self.cargar_reservas)

        self.cargar_reservas()

    def cargar_reservas(self):
        """Carga los datos de la base en la tabla."""
        conexion = sqlite3.connect(DB)
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT ReservaID, AeropuertoOrigenID, AeropuertoDestinoID,
                   FechaIda, FechaVuelta, ClaseID, TipoVueloID, PasajeroID
            FROM Reserva
        """)

        datos = cursor.fetchall()
        conexion.close()

        self.tabla.setRowCount(len(datos))
        self.tabla.setColumnCount(8)
        self.tabla.setHorizontalHeaderLabels([
            "ID", "Origen", "Destino", "Fecha Ida", "Fecha Vuelta", "Clase", "Tipo Viaje", "Pasajeros"
        ])

        for fila, reserva in enumerate(datos):
            for col, valor in enumerate(reserva):
                self.tabla.setItem(fila, col, QTableWidgetItem(str(valor)))

    def eliminar_reserva(self):
        """Elimina la reserva seleccionada."""
        fila = self.tabla.currentRow()
        if fila < 0:
            QMessageBox.warning(self, "Error", "Seleccioná una reserva.")
            return

        id_reserva = self.tabla.item(fila, 0).text()

        conexion = sqlite3.connect(DB)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Reserva WHERE ReservaID = ?", (id_reserva,))
        conexion.commit()
        conexion.close()

        QMessageBox.information(self, "OK", "Reserva eliminada.")
        self.cargar_reservas()

    def modificar_reserva(self):
        """Actualiza la reserva seleccionada con los valores editados."""
        fila = self.tabla.currentRow()
        if fila < 0:
            QMessageBox.warning(self, "Error", "Seleccioná una reserva.")
            return

        valores = []
        for col in range(8):
            item = self.tabla.item(fila, col)
            valores.append(item.text() if item else "")

        conexion = sqlite3.connect(DB)
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE Reserva SET
                AeropuertoOrigenID=?, AeropuertoDestinoID=?, FechaIda=?, FechaVuelta=?, 
                ClaseID=?, TipoVueloID=?, PasajeroID=?
            WHERE ReservaID=?
        """, (valores[1], valores[2], valores[3], valores[4], valores[5], valores[6], valores[7], valores[0]))

        conexion.commit()
        conexion.close()

        QMessageBox.information(self, "OK", "Reserva modificada.")
        self.cargar_reservas()









