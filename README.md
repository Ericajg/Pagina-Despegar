
# ✈️ Sistema de Reservas - Proyecto Final

Este proyecto es una simulación básica del funcionamiento de un sistema de reservas de vuelos (similar a Despegar), desarrollado como trabajo final para la carrera **Analista de Sistemas**.

Permite realizar altas, consultas, modificaciones y eliminación de reservas utilizando una interfaz gráfica desarrollada en **PyQt6**, con almacenamiento en **SQLite**.

---

## 📌 Funcionalidades del sistema

✔ Registrar una reserva con:

- Origen ✈️  
- Destino 📍  
- Fecha de ida y vuelta 📅  
- Clase ✨  
- Cantidad de pasajeros 👥  
- Tipo de vuelo (Solo ida / Ida y vuelta)

✔ Visualizar todas las reservas registradas  
✔ Modificar una reserva seleccionándola en la tabla  
✔ Eliminar reservas  
✔ Actualización en tiempo real de la tabla  
✔ Uso de ventanas emergentes (QDialog) para mejor experiencia de usuario  

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|-----------|------|
| **Python 3** | Lenguaje principal |
| **PyQt6** | Interfaz gráfica |
| **SQLite** | Base de datos local |
| **Qt Designer** | Diseño visual de las interfaces (`.ui`) |

---

## 📂 Estructura del Proyecto

📁 despegar_final
│
├── main.py ← Archivo principal del programa
├── test_reserva.py ← Archivo de prueba de reservas
│
├── ventana_principal.py
├── ventana_reservas.py
├── ventana_calendario.py
├── ventana_pasajeros.py
│
├── ventana_principal.ui
├── ventana_reservas.ui
├── ventana_calendario.ui
├── ventana_pasajeros.ui
│
├── Despegar_BD.db ← Base de datos SQLite
│
└── iconos/ ← (opcional) recursos gráficos usados en la interfaz



---

## ⭐ Mejoras futuras

🔹 Validación de fechas  
🔹 Integración de precios y cálculo de totales  
🔹 Conexión con API de vuelos reales  
🔹 Exportación a PDF o Excel  

---

## 👤 Autora

**Erica Almirón**  
Proyecto Final —  

---



