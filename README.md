## Installation

1. Clone the repository.

2. Create a virtual environment and activate it.

3. Install project dependencies: `pip install -r requirements.txt`

4. Run migrations: `python manage.py migrate`

5. Start the development server: `python manage.py runserver`

API Documentation:
Provide detailed documentation for each API endpoint, including usage examples and explanations. You can structure this section with headings for each endpoint.



## API Endpoints

### Custom API (GET)

- **URL:** `/api`
- **Method:** GET
- **Parameters:**
  - `slack_name` (Query Parameter): Slack name of the user.
  - `track` (Query Parameter): Track information.
- **Description:** This endpoint returns information based on query parameters.
- **Example Request:**
GET /api?slack_name=olatunde&track=backend

**Example Response:**
```json
{
  "slack_name": "olatunde",
  "current_day": "Saturday",
  "utc_time": "12:34:56Z",
  "track": "backend",
  "github_file_url": "https://github.com/olatunde2/TASK1-/tree/main/tasks1",
  "github_repo_url": "https://github.com/olatunde/task1.git",
  "status_code": 200
  
}


Custom API (POST)

URL: /api

Method: POST

Description: This endpoint allows you to create a new resource.

Request Body:

  "slack_name": "new_user",
  "current_day": "Sunday",
  "utc_time": "13:45:00Z",
  "track": "frontend",
  "github_file_url": "https://github.com/new_user/tasks",
  "github_repo_url": "https://github.com/new_user/task-repo.git",
  "status_code": 201
}
Example Response:

  "slack_name": "new_user",
  "current_day": "Sunday",
  "utc_time": "13:45:00Z",
  "track": "frontend",
  "github_file_url": "https://github.com/new_user/tasks",
  "github_repo_url": "https://github.com/new_user/task-repo.git",
  "status_code": 201
}
}```






