## Setup

I set this project up to run on the AWS Academy server, I had to download and update several packages in order for the project to run.

1. `sudo apt update`
2. `sudo apt install python3.8`
3. `python3.8 -m pip install --upgrade pip`
4. `python3.8 -m pip install -U discord.py==2.0.1`
5. `pip3 install -U python-dotenv`

As you set up your bot in the discord developer portal, make sure to give to give it message intent permissions in the 'Bot' tab. This is also where you will find the authorization token. Copy this token into a `.env` file. Once you do this, it is very important to ensure your .env file does not ever get uploaded to your remote repo.

## Usage

This bot completes quotes from Psych. Shawn has told Gus not to be many things

by typing "Gus, don't be" the bot will complete the quote with one of many exmples.

![alt text](https://github.com/WSU-kduncan/ceg3120-C1WP/blob/main/Discord-Bot/quotes.png "quotes")

## Research