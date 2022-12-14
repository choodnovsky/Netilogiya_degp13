from pyspark.sql import SparkSession
from pyspark.sql.window import Window # класс окна
from pyspark.sql import functions as f  # импортируем функции
import os
import time

start_time = time.time()
print(time.strftime("%T", time.localtime()) + "   Создаем сессию")

spark = SparkSession.builder\
    .master('local[*]')\
    .appName('dz_05.02')\
    .getOrCreate()

print(time.strftime("%T", time.localtime()) + "   Считываем сырой файл")

df = spark.read\
    .option('inferSchema', True)\
    .option('sep', ',')\
    .option('header', True)\
    .csv('Downloads/covid-data.csv')

# создаем объект окна
windowSpec = Window()

df.printSchema()
'''
Задание 1
Выберите 15 стран с наибольшим процентом переболевших на 31 марта
(в выходящем датасете необходимы колонки: iso_code, страна, процент переболевших)
'''

df_1 = df.filter(
    (f.col('date') <= f.lit('2022-03-31')) &
    (~f.col('iso_code').contains('OWID')) |
    (f.col('iso_code').contains('KOS'))).select([
    'iso_code',
    'location',
    'total_cases',
    'population'])

res_1 = df_1.groupBy('iso_code', 'location').agg(
    (f.max('total_cases') / f.max('population') * 100).alias('percent'))\
    .orderBy(f.col('percent').desc()).limit(15)
res_1 = res_1.withColumn('percent', f.concat(f.round(res_1['percent'], 2), f.lit('%')))

print(time.strftime("%T", time.localtime()) + "   Выполнено 1 задание")

'''
Задание 2.
Top 10 стран с максимальным зафиксированным кол-вом новых случаев 
за последнюю неделю марта 2021 в отсортированном порядке по убыванию 
(в выходящем датасете необходимы колонки: число, страна, кол-во новых случаев)
'''

df_2 = df.filter(
    ((f.col('date') >= f.lit('2021-03-25')) & (f.col('date') <= f.lit('2021-03-31'))) &
    ((~f.col('iso_code').contains('OWID')) | (f.col('iso_code').contains('KOS'))))\
    .select([
    'location',
    'new_cases',
    'date']).withColumn('date', f.col('date').cast('date'))

res_2 = df_2.withColumn('row_number', f.row_number().over(
    windowSpec.partitionBy('location').orderBy(f.col('new_cases').desc())))\
    .filter(f.col('row_number') == f.lit(1))\
    .select([
    'location',
    'new_cases',
    'date']).orderBy(f.col(
    'new_cases').desc()).limit(10)

print(time.strftime("%T", time.localtime()) + "   Выполнено 2 задание")

'''
Задание 3
Посчитайте изменение случаев относительно предыдущего дня в России за последнюю неделю марта 2021. 
(например: в россии вчера было 9150 , сегодня 8763, итог: -387) 
(в выходящем датасете необходимы колонки: число, кол-во новых случаев вчера, кол-во новых случаев сегодня, дельта)
'''

df_3 = df.filter(
    (f.col('date') >= f.lit('2021-03-25')) &
    (f.col('date') <= f.lit('2021-03-31')) &
    (f.col('iso_code') == f.lit('RUS')))\
    .select([
    'date',
    'new_cases']).withColumn('date', f.col('date').cast('date'))

df_3 = df_3.withColumn(
    'prev_day_cases', f.lag(f.col('new_cases'), 1)\
        .over(windowSpec.partitionBy(f.lit(0)).orderBy('date')))\
    .withColumn('prev_day_cases', f.coalesce('prev_day_cases', 'new_cases'))

res_3 = df_3.withColumn('delta', f.col('new_cases') - f.col('prev_day_cases'))

print(time.strftime("%T", time.localtime()) + "   Выполнено 3 задание")

# Удаляем ранее созданные папки с результатами в случае перезапуска скрипта
path = f'{os.getcwd()}/dz_05.02/'  # Определяем путь до папки в которуюю поместим папки с результатами
os.system(f'rm -rf {path}res_1 {path}res_2 {path}res_3')

# Сохраняем результаты в своих директориях

res_1.write.option('header', 'true').csv(f'{path}res_1')
res_2.write.option('header', 'true').csv(f'{path}res_2')
res_3.write.option('header', 'true').csv(f'{path}res_3')

'''если надо сохранить в GCP storage 
spark.conf.set("google.cloud.auth.service.account.enable", "true")
spark.conf.set("google.cloud.auth.service.account.email", "Your_service_email")
spark.conf.set("google.cloud.auth.service.account.keyfile", "path/to/your/files")

df = spark.write.option("header",True).csv("gs://bucket_name/path_to_your_file.csv")
df.show() 
'''

spark.stop()

print(time.strftime("%T", time.localtime()) + "   Результаты сохранены. Сессия завершена, время выполнения: " +
      str(round((time.time() - start_time), 2)) + " сек")
