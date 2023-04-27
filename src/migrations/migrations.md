>• ___Миграции aerich___

1. __Инициализируем aerich:__ ``aerich init -t app.settings.components.TORTOISE_ORM``
2. __Инициализируем бд:__ ``aerich init-db``
3. __Создаем миграцию:__ ``aerich migrate --name MIGRATION_NAME``
4. __Обновляем:___ ``aerich upgrade``
