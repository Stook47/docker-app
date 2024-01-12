FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/

#(This line is causing my project to not build due to an invalid ELF header.)
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "data_generator.py"]