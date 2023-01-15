"""
1. Follow other users
2. Post images to feed
3. View a feed of images

----------

1. Concept of a user
2. Concept of unidirectional following
    - Following a user doesn't mean they need to follow back
3. Adding an image that is associated to your account
4. Seeing the images posted by all the people you follow in a timeline fashion

----------

- 10 millions active users per month
- High traffic burst?
- Limit of uploads per day?
- Average uploads = 2 per month
- Average pic size = 5 MB
- 5 MB * 10 000 000 * 2 = 100 000 000 MB = 100 TB per month
- 1 PB per year

Data Models
-----------

User
    - id
    - name
    - email
    - location

Follow
    - from_user
    - to_user

Media
    - id
    - user_id
    - caption
    - location
    - timestamp
    - uri

----------

Notes:
    - Mobile application

Distribute the app across mobile app stores:
    - Apple store
    - Google store
    - Windows store

Compression:
    - 5 MB -> 50 KB
    - 1 PB -> 10 TB per year
    - Reduction 100x

Load balancer
    - Redirect traffic to one of the available servers
    - Base decision on the server's current workload + latency estimations
    - Use the geolocation of the user to pick which data center to query

Server
    - Stateless - Allows us to scale horizontally

Database (SQL)
    - Master Slave - Lots of reads, few writes
    - Fetch meta data from the database

CDN (Cloudflare)
    - Cache the images to speed up feed view times

File store (S3)
    - Store documents

Advertisement service:
    - Based on telemetry data, makes suggestions on the posts to show to the user
    - Telemetry data is stored in separate database specific for user engagements

Follower suggestions service:
    - Based on telemetry data, makes suggestions on the users to show to the user
    - Telemetry data is stored in separate database specific for user engagements
"""
