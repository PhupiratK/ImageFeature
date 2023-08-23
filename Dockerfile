FROM python:3.11.4

# 
WORKDIR /imagefeature

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# 
COPY ./requirements.txt /imagefeature/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /imagefeature/requirements.txt

# 
COPY ./app /imagefeature/app


ENV PYTHONPATH "${PYTHONPATH}:/imagefeature"

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]