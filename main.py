import discord
import os
import requests
import re
import asyncio

from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

reminders = {}
reminder_id_counter = 0

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

client = discord.Client(intents=intents)


def get_gemini_response(user_message):
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api_key}"

    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": user_message}]}]}
    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    if 'candidates' in result and result['candidates']:
        return result['candidates'][0]['content']['parts'][0]['text']
    else:
        return "Sorry, I couldn't process that."


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

async def create_reminder(message):
    global reminder_id_counter
    reminder_regex = re.compile(r'\$remind "(.*?)" "(\d{4}-\d{2}-\d{2} \d{2}:\d{2})"')
    match = reminder_regex.match(message.content)

    if not match:
        await message.channel.send('Invalid format! Use: `$remind "Reminder text" "YYYY-MM-DD HH:MM"`')
        return

    text = match.group(1)
    time_str = match.group(2)

    try:
        reminder_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        if reminder_time < datetime.now():
            await message.channel.send("Time must be in the future!")
            return

        # Add reminder to user's list
        user_reminders = reminders.get(message.author.id, [])
        reminder_id_counter += 1
        user_reminders.append((reminder_id_counter, text, reminder_time))
        reminders[message.author.id] = user_reminders

        await message.channel.send(f"Reminder set! ID: {reminder_id_counter} — '{text}' at {time_str}")
    except ValueError:
        await message.channel.send("Invalid time format! Use: YYYY-MM-DD HH:MM")


async def create_poll(message):
    poll_regex = re.compile(r'\$poll "(.*?)"(?: "(.*?)")+')
    match = poll_regex.match(message.content)

    if not match:
        await message.channel.send('Invalid format! Use: `$poll "Question" "Option 1" "Option 2" ...`')
        return

    question = match.group(1)
    options = re.findall(r'"(.*?)"', message.content)[1:]

    if len(options) < 2 or len(options) > 10:
        await message.channel.send('Please provide between 2 and 10 options.')
        return

    poll_message = f"📊 **{question}**\n\n"
    emoji_numbers = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

    for i, option in enumerate(options):
        poll_message += f"{emoji_numbers[i]} {option}\n"

    poll = await message.channel.send(poll_message)

    for i in range(len(options)):
        await poll.add_reaction(emoji_numbers[i])


async def check_reminders():
while True:
    now = datetime.now()
    for user_id, user_reminders in reminders.items():
        for reminder in user_reminders[:]:
            reminder_id, text, reminder_time = reminder
            if now >= reminder_time:
                user = client.get_user(user_id)
                if user:
                    await user.send(f"⏰ Reminder: {text}")
                user_reminders.remove(reminder)
    await asyncio.sleep(60) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"Message from {message.author}: {message.content}")

    user_message = message.content

    if user_message.startswith('$remind'):
        await create_reminder(message)
        return

    if user_message.startswith('$poll'):
        await create_poll(message)
        return

    response = get_gemini_response(user_message)
    await message.channel.send(response)


@client.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.text_channels, name="welcome")

    if welcome_channel:
        await welcome_channel.send(f"🎉 Welcome to the server, {member.mention}!")
    else:
        print("No 'welcome' channel found. Please create a text channel named 'welcome'.")


client.run(os.getenv('TOKEN'))
