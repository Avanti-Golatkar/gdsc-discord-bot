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
6) Modified my base code to integrate AI response in it.
7) After integrating Gemini API, I updated the bot's logic so that if a user sends a message that doesn’t match any predefined features, it forwards the message to the Gemini AI and sends it's response back to the user.
8) Then I added the reminder feature (using the re library) to capture the reminder text and time in a specific format. I thhen made a dictionary to store reminders by users and added a loop (check_reminders) to check every minute if any reminders were due.
9) To implement the polling feature I again used RegEx so that when a user sends a command in a specific format, the bot creates polls and posts it in the chat.
10) Then I created a welcome channel and made a on_member_join functon which sends a custom text on the channel welcoming every new user.



Usage:

1)Chat with AI:
your message

2)Create a poll:
<$poll "Question?" "Option 1" "Option 2">

3)Set reminders:
<$remind "Reminder" "YYYY-MM-DD HH:MM"




Code Breakdown:



1)Imported libraries:

Discord: Core library to interact with discords API.

OS:originally intended to store the bot token, but that step was later replaced by using a .env file for better security, I forgot to delete it later.

Requests: To communicate with gemini API, call it by making HTTP requests.

Re: For regular expressions to set reminders and poll.

Asyncio: Enables bot to handle multiple tasks.

Datetime:To manage reminders.

Dotenv: To import the env files to access tokens



2)Gemini API integration:

Defines a function which takes the user's text as an argument and sends the user’s message to the Gemini AI API using a POST request to get a text response.
If the AI is not able to send a valid response it returns a “Sorry! I couldn't process that.” message.



3)On-Ready Function:

Runs when the bot logs in and returns a confirmation message.



4)Create_Reminder Function:

Uses regular expressions to match the format of the user's text and adds the reminder to the user’s list. If the format is wrong it sends an error message.
Format: 
<$remind "Reminder" "YYYY-MM-DD HH:MM"



5)Check_Reminders Function:

Runs in a loop to check the reminders every minute. If the reminders time has passed it informs the user and deletes the reminder.


6)Create_Poll Function:

Uses regular expressions to match the format of the user's text .Then the function slices list to skip the first element (question) leaving only the options. Ensures the poll has at least 2 options and then iterates through the options and adds each one, paired with the corresponding emoji and sends the poll.If the user's message doesn’t match the regex the bot sends an error message explaining the correct format.
Format:
<$poll "Question?" "Option 1" "Option 2".....>



7)On-Message Function:

It ignores the messages sent by the bot itself. Checks whether the commands match the 2 features ($remind or $poll) and triggers the reminder or poll creation. If it doesn't match, the message is sent to Gemini AI and returns the AI’s response. 



8)On-Member-Join Function:

Prints a custom welcome message in the welcome channel whenever a new user joins the server. 



If I was given more time I would have enhanced the AI integration by allowing more dynamic conversations with Gemini, like multi-turn dialogues. I would have researched about and tried to integrate music. The reminder system could be upgraded with options to view, edit, and cancel reminders easily. The error handling could have been improved. 


