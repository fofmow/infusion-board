## Быстрый Старт
1. Клонируйте репозиторий себе на устройство с помощью команды 
`git clone https://github.com/fofmow/infusion-board `
2. Откройте корневую папку проекта и создайте в ней виртуальное окружение (ВО) —
`python -m venv venv`. Версия Python должна быть не ниже 3.9
3. Активируйте ВО: `venv/Scripts/activate` на Windows или `source venv/bin/activate` на Linux
4. Обновите pip: `python -m pip install -U pip`
5. Установите необходимые зависимости: `pip install -r requirements.txt`
6. Создайте в корневой директории файл .env и укажите в нем следующие параметры:
   * `BOT_TOKEN`=Токен бота, полученный от BotFather
   * `WEB_APP_URL`=Ссылка на веб-приложение с протоколом https
   * `DB_NAME`=Название базы данных (БД)
   * `DB_USER`=Имя пользователя БД
   * `DB_PASSWORD`=Пароль БД
   * `DB_HOST`=Хост БД
   * `DB_PORT`=Порт БД
   * `HR_TG_ID`=Телеграм ID HR
   * `HR_TG_ACCOUNT_URL`=ссылка на Телеграм аккаунт HR
   * `DEFAULT_ACTIVATION_WORD`=кодовое слово для авторизации по умолчанию
7. Создайте файл `auth.json` в директории `storage` c содержанием: `{"start_code_word": "<auth_word>"}`
8. Запустите файл main.py в интерпретаторе Python.


## Исторический Контекст
Проект зародился на хакатоне, проводимым Росмолодежью с 17.02.2023 по 19.02.2023. 
Решение направлено на улучшение процесса адаптации новых сотрудников агенства, простое 
и интерактивное погружение их в корпоративную среду c выполнением при этом всех необходимых действий.

Командный Состав (ссылки на телеграм):
- [Backend Developer](https://t.me/fofmow) (Никита Прожога)
- [Frontend Developer](https://t.me/just_vv) (Василий Жестков)
- [Designer](https://t.me/Nikky3004) (Вероника Шудина)
- [Designer](https://t.me/Ekaterinaovm) (Екатерина Михайлова)

[ПРЕЗЕНТАЦИЯ ПРОЕКТА](https://github.com/fofmow/infusion-board/blob/master/static/HaHaTown.pdf)

[ПРЕЗЕНТАЦИЯ на Behance](https://www.behance.net/gallery/167591761/Web-App-dlja-onbordinga)
