# base image
FROM python:3.8

# exposing default port for streamlit
EXPOSE 8501

# making directory of app
WORKDIR /app

# copy over requirements
COPY requirements.txt ./requirements.txt

# install pip then packages
RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt

# copying all files over
COPY . .

# cmd to launch app when container is run
CMD streamlit run --server.port $PORT DASHBOARD_WHITE_PAPER.py
