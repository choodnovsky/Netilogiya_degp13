# 1. Базовый образ
FROM continuumio/miniconda3:latest
# 2. Создаем папку /app и назначаем ее рабочей
RUN mkdir -p /app
WORKDIR /app
# 3. Переносим файл с требованиями и bash скрипт в рабочую папку
COPY requirements.txt requirements.txt
COPY 1.sh 1.sh
# 4. Устанавливаем в конду пакеты из файла с требованиями
RUN conda config --append channels conda-forge
RUN conda install --file requirements.txt
# 5. Выдаем файлу 1.sh права на исполнение. Путь приписывать не надо, т.к. он и без того в рабочей папке /app
RUN chmod +x 1.sh
# 6. Выполняем файл 1.sh
CMD ["/app/1.sh"]