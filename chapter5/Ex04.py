import matplotlib.pyplot as plt
import pandas as pd

data = {
    'city': ['LA', 'San Diego', 'San Jose', 'SF', 'Fresno',
             'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim'],
    'area_total_km2': [1302, 964, 467, 600, 298, 259, 132, 202, 390, 131]
}

df = pd.DataFrame(data)
df = df.sort_values(by='area_total_km2', ascending=False)

plt.barh(df['city'], df['area_total_km2'])

plt.title('Top 10 thành phố lớn nhất California (diện tích)')
plt.xlabel('Diện tích (km²)')
plt.ylabel('Thành phố')
plt.gca().invert_yaxis()
plt.show()