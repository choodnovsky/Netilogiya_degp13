FROM continuumio/miniconda3:latest
COPY . ./app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN chmod +x /app/1.sh
RUN conda config --append channels conda-forge
RUN conda install --file requirements.txt
RUN bash /app/1.sh