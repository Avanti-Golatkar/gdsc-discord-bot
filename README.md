# gdsc-discord-bot
discord bot for gdsc 

Link to join the Server:
https://discord.gg/49yTxFBx

Features of the bot:
1) Responses to server messages using Gemini API
2) Welcomes new user by sending custom welcome message
3) Creates Polls
4) Summarizes long paragraphs
5) Sets reminders

Process:
1) I started off by creating a discord server to add the bot to, by clicking on add a server and gave it a name.
2) Then I created a discord bot account on the discord developer portal (link attached below). On the portal I created a new bot by clicking on new application and giving the bot a name.
https://discord.com/developers/applications
3) Did a little research (watched tutorials and googled a few things) to learn how code a bot on python, what libraries to use, and the their functionality.
4) Wrote a basic code as a 'base code' which only prints “Hello!” when the user writes a sentence starting with "$hello" using a simple logic (only used the discord library for this).
5) Next I wanted to integrate Gemini API in my code, I created a Gemini API key on Google AI Studio and then stored the key in a .env file to keep it secure.
6) Modified my base code to integrate AI response in it 


Usage:
1)Chat with AI:
<your message>

2)Create a poll:
<$poll "Question?" "Option 1" "Option 2">

3)Set reminders:
<$remind "Reminder" "YYYY-MM-DD HH:MM"
