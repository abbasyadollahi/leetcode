# Twitter

## Assumptions

- Start small and simple (1k users). Scale later.
- Contains both famous and normal users.

## Focus

- Backend structure, APIs, clients, data schemas.
- Frontend logic is done (web/mobile apps, UI, UX).
- User logic is done (registration flow, login, authentication, user table).

## Workflows:

- Post a tweet.
- View a tweet.
- Follow/unfollow.
- View a user's timeline (own or somebody else's). No smarts - chronological order.
- View home timeline (merge timelines of all people you follow). No smarts - chronological order.

---

## Backend

- API gateway
- Stateless service
- Relational database

## APIs

Protocol: REST

Other options: gRPC, protobufs

### PostTweet

- Method: POST
- Path: `/tweet/create`
- Body: {
    content: str,
    username: str,
    creation_time: timestamp,
    device_info: metadata
}

### ViewTweet

- Method GET
- Path: `/tweet/<id>`
- Body: {
    content: str,
    username: str,
    creation_time: timestamp
}

### ViewTimeline

- Method: GET
- Path: `/timeline/<username>?page=<page number>&size=<items per page>&asof=<timestamp>`
- Body: {
    tweets: [tweet_object],
    next_page: {
        page: int
    }
}

## Database

Relation database: Postgresql

- Read heavy over write heavy.
- More read replicas that can handle the traffic.
- Hot partitions for famous users.

### Users

Columns:
- id: bigint unique autoincrement
- username: str

Indexes:
- id
- username

### Tweets

Columns:
- id: bigint unique autoincrement
- user_id: bigint nonnull (fk to users)
- creation_time: timestamp nonnull
- update_time: timestamp nullable
- content: varchar

Indexes:
- id
- user_id, creation_time desc

### Followers

Columns:
- id: bigint unique autoincrement
- follower: bigint nonnull (fk to users)
- followee: bigint nonnull (fk to users)

Indexes:
- id
- follower
- followee

---

How to make the home timeline less taxing to the service?
- Caching is not trivial.
- Create a separate database that stores just the latest 10 tweets of every user.
    - Only store user_id and creation time. Pull content from tweets table.
    - Reduce the amount of storage and search space would result in faster queries.
    - Maybe something like Redis.

10M * 10 * id (8 B) * user_id (8 B) * creation_time (8 B) = 50 GB
