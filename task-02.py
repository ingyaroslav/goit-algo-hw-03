import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Введення рівня рекурсії
    level = int(input("Введіть рівень рекурсії для побудови сніжинки Коха: "))

    # Створення екземпляра вікна та черепашки
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    t.speed(0)

    # Побудова сніжинки Коха
    for i in range(3):
        koch_snowflake(t, level, 300)
        t.right(120)

    # Завершення програми при кліку на вікно
    window.exitonclick()

if __name__ == "__main__":
    main()