"""
Analyze list of words from a text file and return all palindromes.

App:
    - Web page
    - Text file
    - One word per line
    - Get all palindromes in the text
    - Return a new text file

Use case:
    1. User presses button to upload a text
    2. Check for palindromes line by line
    3. Return a text file with all the non palindrome stripped out

Notes:
    - Thousands of words
    - Could have invalid inputs
    - Always accept text files only
    - Light traffic (internal application)

Design
------

Client browser
    - Uploads text file to filestore if request was accepted given metadata about file

Api server
    - Accepts palindrome file requests
    - Reject f not a text file
    - Strip out invalid lines and logs them for the user
    - Rejects - Not possible with error messages
    - Accepts - The file is being processed in background will notify when job is completed

MQ service
    - Accepts jobs sent by the api server
    - Palindrome service listens to this queue waiting for events

Palindrome service
    - Fetch metadata about unprocessed file from the DB and fetch file from filestore
    - Line by line find all the palindromes and strip out non palidnromes
    - Log any invalid lines while doing so
    - After finishing to process the file -> Upload to filestore and record metadata about processed file in DB

Filestore (S3)
    - Stores unprocessed/processed palindrome text files

Database (SQL)
    - Stores metadata about file paths on filestore, timestamps, sizes, etc

Email service
    - Sends email to the user with links to the processed file and error log in the filestore
"""
