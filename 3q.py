preparations = [
    ["Амоксицилін", 100, "antibiotic", 8.5],
    ["Вітамін С", 50, "vitamin", 22.0],
    ["Вакцина грип", 200, "vaccine", 2.0],
    [" Цефтріаксон", "багато", "antibiotic", 6.0],
    ["Вітамін D", 40, "vitamin", "тепло"],
]

for item in preparations:
    name = item[0]
    quantity = item[1]
    category = item[2]
    temperature = item[3]
    
    if not isinstance(quantity, int) or isinstance(quantity, bool):
        print(name, "- Помилка даних")
        continue
    if not isinstance(temperature, float) or isinstance(temperature, bool):
        print(name, "- Помилка даних")
        continue
    
    match category:
        case "antibiotic":
            category_status = "Рецептурний препарат"
        case "vitamin":
            category_status = "Вільний продаж"
        case "vaccine":
            category_status = "Потребує спецзберігання"
        case _:
            category_status = "Невідома категорія"
            
    if temperature < 5:
        temp_status = "Надто холодно"
    elif temperature > 25:
        temp_status = "Надто жарко"
    else:
        temp_status = "Норма"
        
    print(name, "-", category_status, "-", temp_status)
