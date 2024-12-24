import argparse
import requests

BASE_URL = "https://api.trello.com/1"

def validate_credentials(api_key, token):
    #Validate the Trello API key and token.
    url = f"{BASE_URL}/members/me"
    params = {"key": api_key, "token": token}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return True
    print("Invalid API key or token. Please check your credentials.")
    return False

def validate_list(api_key, token, list_id):
    #Validate if the provided list ID exists.
    url = f"{BASE_URL}/lists/{list_id}"
    params = {"key": api_key, "token": token}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return True
    print("Invalid list ID. Please check the list ID.")
    return False

def create_card(api_key, token, list_id, card_name, labels, comment):
    #Create a Trello card
    validate_credentials(api_key, token)
    validate_list(api_key, token, list_id)
    card = add_card(api_key, token, list_id, card_name)
    card_id = card['id']

    if labels:
        add_labels(api_key, token, card_id, labels)

    if comment:
        add_comment(api_key, token, card_id, comment)

    print(f"Card created successfully: {card['shortUrl']}")

def add_card(api_key, token, list_id, card_name):
    #Add a new card to the specified list.
    url = f"{BASE_URL}/cards"
    params = {"key": api_key, "token": token, "idList": list_id, "name": card_name}
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()

def add_labels(api_key, token, card_id, labels):
    #Add labels to the card.
    for label in labels.split(','):
        url = f"{BASE_URL}/cards/{card_id}/labels"
        params = {"key": api_key, "token": token, "name": label.strip()}
        requests.post(url, params=params).raise_for_status()

def add_comment(api_key, token, card_id, comment):
    #Add a comment to the card.
    url = f"{BASE_URL}/cards/{card_id}/actions/comments"
    params = {"key": api_key, "token": token, "text": comment}
    requests.post(url, params=params).raise_for_status()

if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Add a card to a Trello board.")
    parser.add_argument("api_key")
    parser.add_argument("token")
    parser.add_argument("list_id")
    parser.add_argument("card_name")
    parser.add_argument("--labels", default="")
    parser.add_argument("--comment", default="")

    api_key = input("Enter your Trello API key: ")
    token = input("Enter your Trello API token: ")
    list_id = input("Enter the Trello list ID: ")
    card_name = input("Enter the card name: ")
    labels = input("Enter labels (comma-separated, optional): ")
    comment = input("Enter a comment (optional): ")
    
    # Pass arguments to parser.parse_args() as a list of strings
    args = parser.parse_args([api_key, token, list_id, card_name, '--labels', labels, '--comment', comment])
    
    try:
        create_card(args.api_key, args.token, args.list_id, args.card_name, args.labels, args.comment)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
