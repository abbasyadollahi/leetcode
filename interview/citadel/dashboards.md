# Dashboards

## Summary

Input of a table
Provides filter on data
Pushes data to UI as a table

### Data

- 200 columns
- 1M rows
- Primitive types
- List of dicts

### Filter

- From the UI (user filtering)
- From the server (authorization, archived)
- No pagination

## Requirements

### Functional

- Filter the data
- Paint the UI
- Authorization of the data

### Non Functional

- As quick possible (async)
- Favor consistent data to all users over precise data
- Reasonable availability
- Reliable
- 1000 users

## Design

UI - LB - Gateway - Server 1 (metadata server) - Queue 1 (generic requests) + Queue 2 (personal requests) - Server 2 (processing server) - HPC - Database + Filesystem

Server 1 -> Stores metadata for generic and personal dashboard requests (job status, expiration, filters, owner)
Server 2 -> Polls queues to process the dashboard requests and launch jobs

Queue 1 -> Dashboard requests to create generic dataset
Queue 2 -> Dashboard requests to create personal dataset

### Generic

Queue 1 - Server 2 - HPC - Jobs - Database - Filesystem

Split into data segments
Reduce into a large dataset
Store generic dataset in filesystem

### Personal

Queue 2 - Server 2 - HPC - Jobs - Database - Filesystem

Fetch data from filesystem
Filter based on user
Reduce into a subset of dataset
Store personal dataset in filesystem
User can fetch using the link

### UI

- Use virtualization to reduce DOM nodes displayed
- Prerender HTML instead of storing raw personal dataset
- Stream bytes from personal dataset instead of loading all in memory
- Use pixel location to track which chunk of bytes to stream
