## Diplom_2


### содержание

- [start](#)
- [conftest](#conftest)
- [tests](#tests)
- [allure_results](#allure_results)
- [data](#data)
- [methods](#methods)

### start

####$ Для запуска проекта нужно использовать следующее:

импортировать библиотеки:
pytest, allure, webdriver


для запуска всех автотестов с формированием актуальных отчетов:
```
 pytest test_create_order.py test_create_user.py test_changing_data_users.py test_login.py test_take_order_user.py --alluredir=allure_results
```

открыть в браузере сформированные отчеты:

```
allure serve allure_results 
```


### conftest
В нем лежит стартовая фикстура, в которую передается сгенерированные данные для создание пользователя.
Также после окончания работы теста, созданный пользователь - удаляется 


### tests
Здесь лежат тесты


### allure_results
Тут лежат отчеты. 

###  data
В этот файл вынесены данные, которые переиспользуются в разных тестах.
Есть урлы для апи и текста проверок.


### methods
В этом файле ежит генератор данных для создания пользователя