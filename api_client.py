"""
Simple API Client (Task 27: Build a Simple API Client)
======================================================
Author: Hemasri Malla
API: JSONPlaceholder (https://jsonplaceholder.typicode.com)
Description:
    A beginner-friendly Python application that calls a public REST API,
    retrieves JSON data, handles network and response errors gracefully,
    and displays selected information in a clean, human-readable format.
"""

import sys
import json
import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException

# Base URL for JSONPlaceholder (Free public REST API requiring NO API key)
BASE_URL = "https://jsonplaceholder.typicode.com"

# Request timeout in seconds to prevent the program from hanging indefinitely
DEFAULT_TIMEOUT = 10


def fetch_data(url: str, params: dict = None):
    """
    Sends an HTTP GET request to the specified URL with an optional query parameter dictionary.
    
    Parameters:
        url (str): The endpoint URL to fetch data from.
        params (dict, optional): Query parameters to append to the URL.
        
    Returns:
        dict or list or None: The parsed JSON response on success, or None if an error occurs.
        
    Key Error Handling Covered:
        - HTTPError: Triggered by raise_for_status() for 4xx and 5xx status codes (e.g., 404 Not Found).
        - ConnectionError: Triggered when internet is disconnected or DNS fails.
        - Timeout: Triggered when the server fails to respond within DEFAULT_TIMEOUT seconds.
        - RequestException: Base class catch-all for any other requests-related issue.
        - ValueError / JSONDecodeError: Triggered if the response body is not valid JSON.
    """
    try:
        # Standard HTTP headers: specify we expect JSON response
        headers = {
            "Accept": "application/json",
            "User-Agent": "SimpleApiClient/1.0"
        }
        
        # Send the GET request with a timeout
        response = requests.get(url, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
        
        # Check HTTP status code
        # 200 OK means the request succeeded.
        # response.raise_for_status() will raise an HTTPError for 4xx or 5xx status codes.
        response.raise_for_status()
        
        # Parse and return JSON response
        return response.json()

    except HTTPError as http_err:
        status = response.status_code
        if status == 404:
            print(f"[!] Error: Resource not found (HTTP 404). Please verify the requested URL or ID.")
        elif status == 500:
            print(f"[!] Error: Internal Server Error (HTTP 500). The remote server encountered an error.")
        else:
            print(f"[!] HTTP error occurred (Status {status}): {http_err}")
        return None

    except ConnectionError:
        print("[!] Connection Error: Could not connect to the server.")
        print("    Please check your network connection or DNS settings.")
        return None

    except Timeout:
        print(f"[!] Timeout Error: The request took longer than {DEFAULT_TIMEOUT} seconds to respond.")
        return None

    except RequestException as req_err:
        print(f"[!] Network / Request Error: An unexpected request error occurred: {req_err}")
        return None

    except (ValueError, json.JSONDecodeError) as json_err:
        print(f"[!] JSON Parsing Error: Failed to decode response as JSON: {json_err}")
        return None

    except Exception as unexpected_err:
        # Safety net to guarantee the program never crashes with a raw traceback
        print(f"[!] Unexpected error occurred: {unexpected_err}")
        return None


def display_users_table(users: list):
    """
    Displays a list of users in a formatted table layout.
    """
    if not users:
        print("No users found to display.")
        return

    # Print table header
    header = f"{'ID':<4} | {'Name':<22} | {'Username':<15} | {'Email':<25} | {'City':<16}"
    separator = "-" * len(header)
    print("\n" + separator)
    print(header)
    print(separator)

    # Print each user row with safe fallbacks for missing fields
    for user in users:
        user_id = user.get("id", "N/A")
        name = user.get("name", "N/A")[:20]
        username = user.get("username", "N/A")[:13]
        email = user.get("email", "N/A")[:23]
        city = user.get("address", {}).get("city", "N/A")[:14]

        print(f"{user_id:<4} | {name:<22} | {username:<15} | {email:<25} | {city:<16}")
    
    print(separator)
    print(f"Total Users: {len(users)}\n")


def display_user_profile(user: dict):
    """
    Displays a single user's detailed profile in neatly labeled sections.
    """
    if not user:
        print("No user data available.")
        return

    address = user.get("address", {})
    company = user.get("company", {})

    print("\n" + "=" * 55)
    print(f" USER PROFILE : {user.get('name', 'N/A').upper()} (ID #{user.get('id', 'N/A')})")
    print("=" * 55)
    print(" [Basic Information]")
    print(f"  - Username : {user.get('username', 'N/A')}")
    print(f"  - Email    : {user.get('email', 'N/A')}")
    print(f"  - Phone    : {user.get('phone', 'N/A')}")
    print(f"  - Website  : {user.get('website', 'N/A')}")

    print("\n [Address Details]")
    print(f"  - Street   : {address.get('street', 'N/A')}, {address.get('suite', '')}")
    print(f"  - City     : {address.get('city', 'N/A')} (Zip: {address.get('zipcode', 'N/A')})")
    print(f"  - Geo      : Lat {address.get('geo', {}).get('lat', 'N/A')}, Lng {address.get('geo', {}).get('lng', 'N/A')}")

    print("\n [Company Details]")
    print(f"  - Company  : {company.get('name', 'N/A')}")
    print(f"  - Catchphrase: \"{company.get('catchPhrase', 'N/A')}\"")
    print(f"  - Business : {company.get('bs', 'N/A')}")
    print("=" * 55 + "\n")


def display_posts(posts: list, max_items: int = 5):
    """
    Displays posts authored by a user in clean cards.
    """
    if not posts:
        print("No posts found for this user.")
        return

    shown_posts = posts[:max_items]
    print("\n" + "-" * 60)
    print(f" POSTS (Showing {len(shown_posts)} of {len(posts)} posts)")
    print("-" * 60)

    for idx, post in enumerate(shown_posts, start=1):
        post_id = post.get("id", "N/A")
        title = post.get("title", "No Title").strip().capitalize()
        # Clean up newlines in body for neat preview
        body = post.get("body", "").replace("\n", " ")
        if len(body) > 90:
            body = body[:87] + "..."

        print(f" [{idx}] Post ID #{post_id}")
        print(f"     Title: {title}")
        print(f"     Body : {body}\n")
    print("-" * 60 + "\n")


def display_data(data, data_type: str = None):
    """
    Master display function to output retrieved data in a clean, aligned format.
    Automatically identifies the data shape (list of users, user profile, posts)
    or routes to the specified data_type.
    
    Parameters:
        data (list or dict): The JSON data returned by fetch_data.
        data_type (str, optional): 'users', 'user', 'posts', or None for auto-detection.
    """
    if data is None:
        print("[!] No data to display.")
        return

    # Explicit routing based on data_type argument
    if data_type == "users" and isinstance(data, list):
        display_users_table(data)
        return
    elif data_type == "user" and isinstance(data, dict):
        display_user_profile(data)
        return
    elif data_type == "posts" and isinstance(data, list):
        display_posts(data)
        return

    # Automatic structure detection
    if isinstance(data, list):
        if len(data) > 0 and isinstance(data[0], dict):
            if "email" in data[0] and "username" in data[0]:
                display_users_table(data)
            elif "title" in data[0] and "body" in data[0]:
                display_posts(data)
            else:
                print(json.dumps(data, indent=2))
        else:
            print(data)
    elif isinstance(data, dict):
        if "email" in data and "username" in data:
            display_user_profile(data)
        else:
            print("\n--- JSON Object ---")
            for key, value in data.items():
                print(f"  {key:<15}: {value}")
            print("-------------------\n")
    else:
        print(data)


def prompt_user_id() -> int:
    """
    Helper function to safely get and validate a positive user ID from user input.
    Guarantees no raw crashes from non-integer or negative inputs.
    """
    while True:
        raw = input("Enter User ID (1 to 10): ").strip()
        if not raw:
            print("[!] Input cannot be empty. Please enter a number.")
            continue
        try:
            val = int(raw)
            if val <= 0:
                print("[!] User ID must be a positive integer greater than 0.")
                continue
            return val
        except ValueError:
            print(f"[!] Invalid input '{raw}'. Please enter a valid number (e.g., 1, 2, 5).")


def main():
    """
    Main application flow: presents an interactive terminal menu allowing
    users to fetch users, inspect single profiles, view posts, or test error scenarios.
    """
    banner = """
=====================================================================
          SIMPLE REST API CLIENT (JSONPlaceholder Demo)
=====================================================================
  1. List All Users (Table format)
  2. View Single User Details by ID
  3. View Posts by User ID
  4. Test Error Handling (Invalid URL / 404 Simulation)
  5. Test Error Handling (Network Connection Error Simulation)
  6. Exit
====================================================================="""

    print(banner)

    while True:
        try:
            choice = input("\nSelect an option (1-6): ").strip()

            if choice == "1":
                print("\n--> Fetching all users from JSONPlaceholder...")
                url = f"{BASE_URL}/users"
                data = fetch_data(url)
                if data:
                    display_data(data, data_type="users")

            elif choice == "2":
                user_id = prompt_user_id()
                print(f"\n--> Fetching details for user #{user_id}...")
                url = f"{BASE_URL}/users/{user_id}"
                data = fetch_data(url)
                if data:
                    display_data(data, data_type="user")

            elif choice == "3":
                user_id = prompt_user_id()
                print(f"\n--> Fetching posts written by user #{user_id}...")
                url = f"{BASE_URL}/posts"
                params = {"userId": user_id}
                data = fetch_data(url, params=params)
                if data:
                    display_data(data, data_type="posts")

            elif choice == "4":
                print("\n--> Testing 404 Error handling with a non-existent URL endpoint...")
                invalid_url = f"{BASE_URL}/non_existent_endpoint_404"
                print(f"Requesting: {invalid_url}")
                fetch_data(invalid_url)

            elif choice == "5":
                print("\n--> Testing ConnectionError handling with an unreachable domain...")
                broken_url = "https://this-domain-does-not-exist-123456789.org/api"
                print(f"Requesting: {broken_url}")
                fetch_data(broken_url)

            elif choice == "6":
                print("\nThank you for using Simple API Client. Goodbye!\n")
                break

            else:
                print("[!] Invalid option selected. Please choose a number from 1 to 6.")

        except (KeyboardInterrupt, EOFError):
            print("\n\n[!] Program interrupted by user. Exiting gracefully. Goodbye!\n")
            sys.exit(0)
        except Exception as e:
            # Catch-all to guarantee menu loop never crashes
            print(f"[!] An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
