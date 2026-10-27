# Simple REST API Client 🌐

> **Task 27 (Level 1, Day 27): Build a Simple API Client**  
> A lightweight, beginner-friendly Python client demonstrating how to consume public REST APIs, handle JSON data, and manage network errors gracefully without crashing.

---

## 📌 Project Overview

This project demonstrates the fundamentals of consuming RESTful web services in Python using the standard `requests` library. It interacts with the free [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) to fetch user profiles and user posts, parses the returned JSON payload, and presents the data in a clean, human-readable terminal format (both tabular and structured card views).

### Key Highlights
- **Zero Secrets / No API Keys**: Uses public endpoints requiring no authentication credentials.
- **Robust Error Handling**: Handles network disconnects, timeouts, 404/500 HTTP errors, corrupted JSON, and invalid terminal inputs.
- **Traceback-Free**: Guarded with defensive exception blocks to ensure the user never sees raw Python crash tracebacks.
- **Modular & Readable Code**: Divided into clear, single-responsibility functions (`fetch_data`, `display_data`, `main`) designed for easy explanation during technical interviews.

---

## 🔗 API Used

- **Service**: [JSONPlaceholder](https://jsonplaceholder.typicode.com/) (Free fake REST API for testing and prototyping)
- **Base URL**: `https://jsonplaceholder.typicode.com`
- **Endpoints Used**:
  - `GET /users` — Returns a list of 10 mock users with address, contact, and company details.
  - `GET /users/{id}` — Returns a specific user profile by user ID.
  - `GET /posts?userId={id}` — Returns all blog posts written by a specific user.

---

## 📂 Project Structure

```text
simple-api-client/
├── api_client.py        # Core Python script (fetching, error handling, formatting, interactive menu)
├── sample_response.json # Real captured API response from GET /users/1
├── requirements.txt     # Python dependency (requests)
├── README.md            # Complete documentation, output samples, and interview Q&A
└── .gitignore           # Ignores venv, bytecode, IDE files, and temporary artifacts
```

---

## ⚙️ Installation & Setup

### 1. Clone or Navigate to the Project Directory
```bash
git clone https://github.com/hemasrimalla/simple-api-client.git
cd simple-api-client
```

### 2. (Recommended) Create and Activate a Virtual Environment
- **Windows (Command Prompt / PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

Execute the script using Python:

```bash
python api_client.py
```

You will see an interactive menu:
```text
=====================================================================
          SIMPLE REST API CLIENT (JSONPlaceholder Demo)
=====================================================================
  1. List All Users (Table format)
  2. View Single User Details by ID
  3. View Posts by User ID
  4. Test Error Handling (Invalid URL / 404 Simulation)
  5. Test Error Handling (Network Connection Error Simulation)
  6. Exit
=====================================================================
```

---

## 🖥️ Sample Formatted Output

### 1. All Users (Table Layout)
```text
----------------------------------------------------------------------------------------------
ID   | Name                   | Username        | Email                     | City            
----------------------------------------------------------------------------------------------
1    | Leanne Graham          | Bret            | Sincere@april.biz         | Gwenborough     
2    | Ervin Howell           | Antonette       | Shanna@melissa.tv         | Wisokyburgh     
3    | Clementine Bauch       | Samantha        | Nathan@yesenia.net        | McKenziehaven   
4    | Patricia Lebsack       | Karianne        | Julianne.OConner@kory.o   | South Elvis     
5    | Chelsey Dietrich       | Kamren          | Lucio_Hettinger@annie.c   | Roscoeview      
6    | Mrs. Dennis Schulist   | Leopoldo_Cork   | Karley_Dach@jasper.info   | South Christy   
7    | Kurtis Weissnat        | Elwyn.Skiles    | Telly.Hoeger@billy.biz    | Howemouth       
8    | Nicholas Runolfsdott   | Maxime_Nienow   | Sherwood@rosamond.me      | Aliyaview       
9    | Glenna Reichert        | Delphine        | Chaim_McDermott@dana.io   | Bartholomebury  
10   | Clementina DuBuque     | Moriah.Stanto   | Rey.Padberg@karina.biz    | Lebsackbury     
----------------------------------------------------------------------------------------------
Total Users: 10
```

### 2. Single User Details (Profile Card)
```text
=======================================================
 USER PROFILE : LEANNE GRAHAM (ID #1)
=======================================================
 [Basic Information]
  - Username : Bret
  - Email    : Sincere@april.biz
  - Phone    : 1-770-736-8031 x56442
  - Website  : hildegard.org

 [Address Details]
  - Street   : Kulas Light, Apt. 556
  - City     : Gwenborough (Zip: 92998-3874)
  - Geo      : Lat -37.3159, Lng 81.1496

 [Company Details]
  - Company  : Romaguera-Crona
  - Catchphrase: "Multi-layered client-server neural-net"
  - Business : harness real-time e-markets
=======================================================
```

### 3. Posts by User (Clean Card Previews)
```text
------------------------------------------------------------
 POSTS (Showing 5 of 10 posts)
------------------------------------------------------------
 [1] Post ID #1
     Title: Sunt aut facere repellat provident occaecati excepturi optio reprehenderit
     Body : quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molesti...

 [2] Post ID #2
     Title: Qui est esse
     Body : est rerum tempore vitae sequi sint nihil reprehenderit dolor beatae ea dolores neque fu...

 [3] Post ID #3
     Title: Ea molestias quasi exercitationem repellat qui ipsa sit aut
     Body : et iusto sed quo iure voluptatem occaecati omnis eligendi aut ad voluptatem doloribus v...
------------------------------------------------------------
```

---

## 🛡️ Errors Handled

The application incorporates defensive coding to ensure it never crashes with raw tracebacks:

| Error Type / Scenario | Cause | Handled Output Example |
| :--- | :--- | :--- |
| **HTTP 404 Not Found** | Invalid endpoint or requesting user ID that does not exist (`/users/999`) | `[!] Error: Resource not found (HTTP 404). Please verify the requested URL or ID.` |
| **HTTP 500 / 5xx** | Server failure on the remote host | `[!] Error: Internal Server Error (HTTP 500). The remote server encountered an error.` |
| **`requests.exceptions.ConnectionError`** | No internet connection, DNS resolution failure, or unreachable host | `[!] Connection Error: Could not connect to the server. Please check your network connection or DNS settings.` |
| **`requests.exceptions.Timeout`** | Remote server takes longer than specified timeout (e.g. 10s) | `[!] Timeout Error: The request took longer than 10 seconds to respond.` |
| **`requests.exceptions.RequestException`** | General fallback for any unexpected network or protocol error | `[!] Network / Request Error: An unexpected request error occurred: ...` |
| **`ValueError` / `JSONDecodeError`** | Remote endpoint returned non-JSON data (e.g. HTML error page) | `[!] JSON Parsing Error: Failed to decode response as JSON: ...` |
| **Invalid User Input** | Entering text (`abc`) or negative numbers (`-5`) when a number is requested | `[!] Invalid input 'abc'. Please enter a valid number (e.g., 1, 2, 5).` |
| **Interruption (`Ctrl+C` / EOF)** | User terminates execution in terminal | `[!] Program interrupted by user. Exiting gracefully. Goodbye!` |

---

## 💡 Interview Questions & Answers

### 1. What is a REST API?
> **Answer**:  
> **REST** stands for **Representational State Transfer**. It is an architectural style for designing networked applications that communicate over HTTP using standard web protocols.  
> Key characteristics include:
> - **Statelessness**: Every request from client to server must contain all the information necessary to understand and process the request; the server stores no client session context.
> - **Resource-Oriented**: Data entities (like users, posts, or orders) are modeled as resources identified by unique Uniform Resource Identifiers (URIs).
> - **Standard HTTP Methods**: Operations on resources map directly to HTTP verbs (`GET` to read, `POST` to create, `PUT`/`PATCH` to update, and `DELETE` to remove).
> - **Standard Representation**: Data is commonly exchanged in lightweight formats like **JSON** or XML.

---

### 2. What is HTTP status code 200?
> **Answer**:  
> **HTTP 200 OK** is the standard success status response code indicating that the client's HTTP request has succeeded.  
> - For a `GET` request, 200 OK means the resource was located on the server and returned in the response body.
> - For a `POST` or `PUT` request, it signifies that the server successfully processed the action and returned the resulting resource or confirmation.

---

### 3. What is JSON and why is it preferred in REST APIs?
> **Answer**:  
> **JSON** stands for **JavaScript Object Notation**. It is a lightweight, text-based data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.  
> - It is language-independent and maps directly to native data structures across programming languages (e.g., Python `dict` and `list`, JavaScript objects and arrays).
> - It is preferred over XML because it has less overhead, smaller payload sizes, and faster serialization/deserialization speeds.

---

### 4. What is the difference between GET and POST?
> **Answer**:  
> | Feature | `GET` | `POST` |
> | :--- | :--- | :--- |
> | **Primary Purpose** | Retrieve/read existing data from a server | Submit new data to a server to create a resource |
> | **Request Payload (Body)** | Does not typically include a body; parameters are sent via URL query string | Includes data in the HTTP request body (e.g., JSON payload) |
> | **Idempotency** | **Idempotent**: Calling GET multiple times produces the same result without side effects | **Non-Idempotent**: Calling POST multiple times creates multiple duplicate resources |
> | **Caching & Bookmarks** | Responses can be cached by browsers/proxies; URLs can be bookmarked | Never cached by default; cannot be bookmarked |
> | **Security / Visibility** | Parameters are visible in the URL bar and server logs (not safe for passwords/tokens) | Data is encapsulated in the request body (more secure for sensitive inputs over HTTPS) |

---

### 5. Why is setting a `timeout` in `requests.get()` critical in production?
> **Answer**:  
> By default, `requests.get()` will wait indefinitely if the remote server accepts the connection but never sends data back. In production systems or microservices, this can tie up threads and worker processes, leading to thread exhaustion, severe memory leaks, and cascading downtime. Specifying `timeout=(connect_timeout, read_timeout)` ensures the program fails fast and recovers cleanly.

---

## 🛠️ Git Setup & Repository Push Instructions

To initialize this project as a local Git repository and push it to your GitHub account:

```bash
# 1. Initialize local git repository
git init

# 2. Add all files to staging (respecting .gitignore)
git add .

# 3. Create initial commit
git commit -m "feat: complete simple-api-client with error handling and documentation"

# 4. Set the default branch to main
git branch -M main

# 5. Link local repository to your GitHub remote repository
git remote add origin https://github.com/hemasrimalla/simple-api-client.git

# 6. Push to GitHub
git push -u origin main
```

---

## 👤 Author
- **Hemasri Malla**  
- GitHub: [@hemasrimalla](https://github.com/hemasrimalla)
