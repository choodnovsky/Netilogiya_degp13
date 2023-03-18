## **Выполнение задания**:

1. Колнируем репозиторий Штефана Продана- https://github.com/stefanprodan/dockprom
2. Собираем (там и без того все уже собрано)
3. Поднимаем `docker-compose up -d`
4. Проверяем, что всё работает через `docker ps` ![docker_ps.png](docker_ps.png)
так же все работает в дашборде docker desktop ![docker_dt.png](docker_dt.png) и в pycharm ![docker_pc.png](docker_pc.png)
5. Логинимся в Prometheus и изучаем настроенные alerts, rules  
в интерфейсе __alerts__ видим 7 алертов в своих разделах с расчитанными на PromQL метриками ![prometheus_alerts.png](prometheus_alerts.png)
эти же 7 алертов со своими порогами срабатывания содержатся в rules в аналогичных разделах ![prometheus_rules.png](prometheus_rules.png)
6. Логинимся в Grafana
7. Смотрим, что настроено в дашбордах и explore
Дошборды разбиты на группы согласно конфигурационным файлам из предложенного репозитория
    - Docker Containers  
    - Docker Host  
    - Monitoring Services  
    - Ngnix

Более подробно на дашборде __Docker Containers__ расположены визуализации использования ресурсов контейнеров ![grafana_docker_containers.png](grafana_docker_containers.png)
в разделе __Explore__ пошагово описаны расчеты метрик ![grafana_explore.png](grafana_explore.png)