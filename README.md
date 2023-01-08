# HelloGirls
A program to send good morning and good night dm's to multiple Instagram accounts

> **Status:** Testing Phase

**Developed with 💙 by ImSoDrowned**
# Introduction
Do you have multiple girlfriends?

Do you find it difficult to send a good morning and a good night to her every day?

No need to worry about this anymore because **HelloGirls** is here to protect your relationship(s)!

**HelloGirls** allows you to 
- Send Instagram dm's to as many accounts as you prefer 
- Schedule your messages to be sent at a given time 
- Send greetings to up to 100 accounts
    - > Although sending messages to this many accounts at once can get your account banned
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
