from config import API_ID, API_HASH, SESSIONS
from pyrogram import Client, idle


CLIENTS = []

for SESSION in SESSIONS:
    if SESSION:
        client = Client(
            session_name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="SavvySpam"),
        )
        CLIENTS.append(client)


if __name__ == "__main__":

    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("about_ranavanshi_divy")
            CLIENT.join_chat("about_ranavanshi_divy")
            print(f"---> Client {i+1} has been Started...")
        except Exception as e:
            print(e)

    print("💞YOUR ✨𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘✨ USERBOTS DEPLOYED SUCCESSFULLY 💞")
    idle()
