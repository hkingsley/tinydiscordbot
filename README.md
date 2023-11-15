
# tinydiscordbot

## Description

Welcome to `tinydiscordbot`, a minimal yet powerful Discord bot designed for easy customization and extension to help as a starting point for Discord bot projects. Built using Python and the discord.py library, this bot is built to provide a quick and efficient experience for Discord server management, automation, and interaction.

## Requirements

Ensure you have the following:
- Python 3.7 or higher
- Discord account and a bot token ([Discord Developer Portal](https://discord.com/developers/applications))

Dependencies are listed in the `requirements.txt` file and can be installed using pip.

## Installation

1. Clone this repository or download the zip file and extract it.
2. Navigate to the bot's directory in your terminal.
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

To configure the bot:
1. Navigate to the `config` directory.
2. Edit the configuration files to include your bot token and any other necessary settings. Follow the template provided in the configuration files for guidance. Currently setup to look for a environment variable called BOT_TOKEN
3. For scheduled tasks and messages you will also need to ensure you have a environment variable called DISCORD_CHANNEL_ID set up so it send to the correct channel

## Usage

To run the bot:
1. Ensure you have completed the configuration steps.
2. Run `main.py`:
   ```
   python main.py
   ```
3. The bot should now be running and responsive to commands in your Discord server.

## Cogs

The `cogs` directory contains modular components that add functionality to the bot. You can create new cogs or edit existing ones to customize the bot's behavior.

## Contributing

Contributions to `tinydiscordbot` are welcome! Please feel free to fork this repository, make your changes, and submit a pull request.


