## Запуск тестов и просмотр отчетов Allure

Создайте виртуальное окружение и активируйте его.

В рабочей директории Task_tensor_1_2_3 установите пакеты для работы следующей командой:
```html
pip install -r requirements.txt
```

В терминале в директории проекта Task_tensor_1_2_3 выполнить команду для запуска тестов и создания Allure отчетов в папке test_results/:
```html
python -m pytest --alluredir=test_results/
```

Для просмотра отчетов Allure в директории проекта Task_tensor_1_2_3 в терминале выполнить команду:
```html
allure serve test_results/
```
