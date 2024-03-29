## Домашняя работа к занятию “Kubernetes (к8s)”
## **Цель задания**: 

Написать kubernetes-манифест чтобы понять, как описывать приложение в манифесте для развертывания в k8s.

## **Задание**:

1.	Ответить на вопросы:
   * Что такое k8s?   
   * В чём преимущество контейнеризации над виртуализацией?  
   * В чём состоит принцип самоконтроля k8s?
   * Как вы думаете, зачем Вам понимать принципы деплоя в k8s?
   * Какое из средств управления секретами наиболее распространено в использовании совместно с k8s? 
   * Какие типы нод есть в k8s, каковы их базовые функции?

2.   Написать манифест, который будет содержать в себе следующие условия:
   * apiVersion – v1  
   * название – netology-ml 
   * внутри него сервер приложений tomcat версии 8.5.69 с портом 8080
   * наличие 2 реплик 
   * использование стратегии rollingupdate

Домашнее задание выполните в файле readme.md в github репозитории.

## **Результат**:  
В личном кабинете отправьте на проверку ссылку на .md файл, содержащий ответы на вопросы и kubernetes-манифест.

Также вы можете выполнить задание в Google Docs и отправить в личном кабинете на проверку ссылку на ваш документ. Название файла Google Docs должно содержать номер лекции и фамилию студента. Пример названия: "1.2. Docker — Товаркин Мананаж" Перед тем как выслать ссылку, убедитесь, что ее содержимое не является приватным (открыто на комментирование всем, у кого есть ссылка). Если необходимо прикрепить дополнительные ссылки, просто добавьте их в свой Google Docs.

## **Инструменты**: 

Репозиторий с домашним заданием https://github.com/Netology-DS/devops-mlops/tree/master/k8s   

Любые вопросы по решению задач задавайте в чате Slack.