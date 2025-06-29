<h1>WEATHER APPLICATION</h1>

<p style='text-align:  justify;'> 
    <span style='margin-left: 40px;'>Цей</span> 
    проєкт розроблено з метою ознайомлення із роботою 
    <a href='https://developer.mozilla.org/en-US/docs/Glossary/API'>API</a>, 
    принципом отримання даних від віддаленого серверу, вмінням обробляти дані, структурувати та застосовувати у свому проєкті. А саме застосовувалось API такого веб-ресурсу як 
    <a href='https://openweathermap.org/'>OpenWeatherMap</a>.
    Проєкт допоможе розібратисяс у роботі файлів
    <a href='https://www.json.org/json-uk.html'>JSON</a>, 
    як правильно отримувати та зберігати дані у файлах з типом json. Та познайомить користувача з інтерфейсом застосунку розробленим за допомогою пакету 
    <a href='https://customtkinter.tomschimansky.com/'>Custotkinter</a>.
</p>

<img src='/static/icon/screen.png'>

<h2>Зміст:</h2>
<ol>
    <li>
        <a href='#all-modules'>Модулі проєкту</a>.
    </li>
    <li>
        <a href='#download-project'>Розгортання проєкту</a>.
    </li>
    <li>
        <a href='#create-venv'>Створення віртуального оточення</a>.
        <ul>
            <li>
                <a href='#windows'>Для Windows</a>.
            </li>
            <li>
                <a href='#mac-os'>Для Mac OS</a>.
            </li>
        </ul>
    </li>
    <li>
        <a href='#download-modules'>Завантаження модулей до віртуального проєкту</a>.
        <ul>
            <li>
                <a href='#requriments'>Завантаження requriments.txt</a>.
            </li>
            <li>
                <a href='#Windows'>Windows</a>.
            </li>
            <li>
                <a href='#MacOS'></a>.
            </li>
            <li>
                <a href='#pip-install'>Завантаження окремих модулів</a>.
            </li>
        </ul>
    </li>
    <li>
        <a href='#start-project'>Старт проєкту</a>.
    </li>
    <li>
        <a href='#base-mechanics'>Основні механіки проєкту</a>.
    </li>
    <li>
        <a href='#result'>Висновок</a>.
    </li>
</ol>

<hr>

<hr>
<h3 id='all-modules'>Модулі проєкту</h3>
"Всі модулі"

    "1.customtkinter"

    "2.json"

    "3.colorama"

    "4.os"

    "5.requests"

    "6.pillow"

    "7.datetime"
<h3 id='download-project'>Розгортання проєкту</h3>
git clone https://github.com/your-username/Oleg-Weather-app.git

cd Oleg-Weather-app
<h3 id='create-venv'>Створеня віртуального оточення</h3>
<h3 id='windows'>Для Windows</h3>
python -m venv venv

venv\Scripts\activate
<h3 id='mac-os'>Для Mac OS</h3>
python3 -m venv venv

source venv/bin/activate
<h3 id='download-modules'>Завантаження модулів</h3>
<h3 id='requriments'>1 Варіант: Завантаженя із requirements.txt</h3>
pip install -r requirements.txt
<h3 id='download-modules'>2 Варіант:Завантаженя окремі модулі</h3>
pip install customtkinter requests
<h3 id='start-project'>Старт проєкту</h3>
Переходим в main.py и нажимаем на кнопку
<h3 id='result'>Висновок</h3>
Коли ми робили цей проєкт, ми дізналися, як працювати з API-запитами та отримувати інформацію у вигляді JSON-файлу. Ми навчились працювати з HTTP-запитами. Також ми навчилися створювати дизайн. І ще ми навчилися створювати файл у форматі .exe.
