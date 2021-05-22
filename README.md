# Автоматический пересчёт рабочих объемов фьючерсов на бирже Binance для Cscalp.
# Automatic recalculation of working amounts of futures on the Binance exchange for Cscalp.

# Как это работает?
Скрипт получает от пользователя рабочие объемы в USDT в формате "300 600 900 1200 100", получает с Binance цену и шаг цены для каждого фьючерса, для каждого рабочего объема рассчитывает количество монет (рабочий объем / цена // шаг цены  * шаг цены), проходится по всем файлам с настройками cscalp и записывает рассчитанные значения.
Cscalp во время запуска не должен быть открыт.
Работает только с фьючерсами и только Binance.

Видео работы: https://www.youtube.com/watch?v=cbLUQegTwF0

# Предостережение:
Перед началом работы ознакомьтесь с лицензией и создайте резервную копию настроек стаканов и графиков Cscalp (C:\Users\WINDOWS_USER_NAME\AppData\Roaming\CScalp\Visualizer, где WINDOWS_USER_NAME - имя пользователя Windows)

# Требования:
* Доступ в интернет
* Python 3.8 (при установке поставить галочку "Add Python to environment variables")
* Библиотека requests
* Установленный Cscalp
* Преднастроенные стаканы инструментов

# Подготовка
Перед запуском программы нужно положить файлы cscalp_work_amounts.py и run.bat в папку с настройками стаканов Cscalp (путь:  C:\Users\WINDOWS_USER_NAME\AppData\Roaming\CScalp\Visualizer\mvs_cs, WINDOWS_USER_NAME нужно заменить на название пользователя windows (можно посмотреть в настройках или в папке C:\Users)).

Для удобства запуска можно создать ярлык для run.bat на рабочем столе (ПКМ - Отправить - Рабочий стол (создать ярлык)).

# Donate
Если эта программа вам помогла, не стесняйтесь поддержать автора:
* USDT TRC20: TYvX3gNRghPo6prxVxB9G1pcuEdvCtNUM9 
* BTC: 1A4cCqEBD7U6YLtMFsmqJqZLnKS3g9bZGy
* ETH ERC20: 0xcc559ad9e92621555310d8f5e923ee7a3d914471
* BNB BEP20 (BSC): 0xcc559ad9e92621555310d8f5e923ee7a3d914471
* LTC: LU5rNY1uJEvHpUoTJ8ma6FiG6aMxgxBrim
* BCH: 1A4cCqEBD7U6YLtMFsmqJqZLnKS3g9bZGy
* DOGE: D5wo6uqCxBgtXe4xKYQAvS9jYdorfnmVkD
* XRP BEP20 (BSC): 0xcc559ad9e92621555310d8f5e923ee7a3d914471
