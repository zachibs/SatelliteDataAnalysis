FROM selenium/standalone-chrome

# running commands to install dependencis
RUN sudo apt update
RUN sudo apt install python3-pip -y

COPY requirements.txt .
RUN pip install -r requirements.txt

# creating a working directory and cd in to it
WORKDIR /service

# adding files to it
COPY decodeHexdump.py /service
COPY generateFinalData.py /service
COPY generateUrlDf.py /service
COPY pushToInfluxDB.py /service
COPY start_service.py /service

RUN mkdir generatedCSVs

# default command to run when the container is executed
CMD ["python3", "./start_service.py"]
