# 
This project implements a simple chatbot using Python, which interacts with users via WhatsApp Web. The bot, named "Tridib," can perform various tasks, such as responding to greetings, providing information, and fetching news. Here’s a detailed explanation of the project's components and functionality:

## Project Overview
The Tridib Chatbot leverages libraries such as pyautogui for automating keyboard and mouse actions, requests and BeautifulSoup for web scraping, and wikipedia for fetching information. It is designed to respond to specific user queries and provide a conversational experience.

## Key Components
#### 1.Libraries Used:

* pyautogui: Automates mouse and keyboard actions to interact with the WhatsApp Web interface.
* webbrowser: Opens WhatsApp Web in a browser.
* requests & BeautifulSoup: Used for web scraping, specifically for fetching news from an RSS feed.
* wikipedia: Retrieves summaries from Wikipedia based on user queries.
* tkinter: Accesses the clipboard to get the latest message from WhatsApp.
* pyttsx3: Provides text-to-speech functionality, allowing the bot to "speak" responses.
#### 2.Core Functionality:

* Opening WhatsApp Web: The bot opens the WhatsApp Web interface and waits for the user to interact.
* Reading Messages: It continuously reads messages from the user by copying them to the clipboard.
* Responding to Queries: Based on the content of the messages, the bot has predefined responses for various keywords (e.g., greetings, inquiries about its name or age, news requests).
* Web Scraping for News: When the user asks for news, the bot fetches the latest headlines from Google News using RSS feeds.
* Information Retrieval: The bot can summarize topics from Wikipedia when asked.
* Randomized Responses: To make the conversation feel more natural, the bot uses random responses for certain repeated queries.
#### 3.State Management:

The bot uses counters to keep track of how many times certain questions have been asked (like "how are you?" or "sorry") to manage its responses dynamically and avoid redundancy.
## Example Interactions
* Greeting: If the user says "hello" or "hi," the bot responds with a time-appropriate greeting (morning, afternoon, evening).
* Information Request: If the user types "tell me about [topic]," the bot fetches a summary from Wikipedia and replies with the information.
* News Fetching: When the user requests news, the bot scrapes the latest headlines from Google News and shares them.
## Error Handling
The bot is designed to handle exceptions gracefully. If an error occurs (e.g., due to the clipboard being empty or issues with network requests), it prints the error message and continues running.




