# 👻 GhostAlert

> **Catch Ghost Pingers in 4K.**

GhostAlert is a lightweight Discord moderation bot that detects **ghost pings**—messages that mention users, roles, `@everyone`, or `@here` and are deleted immediately afterward.

It instantly alerts victims, notifies moderators, and logs every incident, making it nearly impossible for ghost pingers to go unnoticed.

---

# 📖 Background

GhostAlert was born out of frustration.

Like many Discord users, I got tired of people constantly ghost pinging others just to annoy them. Existing bots either lacked the features I wanted or weren't as configurable as I'd hoped.

So I decided to build my own.

The goal was simple:

> **If someone ghost pings, everyone who needs to know should know, even if moderators are abusing their power.**

GhostAlert focuses on doing one thing well—detecting ghost pings quickly and reliably while remaining lightweight and easy to configure.

---

# ✨ Features

- 👤 Detects deleted user mentions
- 👥 Detects deleted role mentions
- 🌍 Detects deleted `@everyone` and `@here`
- 📩 Sends private alerts to victims (optional)
- 🚨 Sends staff DM alerts for role and global ghost pings
- 📜 Logs ghost pings to a configurable log channel
- ⚡ Fast and lightweight
- 💾 SQLite database (no external database required)
- 🎨 Clean Discord embeds
- 🔧 Slash command configuration

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/abrar2011/GhostAlert---The-Ultimate-Anti-Ghost-Ping-Bot-For-Discord.git
cd GhostAlert---The-Ultimate-Anti-Ghost-Ping-Bot-For-Discord
```

---

## 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Create a Discord Bot

Go to the Discord Developer Portal:

https://discord.com/developers/applications

Create a new application, create a bot, and copy its token.

---

## 4. Create a `.env` file

Create a file named:

```
.env
```

Inside it, put:

```env
TOKEN=YOUR_DISCORD_BOT_TOKEN
```

---

## 5. Invite the bot

When inviting the bot, enable:

- View Channels
- Read Message History
- Send Messages
- Embed Links
- Use Slash Commands
- Send Direct Messages

---

## 6. Start the bot

```bash
python bot.py
```

If everything is configured correctly, you should see:

```
Logged in as YOUR_BOT_NAME
Synced X commands.
```

---

# ⚙️ Commands

## User Commands

| Command | Description |
|---------|-------------|
| `/enable-dm-alert` | Enable personal ghost ping alerts |
| `/disable-dm-alert` | Disable personal ghost ping alerts |

---

## Administrator Commands

| Command | Description |
|---------|-------------|
| `/set-log-channel` | Sets the server log channel |
| `/add-dm-log-recipient` | Adds a moderator to receive staff DM alerts |
| `/remove-dm-log-recipient` | Removes a moderator from staff alerts |
| `/list-dm-log-recipients` | Lists all current staff alert recipients |

---

# 🚨 How it works

## User Ghost Ping

```
@User Hello!
```

Message gets deleted.

✅ Victim receives a private DM.

✅ Log channel receives a log.

---

## Role Ghost Ping

```
@Students Get Ponged!
```

Message gets deleted.

✅ Staff receives a DM.

✅ Log channel receives a log.

---

## Everyone / Here Ghost Ping

```
@everyone Get Ponged!
```

Message gets deleted.

✅ Staff receives a DM.

✅ Log channel receives a log.

---

# 🤝 Contributing

Contributions, bug reports, and feature suggestions are always welcome.

If you find a bug or have an idea for improving GhostAlert, feel free to open an Issue or submit a Pull Request.
Contatct me [Through Discord](https://discordapp.com/users/1401569296240480311)

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!

It helps others discover GhostAlert and motivates further development.

---

**GhostAlert**

*Catch Ghost Pingers in 4K.*