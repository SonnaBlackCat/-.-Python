preparation = [
    ("Амоксицилін", 50,"antibiotic", 4.5)
    ("Вітамін С", 100, "vitamin", 22.0)
    ("Вакцина грипу", 30, "vaccine", 2.0)
    ("Парацетамол", 20, "medicine", 20.0)
    ("Вакцина БЦЖ", 10, "мфссшту", 8.0)
    ("Невідомий препарат", 5, "something", 30.0)
    ("Аспірин", 75, "antibiotic", 18.5)
]

for name, quantity, category, temp in preparations:
    if not isinstance(quantity, int) or not isinstance(temp, (int, float)):
        print(f"{name}: Помилка даних.")
        continue
    
    match category:
        case "antibiotic":
            category_status = "Рецептурний препарат"
        case "vitamin":
            category_status = "Вільний продаж"
        case "vaccine":
            category_status = "Потрібує спецзберігання"
        case _:
            category_status = "Невідома категорія"
            
    if temp < 5:
        temp_status = "Надто холодно"
    elif temp > 25:
        temp_status = "Надто жарко"
    else:
        temp_status = "Норма"
        
    print(f"Назва:{name}")
    print(f"Статус категоії: {category_status}")
    print(f"Стан температури: {temp_status}")
    print()