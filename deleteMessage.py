import requests

def get_access_token():
    choice = input("Do you want to use the hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
        access_token = "Bearer " + access_token
    else:
        access_token = "Bearer ZmZhNTA0YzEtNzc5Mi00OGE2LTk4NGYtMTM1YWE2MjA1YTVlNzRlZGY2ZDQtOGIx_P0A1_856a32b6-339b-4d3d-89fb-dabbd25aff7b"
    return access_token

def get_messages_in_room(access_token, room_id):
    headers = {"Authorization": access_token}
    params = {"roomId": room_id}
    response = requests.get("https://webexapis.com/v1/messages", headers=headers, params=params)
    response.raise_for_status()
    messages = response.json().get("items", [])
    message_info = [(message["id"], message["text"]) for message in messages]
    return message_info

def delete_message(access_token, message_id):
    headers = {"Authorization": access_token}
    response = requests.delete(f"https://webexapis.com/v1/messages/{message_id}", headers=headers)
    response.raise_for_status()
    print(f"Message {message_id} deleted successfully.")

def main():
    access_token = get_access_token()
    room_id = input("Enter the ID of the room: ").strip()
    
    # Retrieve and print message IDs and text in the room
    message_info = get_messages_in_room(access_token, room_id)
    print("Messages in the room:")
    for message_id, text in message_info:
        print(f"Message ID: {message_id}, Text: {text}")
    
    # Allow user to choose which message to delete
    message_id_to_delete = input("Enter the ID of the message you want to delete: ").strip()
    delete_message(access_token, message_id_to_delete)

if __name__ == "__main__":
    main()
