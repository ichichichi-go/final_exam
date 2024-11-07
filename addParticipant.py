import requests

def get_access_token():
    choice = input("Do you want to use the hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
        access_token = "Bearer " + access_token
    else:
        access_token = "Bearer ZmZhNTA0YzEtNzc5Mi00OGE2LTk4NGYtMTM1YWE2MjA1YTVlNzRlZGY2ZDQtOGIx_P0A1_856a32b6-339b-4d3d-89fb-dabbd25aff7b"
    return access_token

def create_membership(access_token, room_id, person_email):
    headers = {"Authorization": access_token, "Content-Type": "application/json"}
    data = {"roomId": room_id, "personEmail": person_email}
    response = requests.post("https://webexapis.com/v1/memberships", headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def main():
    access_token = get_access_token()
    room_id = input("Enter the ID of the room: ").strip()
    
    while True:
        person_email = input("Enter the email of the person (type 'exit' to stop): ").strip()
        if person_email.lower() == "exit":
            break
        create_membership(access_token, room_id, person_email)
        print("Membership created successfully.")

if __name__ == "__main__":
    main()
