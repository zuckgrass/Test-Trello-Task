
# Trello Card Creation CLI

This is a **Python command-line interface (CLI)** program that allows users to add a card to a **Trello** board. The program can add a Trello card with **labels** and a **comment** to a specified column (list) on a board.

## Features

- Create Trello cards via the command line.
- Input your Trello API key, token, list ID, card name, labels, and comments interactively.
- Labels can be specified as a **comma-separated** list.
- A comment can be added to the card if desired.
- The program **validates** your API credentials and the list ID before proceeding with card creation.

## Prerequisites

Before running the script, make sure you have the following:

- **Python 3.x** installed on your machine.
- **Trello API Key** and **Trello API Token** (You can obtain these from your Trello account).
- **Trello List ID** (The ID of the list where the card will be added).

## Usage

### Run the Python Script

```
python trello-cli.py
```
## Input Details
You will be prompted to enter the following details:

- API Key: Your Trello API key.
- API Token: Your Trello API token.
- List ID: The ID of the list where the card will be added.
- Card Name: The name/title of the card to be created.
- Labels (optional): A comma-separated list of labels (e.g., important, urgent).
- Comment (optional): A comment to add to the card.

## Example Input
```
Enter your Trello API key: <your-api-key>
Enter your Trello API token: <your-api-token>
Enter the Trello list ID: <your-list-id>
Enter the card name: Trello Card
Enter labels (comma-separated, optional): important,urgent
Enter a comment (optional): This is a comment.
```
## Example Output
```
Card created successfully: https://trello.com/c/<card-id>
```
## Error Handling
- If an invalid API key or token is provided, the program will notify you and will not proceed with card creation.
- If an invalid list ID is provided, the program will notify you and will not proceed with card creation.
- The program will raise an error if the Trello API request fails (e.g., network issues or API server problems).
## Next Development Steps
- Error Logging: Implement logging for better error tracking and debugging.
- Advanced Features: Add support for additional Trello card attributes like due dates, members, etc.
- Unit Testing: Write unit tests to validate the functionality of individual methods.
- User Authentication: Implement user authentication to manage multiple Trello boards and lists.
