import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных из CSV-файла
data = pd.read_csv("восток-2_20241207201545.csv")

plt.figure(figsize=(15, 10))  # Увеличенный размер окна для размещения 4 графиков

# Первый график - наземная и орбитальная скорости
plt.subplot(2, 2, 1)  # 2 строки, 2 столбца, 1-й график
plt.plot(data['TimeSinceMark'], data['SpeedSurface'], label='Наземная скорость (м/c)', linewidth=2)
plt.plot(data['TimeSinceMark'], data['SpeedOrbital'], label='Орбитальная скорость (м/c)', linewidth=2, color='green')
plt.title("Скорости по времени")
plt.xlabel("Время (с)")
plt.ylabel("Скорость (м/c)")
plt.grid(True)
plt.legend()

# Второй график - высота
plt.subplot(2, 2, 2)  # 2 строки, 2 столбца, 2-й график
plt.plot(data['TimeSinceMark'], data['AltitudeASL'], label='Высота (м)', linewidth=2, color='orange')
plt.title("Высота по времени")
plt.xlabel("Время (с)")
plt.ylabel("Высота (м)")
plt.grid(True)
plt.legend()

# Третий график - масса
plt.subplot(2, 2, 3)  # 2 строки, 2 столбца, 3-й график
plt.plot(data['TimeSinceMark'], data['Mass'], label='Масса (т)', linewidth=2, color='purple')
plt.title("Масса по времени")
plt.xlabel("Время (с)")
plt.ylabel("Масса (т)")
plt.grid(True)
plt.legend()

# Четвёртый график - Delta V
plt.subplot(2, 2, 4)  # 2 строки, 2 столбца, 4-й график
plt.plot(data['TimeSinceMark'], data['DeltaVExpended'], label='Delta V (м/с)', linewidth=2, color='red')
plt.title("Delta V по времени")
plt.xlabel("Время (с)")
plt.ylabel("Delta V (м/с)")
plt.grid(True)
plt.legend()

# Отображение графиков
plt.tight_layout()  # Автоматическая компоновка для избежания наложений
plt.show()
