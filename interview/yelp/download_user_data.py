"""
Design a feature that allows Yelp users to download all their data (posts, review, photos, videos, etc.)

Use cases:
    - User presses a button, downloads all their data in a single archive file.

Problems:
    - Size of the archive
    - Scalability (look at a single useer for now)

Notes:
    - Only on webpage

Step by step
------------

1. User presses button
2. Sends a request to the server
3. Server accepts or rejects requests
4. Respond to the user that job's been accepted
    - Will receive an email with a downloadable link to the user data
5. Archiving service works on jobs asynchronously
6. Return downloadbable link when archive is ready

Design
------

Web Server
    - Button client interacts with

Api Server

Database (SQL)
    - Stores structural information (posts, reviews, comments, etc)
    - Metadata information about image blobs (paths, versions)
    - Store regional information depending on user location
    - Master - Slave heavier

Filestore (GCS)
    - Stores image blobs

Archiving server
    - Archives user data
    - Requirs high hardware resources
    - Spins up whenever a lot of jobs are available in the queue
    - Metadata information about archives (paths, versions, timestamps)
    - Stores archives on a accessible file system

CDN (CloudFlare)
    - Cache static assets like images
    - Long lived assets that don't expire

MQ service (Kafka)
    - Waits for jobs to be sent from the api server
    - Archiving server listens to this topic

Email service
    - Sends emails to the users about any new notifications
"""
