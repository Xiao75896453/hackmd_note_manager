# hackmd_note_manager

Frontend of PyCon TW official website.

## Set up a Development Environment

### Requirements

- Python >= 3.8.5

> You can refer to `pyproject.toml` file for more details.

### Method 1: `Develop on your local machine`

1. Clone this repository.

2. Make folder ```log``` and ```output```.

3. Make file ```.env``` and add Environment Variables to configure this project:
    ```
    TEAM_PATH=pycontw
    TOKEN={{your hackmd token}}
    HACKMD_API_URL=https://api.hackmd.io/v1/
    ```
4. Install poetry

5. Enter to env

    ```bash
    poetry shell
    ```

6. Install dependencies:

    ```bash
    poetry install
    ```
7. Execute 

    ```bash
    python app.py
    ```


## SOURCE
https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fteam-notes-api# hackmd_note_manager
# hackmd_note_manager
