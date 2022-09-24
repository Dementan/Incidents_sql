import sqlite3

conn=sqlite3.connect("incidents.db")

cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY AUTOINCREMENT,the_date DATETIME, incident_type TEXT, message_source TEXT)")
a=["3.09.22", "3.09.22", "4.09.22", "6.09.22","6.09.22", "7.09.22","8.09.22", "9.09.22","9.09.22", "10.09.22"]
b=["кража", "дтп", "пожар", "убийство","разбой", "хулиганство","дтп", "кража","убийство", "кража"]
c=["Иванова ТП", "Петрова ДИ", "Мухоморова ВЕ", "Васильев НЗ","Кулебяка РП", "Савельев ДВ","Сидоров КТ", "Мухина КВ","Лаврентьев ТХ", "Рушайло УЖ"]
cursor.execute("INSERT INTO messages (the_date, incident_type, message_source) VALUES (?,?,?)", (a, b, c))
conn.commit()

cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS solutions(id INTEGER PRIMARY KEY AUTOINCREMENT, message_number INTEGER, result_type TEXT")
d=["SELECT FROM messages ORDERED BY id INTEGER PRIMARY KEY AUTOINCREMENT"]
e=["отказано", "отправлено", "возбуждено", "возбуждено","отказано", "возбуждено","отправлено", "отказано","возбуждено", "отправлено"]
cursor.execute("INSERT INTO solutions (message_number, result_type ) VALUES (?,?)", (d, e))
conn.commit()

cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS participants (id INTEGER PRIMARY KEY AUTOINCREMENT, incident_number INTEGER , full_name TEXT, address TEXT, criminal_record INTEGER, fingerprints TEXT, status TEXT)")
d=["SELECT FROM messages ORDERED BY id INTEGER PRIMARY KEY AUTOINCREMENT"]
f=["Люциферова АВ", "Смирнов ЖЗ", "Кривоногова АЦ", "Преступников ДИ","Лучезарный КВ", "Простенко ХЗ","Цукатова НД", "Комаров ПИ","Пилипчик АН ", "Косогоров ФР"]
g=["Минск, Космонавтов 54-37", "Марьина горка, Галицкого 34-98", "Минск, Мирошниченко 18-26", "Борисов, Осипенко 45-19","Молодечно, Ленина 76-73", "Вилейка, Пролетарская 56-23","Боровляны, Шумейко 34-88", "Могилев, Победы 56-78","Бобруйск, Гинтовта 24-46", "Минск, Гикало 98-11"]
h=["0", "1", "0", "2","3", "0","0", "2","1", "1"]
i=["есть", "есть", "нет", "нет","есть", "есть","нет", "есть","есть", "нет"]
j=["потерпевший", "виновен", "свидетель", "убийство","подозреваемый", "виновен","подозреваемый", "потерпевший","виновен", "свидетель"]
cursor.execute("INSERT INTO participants (incident_number, full_name , address, criminal_record, fingerprints, status) VALUES (?,?,?,?,?,?)", (d, f, g, h, i, j))
conn.commit()

cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS responsible_officer (id INTEGER PRIMARY KEY AUTOINCREMENT,incident_number INTEGER , certificate_number INTEGER , rank TEXT, full_name TEXT, officer_address TEXT , family_composition TEXT)")
d=["SELECT FROM messages ORDERED BY id INTEGER PRIMARY KEY AUTOINCREMENT"]
k=["2233", "1122", "8877", "9966"]
l=["сержант", "майор", "лейтенант", "оперативник"]
m=["Панкратов НК", "Панкреатитов ЖК","Муравьева КЗ", "Брови ЛЦ"]
n=["Минск, Уручская 18-23","Минск, Победителей 12-16","Минск, Независимости 46-73","Минск, Строителей 14-81"]
o=["женат, 2 детей", "женат, 3 детей","неженат, 0 детей", "неженат, 1 ребенок"]
cursor.execute("INSERT INTO data_about_messages (incident_number, certificate_number, rank, full_name, officer_address, family_composition) VALUES (?,?,?,?,?,?)", (d, k, l, m, n, o))
conn.commit()

cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS incident_information(id INTEGER PRIMARY KEY AUTOINCREMENT, incident_number INTEGER, responsible_officer_id INTEGER, incident_scene TEXT, description TEXT)")
d=["SELECT FROM messages ORDERED BY id INTEGER PRIMARY KEY AUTOINCREMENT"]
p=["8877", "1122", "2233", "9966","8877", "2233","9966", "1122","8877", "1122"]
q=["Минск, Хоружей 15-67","Минск, Кульман 21-65","Минск, Куйбышева 32-87","Минск, Машерова 14-56","Минск, Ванеева 67-28","Минск, Золотая горка 23-89","Минск, Коласа 98-74","Минск, Дзержинского 78-67","Минск, Щорса 77-311","Минск, Свердлова 84-39"]
r=["украден велосипед", "автомобиль сбил лошадь", "мужчина курил в постели", "муж убил соседа из личной неприязни","ворвался в магазин и унес кассу", "разбил окно в здании школы","наезд на пешехода", "украл кошелек в автобусе","по неосторожности застрелил на охоте", "выманил деньги с карты"]
cursor.execute("INSERT INTO data_about_messages (incident_number, responsible_officer_id , incident_scene, description) VALUES (?,?,?,?)", (d, p, q, r))
conn.commit()