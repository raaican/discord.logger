FROM alpine:latest
WORKDIR /app

RUN mkdir -p cogs

COPY cogs/ cogs/
COPY config.py main.py requirements.txt ./

RUN apk add --no-cache python3 py3-pip 
RUN pip install --break-system-packages -r requirements.txt

CMD ["python3", "main.py"]
