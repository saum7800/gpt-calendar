# gpt-calendar


Before sleeping every night, I like to write down what I plan to do the next day. Meal planning, school work, workout, a reminder for something, etc. Just a paragraph of stuff. Then I do some of it, forget some of it, and look back directly the next night. It would be helpful if whatever I wrote was on my calendar. I dont enjoy making each event or reminder on google calendar. With this repo, gpt-4 will (hopefully) do it for me.

The plan is as follows:
1. Use GPT-4 function calling to extract event, event details, and reminders from a paragraph of text. Probably use langchain to make this easier.
2. Use the google calendar API to add the extracted events to my calendar.
3. Wrap this in an API
4. See how whatsapp chatbots work and whether I can have that ping my API.

Uncertainties:
1. How would time and timezones work? Don't know if GPT handles time well. I will have to assume events are just for the next day for now. Fixing timezone for myself too, will see if there is a default user timezone available in google's calendar api.
2. How would auth work if someone starts the flow from whatsapp? will need to understand auth process, ideally I get a link I can send back to the user.
3. How do I confirm whether the events being added are right? Can send the user on whatsapp a summary of the changes being made, but the user would have to do either a complete accept or a complete reject. Let's see, could force the user to confirm each event, but that would be annoying.

Lets go.