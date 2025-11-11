import json
import os
from collections import defaultdict
from google.colab import drive

# Подключаем Google Диск
drive.mount('/content/drive')

# Путь к JSON-файлу на Google Диске
file_path = '/content/drive/MyDrive/PanTabFact.json'

# Открываем и читаем JSON-файл
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Загружено {len(data)} объектов из JSON-файла.")

# Группировка данных по 'table_caption'
grouped_data = defaultdict(list)
for item in data:
    grouped_data[item['table_caption']].append(item)

# Путь к папке для сохранения файлов на Google Диске
output_dir = '/content/drive/MyDrive/PanTabFact_DATA'

# Создание папки, если она не существует
os.makedirs(output_dir, exist_ok=True)

# Сохранение каждой группы в отдельный JSON-файл
for caption, entries in grouped_data.items():
    # Очистка имени файла от недопустимых символов
    safe_caption = "".join([c for c in caption if c.isalnum() or c in (' ', '.', '_')]).rstrip()
    file_name = f"PanTabFact_{safe_caption}.json"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=4)

    print(f"Сохранено {len(entries)} объектов в файл: {file_path}")
