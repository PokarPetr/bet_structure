Odds Parsing Application
This project is an asynchronous application designed for parsing sports betting odds from multiple sources, processing the data, and sending it to a remote server or WebSocket.

How it Works
main.py: Orchestrates the execution of asynchronous tasks, managing the intervals for live and pre-match data parsing.
app.py: Contains the core logic for running parsing tasks, processing the data, and sending it to a remote server or WebSocket.
Parsers: Located in /parsers, these modules handle the specific parsing logic for pre-match and live odds.
Utilities: Utility scripts in /utils manage logging, data sending, and server connections.

Adjust settings in config/settings.py to configure update intervals and server connections.

Future Expansion
This project is designed to be extensible, allowing for the addition of new parsers or processing logic by adding new modules in the /parsers and /utils directories.