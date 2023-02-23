FROM python:3.8

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev \
    curl

RUN pip install flask
RUN pip install requests
RUN pip install numpy
RUN pip install matplotlib
RUN pip install nbformat
RUN pip install pandas
RUN pip install datetime
RUN pip install nbconvert
RUN pip install textwrap3
RUN pip install boto3
RUN pip install botocore


# Copy your Jupyter Notebook file to the Docker image
COPY my_notebook.py /app/
COPY process_notebook.py /app/
WORKDIR /app

# Run a Python script to execute the notebook file and append a string to the output
CMD ["python", "process_notebook.py"]