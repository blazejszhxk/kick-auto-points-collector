import time
import random
import json
import threading
import cloudscraper

with open('config.json', 'r') as f:
    config = json.load(f)

def cl_sm(nick):
    scraper = cloudscraper.create_scraper()
    
    channel_url = f"https://kick.com/api/v2/channels/{nick}"
    
    try:
        channel_response = scraper.get(channel_url)
        channel_data = channel_response.json()
        
        if channel_data.get("livestream") is None:
            return False, None
        
        chatroom_id = channel_data.get("chatroom", {}).get("id")
        if not chatroom_id:
            return False, None
        
        message_url = f"https://kick.com/api/v2/messages/send/{chatroom_id}"
        
        random_message = random.choice(config["messages"])
        
        message_ref = str(random.randint(1000000000000, 9999999999999))
        
        payload = {
            "content": random_message,
            "type": "message",
            "message_ref": message_ref
        }
        
        headers = {
            "Authorization": config["authorization"]
        }
        
        scraper.post(message_url, json=payload, headers=headers)

        return True, random_message
        
    except Exception as e:
        return False

def monitor(nick):
    while True:
        try:
            message_sent, random_message = cl_sm(nick)

            if message_sent:
                wait_time = random.randint(
                    config["wait_times"]["livestream_active"]["min"], 
                    config["wait_times"]["livestream_active"]["max"]
                )
                current_time = time.strftime("%H:%M:%S", time.localtime())
                print(f"[{current_time}] Wysłałem do {nick}: {random_message} Czekam {wait_time} sekund.")
            else:
                wait_time = config["wait_times"]["livestream_inactive"]
                current_time = time.strftime("%H:%M:%S", time.localtime())
                print(f"[{current_time}] {nick} nie ma streama. Czekam {wait_time} sekund.")
            
            time.sleep(wait_time)
        except Exception as e:
            time.sleep(config["wait_times"]["error_wait"])

def main():
    channels = config["channels"]
    
    threads = []
    for nick in channels:
        thread = threading.Thread(target=monitor, args=(nick,), daemon=True)
        threads.append(thread)
        thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()