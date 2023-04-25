# HelloGirls
A program to send good morning and good night dm's to multiple Instagram accounts

> **Status:** Testing Phase (ready for use)

> Forgive me for any errors. I Developed this on a tablet, with no debugging or code prediction

**Developed with 💙 by ImSoDrowned**

Idea by **Abishek RS** 🧠

Dedicated to **Sai Krishanan**
# Introduction
![Console Screenshot](https://github.com/ImSoDrowned/HelloGirls/blob/main/screenshot.jpg)

Do you have multiple girlfriends?

Do you find it difficult to send a good morning and a good night to her every day?

No need to worry about this anymore because **HelloGirls** is here to protect your relationship(s)!

**HelloGirls** allows you to 
- Send Instagram dm's to as many accounts as you prefer 
- Schedule your messages to be sent at a given time 
- Send greetings to up to 100 accounts
    - > Although sending messages to this many accounts at once can get your account banned
# WARNING
I made a duplicate account for testing this code but that account just got banned
![suspended account](https://github.com/ImSoDrowned/HelloGirls/blob/main/Warning.jpg)
So... use it with care 😅

# Installation
` pip install -r requirements.txt `
```json
{
    "instagram_settings": {
        "username": "enter-your-username",
        "password": "enter-your-password"
    },
    "message_settings": {
    	"morning": {
    		"message": "Good Morning", <===Your morning greeting
    		"hour": 8,                 <=== The hour and minute the greeting should go
    		"minute": 0
    	},
    	"night": {
    		"message": "Good Night", <=== Your night greeting
    		"hour": 21,              <=== The hour and minute the greeting should go
    		"minute": 0
    	}
    }
}

```

## Inputing Recipient's Instagram IDs

* Open ` usernames.txt `
* Then add the Instagram IDs

example
```
ganeshpaniker
namanbig
chorian2024
```
**DO NOT LEAVE EMPTY LINES BETWEEN OR AFTER THE USERNAMES**

## Still Confused?
**Contact me on [Removed]()**
