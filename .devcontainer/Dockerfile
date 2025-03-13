FROM ubuntu:latest

# Instalar dependencias
RUN apt-get update && apt-get install -y     python3     python3-pip     python3-venv     git     && apt-get clean     && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Configurar entorno virtual y dependencias
RUN python3 -m venv venv
RUN ./venv/bin/pip install --upgrade pip

# Mantener contenedor activo
CMD ["tail", "-f", "/dev/null"]