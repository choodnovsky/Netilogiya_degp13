# 1. Базовый образ
FROM continuumio/miniconda3:latest
# 2. Копируем все что есть в рабочей папке проекта в образ в папку которую укажем. Если такой папке нет - создаем
COPY . /app
# 3. Назначаем созданную папку рабочей
WORKDIR /app
# 4. Обычно файл с требованиями копируется, но он уже перенесен в папку /app на шаге №2
#COPY requirements.txt requirements.txt
# 5. Выдаем файлу 1.sh права на исполнение. Путь приписывать не надо, т.к. он и без того в рабочей папке /app
RUN chmod +x 1.sh
# 6. Устанавливаем в конду пакеты из файла с требованиями
RUN conda config --append channels conda-forge
RUN conda install --file requirements.txt
# 7. Выполняем файл 1.sh
RUN bash 1.sh