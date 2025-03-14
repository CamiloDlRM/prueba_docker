FROM ubuntu:latest

# Instalar dependencias
RUN apt-get update && apt-get install -y     python3     python3-pip     python3-venv     git    postgresql   postgresql-contrib    && apt-get clean     && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

COPY requirements.txt .

# Configurar entorno virtual y dependencias
RUN python3 -m venv venv
RUN ./venv/bin/pip install --upgrade pip
RUN ./venv/bin/pip install -r requirements.txt


WORKDIR /prueba
RUN touch texto.txt


# Mantener contenedor activo
CMD ["tail", "-f", "/dev/null"]