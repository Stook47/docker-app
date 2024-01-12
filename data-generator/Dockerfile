FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/
#RUN pip install --no-cache-dir -r requirements.txt     #(This line is causing my project to not build due to an invalid ELF header.)

COPY . /app

CMD ["python", "data_generator.py"]