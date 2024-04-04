Posterior a su clonación es necesario correr los siguientes comandos para inicializar el proyecto

Estando en la carpeta contenedora, creamos el entorno virtual:
```
python -m venv venv
```

Lo activamos:
```
cd venv/Scripts
activate
```

Y una vez en la raiz, instalamos las dependencias:
```
cd ..
cd ..
pip install -r requirements.txt
```

Una vez instalado, corremos el servidor:
```
flask --app main run
```


