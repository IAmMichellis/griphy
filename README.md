# griphy


Discord bot for slack-giphy-style giphy integration.

Notes to self:
Used this tutorial: https://www.maxongzb.com/serving-gifs-with-discord-bot-reading-time-12-mins/

# secrets

Make `secrets.py` project directory with the following contents:

```
discord_bot_token = '<your-discord-bot-token>'
giphy_app_token = '<your-giphy-api-token>'

# virtualenv

Setup:
```
virtualenv --python=python3 venv
python3 -m pip install -U discord.py
```
Use:
```
source venv/bin/activate
python griphy.py
deactivate
```
