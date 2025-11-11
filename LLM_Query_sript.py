import json
import requests
import os

def LLMQuery(Query, Table):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }

    # Промпт
    prompt = f"Ответь да или нет (КРАТКО обоснуй) на вопрос: {Query}. Ответ ищи тут: {Table}"

    # Подготовка данных для отправки
    data = {
        "model": "deepseek/deepseek-r1-0528-qwen3-8b",  # Оставьте пустым или укажите имя модели, если нужно
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500,
        "stream": False  # Установите True, если хотите получать потоковый ответ
    }

    # Отправка запроса
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Проверка статуса ответа
    response.raise_for_status()

    # Извлечение ответа
    result = response.json()
    answer = result['choices'][0]['message']['content']

    print("Ответ LLM:")
    print(answer)

directory_path = "D:\program\PanTabFact\PanTabFact_DATA"

for fileName in os.listdir(directory_path):
    file_path = os.path.join(directory_path, fileName)
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Ошибка при чтении JSON из файла: {fileName}")
        for data_elm in data:
            
            print("---------------------------")
            print(data_elm.get("statement"))
            
            LLMQuery(data_elm.get("statement"), data_elm.get("table_text"))
            print("Верный ответ")
            print(data_elm.get("label"))
            
    break       
