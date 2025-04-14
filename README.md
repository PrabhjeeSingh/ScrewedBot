# ScrewedBot

A Discord bot developed in Python, integrating an Email API for in‑chat email display and leveraging the Cogs library for dynamic module management, enabling real‑time code modifications while operational.

## Features

- **Dynamic Module Management**: Uses Discord.py Cogs for modular command organization
- **Moderation Tools**: Kick, ban, and unban functionality
- **Utility Commands**: 
  - Message clearing
  - 8ball fortune telling
  - Latency checking
  - User information
  - Server statistics
  - Role management
  - Poll creation
  - Reminder system
- **Email Integration**:
  - In-chat email display
  - Email notifications
  - Email templates
  - Email scheduling
- **Custom Prefix Support**: Per-server prefix configuration
- **Error Handling**: Custom error messages and command validation
- **Status Cycling**: Dynamic status updates

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ScrewedBot.git
cd ScrewedBot
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `config.json` file with your Discord bot token and email configuration:
```json
{
    "token": "your_bot_token_here",
    "email": {
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "email_address": "your_email@example.com",
        "email_password": "your_email_password"
    }
}
```

## Configuration

The bot uses a `prefix.json` file to store server-specific command prefixes. The default prefix is `#`.

## Usage

### Basic Commands
- `#hello` - Greets the user
- `#ps` - Shows bot latency
- `#8ball <question>` - Ask the magic 8ball a question
- `#clear <amount>` - Clear messages (default: 5)
- `#kick <member> [reason]` - Kick a member
- `#ban <member> [reason]` - Ban a member
- `#unban <member#discriminator>` - Unban a member
- `#userinfo [@member]` - Display information about a user
- `#serverinfo` - Display information about the server
- `#avatar [@member]` - Show a user's avatar
- `#poll <question> | <option1> | <option2> [| <option3> ...]` - Create a poll
- `#remind <time> <message>` - Set a reminder (e.g., #remind 1h do homework)
- `#role add <@member> <role>` - Add a role to a member
- `#role remove <@member> <role>` - Remove a role from a member
- `#roles` - List all available roles
- `#mute <@member> [time] [reason]` - Mute a member
- `#unmute <@member>` - Unmute a member
- `#warn <@member> [reason]` - Warn a member
- `#warnings <@member>` - Check warnings for a member
- `#translate <text> [target_language]` - Translate text (default: English)
- `#weather <location>` - Get weather information
- `#timer <time>` - Set a countdown timer
- `#quote` - Get a random quote
- `#joke` - Get a random joke
- `#roll <dice>` - Roll dice (e.g., #roll 2d6)
- `#flip` - Flip a coin
- `#help [command]` - Show help for commands

### Email Commands
- `#email setup` - Configure email settings for the server
- `#email send <recipient> <subject> <message>` - Send an email
- `#email template list` - List available email templates
- `#email template create <name> <content>` - Create a new email template
- `#email schedule <time> <recipient> <subject> <message>` - Schedule an email
- `#email inbox` - View recent emails in the configured inbox
- `#email search <query>` - Search through emails
- `#email notify on/off` - Toggle email notifications for the channel

### Module Management
- `#load <extension>` - Load a cog
- `#unload <extension>` - Unload a cog
- `#reload <extension>` - Reload a cog

## Available Cogs
- `basic.py` - Basic utility commands
- `exam.py` - Examination-related commands
- `test.py` - Testing functionality
- `email.py` - Email integration and management
- `moderation.py` - Moderation commands
- `fun.py` - Fun and entertainment commands
- `utility.py` - Utility and information commands

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.