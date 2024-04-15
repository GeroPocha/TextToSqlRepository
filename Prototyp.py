import os
import time
import mysql.connector
from openai import OpenAI
from prompts import system_prompts, user_prompts, loesungen
from mysql.connector import connect, Error

def get_database_connection():
    #Stellt eine Verbindung zur Datenbank her.
    try:
        connection = connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return connection
    except Error as e:
        print(f"Fehler beim Verbinden zur MySQL-Datenbank: {e}")
        exit(1)

def query_database(cursor, query):
    #Führt eine SQL-Abfrage aus und gibt das Ergebnis zurück.
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f"Fehler bei der SQL-Abfrage: {e}")
        return None

def clean_result(result):
    #Bereinigt das Datenbankergebnis zur weiteren Verarbeitung.
    return ''.join(str(result).split())

def run_prompts():
    db_connection = get_database_connection()
    cursor = db_connection.cursor()
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    for prompt_name, prompt_details in system_prompts.items():
        prompt_text = prompt_details['prompt']
        for temperature in [0, 0.5, 1]:
            start_time = time.time()
            korrekte_ergebnisse = 0
            verbrauchte_tokens = 0
            for index, task in enumerate(user_prompts):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": prompt_text},
                        {"role": "user", "content": task}
                    ],
                    temperature=temperature
                )
                verbrauchte_tokens += response.usage.total_tokens
                generated_query = response.choices[0].message.content
                result = query_database(cursor, generated_query)
                if result and clean_result(result) == loesungen[index]:
                    korrekte_ergebnisse += 1
            end_time = time.time()

            print(f"Ergebnisse für Systemprompt {prompt_name} und Temperature {temperature}:")
            print(f"Laufzeit: {(end_time - start_time) * 1000:.2f} ms")
            print(f"Anzahl korrekter Ergebnisse: {korrekte_ergebnisse}/{len(user_prompts)}")
            print(f"Anzahl verbrauchter Tokens: {verbrauchte_tokens}")

    db_connection.close()

if __name__ == "__main__":
    run_prompts()
