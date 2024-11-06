import pandas as pd
import numpy as np
from random import randint, choice

# NumPy의 벡터화 연산을 사용하여 더 빠르게 데이터 생성
n_samples = 1000
temperature = np.random.randint(20, 41, n_samples)
humidity = np.random.randint(40, 91, n_samples)
wind_speed = np.round(np.random.uniform(0, 5, n_samples), 1)
weather = np.random.choice(["clear", "clouds", "rain", "fog"], n_samples)
time_of_day = np.random.choice(["morning", "afternoon", "evening", "night"], n_samples)

# 벡터화된 조건문으로 action 결정
condition1 = (temperature > 30) & (humidity > 60)
condition2 = (temperature > 28) & (humidity > 70) & np.isin(time_of_day, ["afternoon", "evening"])
action = np.where(condition1 | condition2, 1, 0)

# DataFrame 한번에 생성
df = pd.DataFrame({
    "Temperature": temperature,
    "Humidity": humidity,
    "Weather": weather,
    "Wind Speed": wind_speed,
    "Time of Day": time_of_day,
    "Action": action
})

# 데이터 확인
print(df.head(10))

# CSV로 저장 (원하는 경우)
df.to_csv("simulated_weather_data.csv", index=False)