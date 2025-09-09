FROM python:3.9-slim

WORKDIR /Football

RUN apt-get update && apt-get install -y

#RUN git clone https://github.com/maigacribzz/Football.git .
COPY . /Football/
RUN pip3 install -r requirements.txt

EXPOSE 8501

#HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Footballs_Top3.py", "--server.port=8501", "--server.address=0.0.0.0"]