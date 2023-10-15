FROM python:3.11.6-slim-bullseye
LABEL org.opencontainers.image.authors="hkuszynski@gmail.com"
WORKDIR /codetain_app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
#ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
CMD [ "/bin/bash", "./setup.sh" ]