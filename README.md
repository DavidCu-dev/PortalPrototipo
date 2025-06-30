# PortalPrototipo 📄

**PortalPrototipo** es una aplicación web desarrollada con Django, enfocada en el manejo de informacion y generacion de documentos Word y Excel a partir de formularios personalizables. Este sistema fue construido con fines educativos y técnicos para demostrar mis habilidades, manejo de datos y generación dinámica de documentos.

> ⚠️ Este proyecto es de uso exclusivamente académico y demostrativo. No representa a ninguna institución pública o privada, ni debe usarse en entornos de producción o con datos reales.

---

## 🚀 Características principales

- 📝 Captura de datos mediante formularios personalizados siguiendo la base de Django.
- 📄 Generación automática de documentos Word con formato administrativo.
- 📊 Exportación de tablas a Excel desde datos de base de datos.
- 🔒 Almacenamiento de datos en base de datos relacional con Django ORM.
- 🎨 Interfaz básica con campos editables y estilos personalizables.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- **Django 4+**
- **openpyxl** para Excel
- **python-docx** para Word
- **SQLite** (modo local) o PostgreSQL (opcional)
- HTML5, CSS3

---

## 📂 Estructura general del proyecto

PortalPrototipo/

├── app/ # Aplicación principal (formularios, modelos, vistas)

├── media/ # Archivos generados (Word, Excel)

├── static/ # Archivos estáticos (CSS, JS, imágenes)

├── templates/ # Plantillas HTML

├── db.sqlite3 # Base de datos por defecto

├── manage.py

├── requirements.txt

└── README.md

---

## ⚙️ Instalación local

1. Clona el repositorio:
git clone https://github.com/DavidCu-dev/PortalPrototipo.git
cd PortalPrototipo

2. Crea un entorno virtual 
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Window

3. Instala dependencias 
pip install -r requirements.txt

4. Aplica migraciones y ejecuta el servidor:
python manage.py migrate
python manage.py runserver

---

## 💡 Origen del proyecto

Este proyecto fue inspirado en una solución que desarrollé durante mi servicio social profesional, cuyo objetivo era automatizar la generación de documentos administrativos mediante formularios web. Esa solución original fue entregada a una organización privada y forma ahora parte de un producto cerrado.

Este repositorio, PortalPrototipo, fue construido de forma independiente con el propósito de:

Replicar la lógica general del proceso de automatización documental.

Mostrar mis habilidades técnicas en desarrollo con Django.

Servir como ejemplo profesional y académico en mi portafolio.

No reutiliza ni copia código, documentos, interfaces ni estructuras de datos del sistema original privado. Su similitud conceptual es común en aplicaciones administrativas modernas.

---

## 🧪 Datos ficticios y uso responsable

Esta aplicación fue diseñada para pruebas y demostración. Se espera que los usuarios no ingresen datos reales y utilicen información ficticia en todos los formularios.

Ejemplos válidos:

Nombre empresa: Empresa Ficticia S.A. de C.V.

RFC: FAK123456XYZ

Correo: prueba@ejemplo.com

Dirección: Calle Falsa #123, Ciudad, Estado

El sistema no recolecta, transmite ni analiza datos reales. Todo el contenido se procesa localmente en la base de datos y no se utiliza con fines comerciales, institucionales ni de análisis.

---

## Aviso legal

Este proyecto no está afiliado, aprobado ni respaldado por la organización original del servicio social.

Es un desarrollo independiente creado con fines formativos y demostrativos.

No contiene marcas registradas, logotipos ni símbolos oficiales de ninguna institución.

Cualquier parecido en los nombres o formatos de documentos es puramente estructural y común en sistemas administrativos.

El autor no se hace responsable del uso indebido de este sistema o del ingreso de datos sensibles por parte de terceros.


---

## 🙋‍♂️ Autor

David Hernandez Cuevas 

GitHub: @DavidCu-dev

¿Dudas o sugerencias? Abre un issue en el repositorio o envía un pull request. Estoy abierto a colaborar en proyectos similares.

