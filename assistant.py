import requests, json, os

API_KEY = os.getenv("OPENROUTER_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"

def main():
    if not API_KEY:
        print("Error: OPENROUTER_KEY missing.")
        return

    while True:
        try:
            inp = input("User > ")
            if inp.lower() in ['exit', 'quit']: break
            
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "openrouter/auto",
                "messages": [
                    {"role": "system", "content": "Your name is HK CORE AI. Created by Harii Kolariya."},
                    {"role": "user", "content": inp}
                ]
            }
            res = requests.post(URL, headers=headers, data=json.dumps(data)).json()
            print(f"\nHK-CORE > {res['choices'][0]['message']['content']}\n")
        except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    main()
  
