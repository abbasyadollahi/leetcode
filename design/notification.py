"""
A notification system has already become a very popular
feature for many applications in recent years. A notification
alerts a user with important information like breaking news,
product updates, events, offerings, etc. It has become an
indispensable part of our daily life. In this chapter, you are
asked to design a notification system.

A notification is more than just mobile push notification.
Three types of notification formats are: mobile push
notification, SMS message, and Email. Figure 10-1 shows an
example of each of these notifications.

Functional requirements
-----------------------

Supports:
- mobile push notifications
- sms
- email

As a user:
  - subscribe to an event and be notified when it happens

How are notifications triggered?
Events get sent to a message queue (e.g. kafka), which gets sent to all subscribers (subscribers consume from the message queue, and publish to users)

https://en.wikipedia.org/wiki/Push_technology#Long_polling
https://systeminterview.com/scale-from-zero-to-millions-of-users.php

Non-functional requirements
---------------------------

API
---

Data model
----------

High level design of components
-------------------------------

Low level design of components
------------------------------
"""
