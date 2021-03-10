###### Este es un script desarrollado para: **MercadoLibre Test**

# LOG de publicaciones
Este script permite tener un registro de todas las publicaciones activas que poseen uno o varios usuarios.
## Para su uso se necesita
- Tener instalado Python junto a su gestor de paquetes pip: [Conseguir acá](https://www.python.org/downloads/ "Conseguir acá")
- Tener instalado el modulo "requests": <br>
`pip install requests`
## Uso
Se debe ejecutar el script con el siguiente comando: <br>
`python app.py`<br>
A continuacion se le va a pedir que ingrese los IDs de los usuarios que se deseen LOGear, todos separados por espacio. <br>
Una vez ingresado el dato solicitado, se creara un archivo(LOG) en el mismo directorio del script, este archivo estará bajo el nombre "log". <br>
IMPORTANTE: El tiempo requerido para crear el archivo de registro dependerá de la cantidad de publicaciones que se necesiten almacenar.
## Ejemplo de LOG
El LOG almacenado tendra el siguiente formato: <br>
`Item ID: MLA837706147 `<br>
`Titulo: Notebook Dell Inspiron I5 32gb 256ssd 15,6  Win 10 Oferta `<br>
`Categoria: MLA1652 `<br>
`Nombre de la categoria: Notebooks `<br>
`----------------------------------------- `<br>
`Item ID: MLA881141900 `<br>
`Titulo: Notebook Laptop Dell Vostro I5 8gb 1tb + 240ssd 14 Win `<br>
`Categoria: MLA1652 `<br>
`Nombre de la categoria: Notebooks `<br>
`----------------------------------------- `<br>
