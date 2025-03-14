# 📂 docs/README.md - Documentación del Proyecto
"""
# 📊 Análisis Estadístico en Power BI con Conexión a SQL Server y MongoDB

## 📌 Descripción del Proyecto

Este proyecto implementa un **dashboard avanzado en Power BI** con conexión a **SQL Server y MongoDB**, incorporando modelos estadísticos en **DAX** para análisis de datos complejos. Incluye:

- **Conexión a bases de datos relacionales y NoSQL (SQL Server y MongoDB).**
- **Implementación de modelos analíticos con DAX en Power BI.**
- **Análisis de tendencias, métricas y KPIs en tiempo real.**
- **Visualización interactiva y optimización de performance en los dashboards.**

## 📂 Estructura del Proyecto
```
📁 PowerBI_Advanced_Analytics
│── 📂 src/
│   │── connect_sql.py  # Conexión a SQL Server
│   │── connect_mongo.py  # Conexión a MongoDB
│   │── dax_models.pbix  # Archivo de Power BI con modelos estadísticos
│── 📂 tests/
│   │── test_connect_sql.py  # Pruebas de conexión a SQL Server
│   │── test_connect_mongo.py  # Pruebas de conexión a MongoDB
│── 📂 docs/
│   │── README.md  # Documentación del proyecto
```

## 🚀 Instalación y Configuración

1. **Clona este repositorio:**
   ```sh
   git clone https://github.com/emmacm20-lab/PowerBI_Advanced_Analytics.git
   ```
2. **Configura la conexión a SQL Server y MongoDB:**
   ```sh
   python src/connect_sql.py
   python src/connect_mongo.py
   ```
3. **Abre y explora el dashboard en Power BI:**
   ```sh
   dax_models.pbix
   ```

## 📩 Flujo de Trabajo
1. **Extracción de datos desde SQL Server y MongoDB.**
2. **Procesamiento de datos y modelado estadístico en DAX.**
3. **Visualización avanzada de métricas y KPIs en Power BI.**
4. **Optimización del performance en reportes.**

## 🛠 Tecnologías Utilizadas
- **Power BI & DAX**: Modelado y análisis estadístico avanzado.
- **SQL Server & T-SQL**: Extracción de datos estructurados.
- **MongoDB**: Manejo de datos NoSQL.
- **Python (PyMongo, pyodbc)**: Conexión y procesamiento de datos.

## 📈 Resultados Esperados
- 📌 **Automatización del análisis de datos en Power BI.**
- 📌 **Modelado y visualización de KPIs con DAX y datos dinámicos.**
- 📌 **Integración de datos estructurados y NoSQL en un solo dashboard.**
- 📌 **Mayor eficiencia en la toma de decisiones empresariales.**

## 🧪 Pruebas
El proyecto incluye pruebas en Python para validar la conexión a las bases de datos.
1. **Ejecución de pruebas:**
   ```sh
   python -m unittest discover tests/
   ```

## 📬 Contacto
Para consultas o sugerencias, contáctame en [emmanuel.cmora20@gmail.com](mailto:emmanuel.cmora20@gmail.com).
"""

# 📂 src/connect_sql.py - Conexión a SQL Server
```python
import pyodbc

def connect_sql():
    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=tu_servidor;DATABASE=tu_db;UID=usuario;PWD=contraseña")
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 * FROM Ventas")
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == "__main__":
    print("Conexión a SQL Server exitosa:", connect_sql())
```

# 📂 src/connect_mongo.py - Conexión a MongoDB
```python
from pymongo import MongoClient

def connect_mongo():
    client = MongoClient("mongodb://usuario:contraseña@tu_servidor:27017/")
    db = client["tu_base"]
    collection = db["ventas"]
    data = collection.find().limit(10)
    return list(data)

if __name__ == "__main__":
    print("Conexión a MongoDB exitosa:", connect_mongo())
```

# 📂 tests/test_connect_sql.py - Pruebas de conexión a SQL Server
```python
import unittest
from src.connect_sql import connect_sql

class TestSQLConnection(unittest.TestCase):
    def test_connection(self):
        data = connect_sql()
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()
```

# 📂 tests/test_connect_mongo.py - Pruebas de conexión a MongoDB
```python
import unittest
from src.connect_mongo import connect_mongo

class TestMongoConnection(unittest.TestCase):
    def test_connection(self):
        data = connect_mongo()
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()
```