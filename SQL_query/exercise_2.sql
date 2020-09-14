/*
-----------------------------------------
Задача №2 Джоин версионных таблиц

На входе есть 2 таблички с наименованием продукта и ценой со следующей структурой:
Table1: product_id, date_from, date_to, product_name
Table2: product_id, date_from, date_to, product_price

Пример данных таблички1 (строк может быть сколько угодно):
1   01-DEC 15-DEC Молоко"Буренка"
1   16-DEC 31-DEC Молоко"Милка"

Пример данных таблички2 (строк может быть сколько угодно):
1   01-DEC 18-DEC 100
1   19-DEC 31-DEC 120

Считаем, что интервалы в таблицах непрерывные непересекающиеся, ключ в обеих - product_id, date_from

Нужно получить интервалы с общими интервалами с именем продукта и ценой, например:
1   01-DEC 15-DEC Молоко"Буренка" 100
1   16-DEC 18-DEC Молоко"Милка" 100
1   19-DEC 31-DEC Молоко"Милка" 120
--------------------------------------------

Ответ:
Синтаксис MySQL (просто он был установлен на домашнем ПК)
*/
SELECT
      TABLE1.PRODUCT_ID
    , GREATEST(TABLE1.DATE_FROM, TABLE2.DATE_FROM) AS DATE_FROM # из двух дат начал, оставляем макс
    , LEAST(TABLE1.DATE_TO, TABLE2.DATE_TO) AS DATE_TO # из двух дат концов, оставляем мин
    , TABLE1.PRODUCT_NAME
    , TABLE2.PRODUCT_PRICE
FROM TABLE1
CROSS JOIN TABLE2 ON TABLE1.PRODUCT_ID = TABLE2.PRODUCT_ID # пересекаем таблицы таблицы
WHERE TABLE1.DATE_FROM BETWEEN TABLE2.DATE_FROM AND TABLE2.DATE_TO # только пересек-ся интервалы
OR    TABLE1.DATE_TO BETWEEN TABLE2.DATE_FROM AND TABLE2.DATE_TO
OR    TABLE2.DATE_FROM BETWEEN TABLE1.DATE_FROM AND TABLE1.DATE_TO
OR    TABLE2.DATE_TO BETWEEN TABLE1.DATE_FROM AND TABLE1.DATE_TO
ORDER BY DATE_FROM;

/*
Я пологал что в полях таблиц DATE_FROM и  DATE_TO содержат формат даты. Если же это строка, везде следует писать STR_TO_DATE(CONCAT('10-AUG','-1900'), '%d-%M-%Y')
*/