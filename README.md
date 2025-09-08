**Ejecutar en docker**
```bash
# Construir imagen
docker build -t utea-datos-ida-vuelta .

# indicando volumenes
docker run -e TZ=America/La_Paz --env-file .env -d --name utea-datos-ida-vuelta -v "G:\\Ingenio Azucarero Guabira S.A\\COOR_GERENCIA_CANA - Parte_Horarios:/app/datos" utea-datos-ida-vuelta