# Определение персонажей игры.
define alexy = Character("Алексей", color="#f1f1f1")
define dmitry = Character("Дмитрий", color="#f1f1f1")
define mihail = Character("Михаил", color="#f1f1f1")
define victor = Character("Виктор", color="#f1f1f1")
define anna = Character("Анна", color="#f1f1f1")
define elena = Character("Елена", color="#f1f1f1")

init:
    $ left1 = Position(xalign=0.2, yalign=1.1)
    $ right1 = Position(xalign=0.8, yalign=1.1)
    $ right2 = Position(xalign=1.0, yalign=1.1)


label start:
    # Часть 1. Сцена 1.
    scene bg room_alex_city
    show alexy normal
    
    "Алексей пакует вещи, размышляя о своей новой работе. Он прощается с друзьями и семьей, полон надежд."
    
    scene bg sttreetintro
    with fade

    # Сцена 2
    show alexy normal at left1
    show dmitry normal at right1

    "Прибытие на арктическую станцию. Холод и снег, атмосфера изоляции. Его встречает Дмитрий, проводит инструктаж о правилах работы."

    # Сцена 3.
    scene bg sttreetintro

    "Первые дни адаптации к условиям. 
    Алексей становится ближе к Михаилу, который помогает ему разобраться в специфике работы. 
    Знакомится с Еленой, которая подбадривает его. Знакомится с Анной - руководителем станции."

    
    scene bg found_errors

    show alexy at left1
    show mihail normal at right1
    show anna at right2

    alexy "Хм.. Что-то тут не то..."
    
    "Алексей замечает сбои в передаче данных. 
    Настораживается и делится своими сомнениями с Анной и Михаилом, которые советует быть внимательным."


    return
