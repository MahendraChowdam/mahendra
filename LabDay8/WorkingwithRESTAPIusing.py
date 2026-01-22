import requests
import json

def fetch_and_save_users():
    # Public REST API endpoint
    url = "https://jsonplaceholder.typicode.com/users"

    # Custom headers
    headers = {
        "User-Agent": "Python-API-Client",
        "Accept": "application/json"
    }

    try:
        # Send GET request
        response = requests.get(url, headers=headers, timeout=10)

        # Raise exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()

        # Parse JSON response
        users = response.json()

        # Extract specific fields
        extracted_data = []
        for user in users:
            extracted_data.append({
                "id": user.get("id"),
                "name": user.get("name"),
                "email": user.get("email"),
                "city": user.get("address", {}).get("city")
            })

        # Serialize and save to JSON file
        with open("users_data.json", "w", encoding="utf-8") as file:
            json.dump(extracted_data, file, indent=4)

        print("Data successfully saved to users_data.json")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server")

    except requests.exceptions.Timeout:
        print("Error: Request timed out")

    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")

    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response")


# Run the function
if __name__ == "__main__":
    fetch_and_save_users()
