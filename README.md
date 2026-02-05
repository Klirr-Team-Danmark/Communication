# Communications

**Important note:** This repo has been modified after handing it in for the hackathon. [This commit is from 14:36 that day](https://github.com/Klirr-Team-Danmark/Communication/tree/24adf1c730c28024f020f57c7cc802b5e9da6d66), and [this one from 15:16](https://github.com/Klirr-Team-Danmark/Communication/tree/fd816e34bc917235c5d5af5b905b14771053e934).

A **prototype** for a communications page for a community, which for now is focusing on:

- A decision log - Where signed in users can post decisions and everyone can read them.
- A chatroom - Where everyone can communicate with each other.

# Usage

1. Create a python virtual env:
```sh
python -m venv venv
```
2. Activate it:
```sh
. venv/bin/activate  # Assuming bash
```
3. Install the dependencies:
```sh
pip install -r code/requirements.txt
```
4. Run the migrations
```sh
code/manage.py migrate
```
5. Start the server
```sh
code/manage.py runserver
```
6. Access it from a browser on localhost:8000 (its default port)

# TODO

Many things, but these are a few:

- Use e.g. `gunicorn`/`uwsgi` instead of django's runserver, which is only for development purposes
- Internationalisation
- UI and UX improvements

## Chat

- Messaging
- Implement it so new decision logs are announced in the chat
- Ability to create accounts that reserves a chat name?

# Dependencies

- Python
- Django
- sqlite
- htmx (already included)
- PicoCSS (already included)
