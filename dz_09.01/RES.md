1. Составляем [Dockerfile](./Dockerfile) выполняем сборку командой `docker build . -t netology-ml:netology-ml`
2. Чтобы процесс сборки отображался в терминале и записывался в лог расширяем команду до `docker build . -t netology-ml:netology-ml --no-cache --progress=plain 2>&1 | tee build.log`
![build.png](build.png). В рультате получаем [build.log](./build.log)
3. Проверяем наличие собранного образа командой `docker images`

![images.png](images.png)
