# The Traveling Zip

_**Zipline Take Home Coding Challenge**_

**Time Expectations**: we expect most folks to come up with a good solution in 90 minutes to 2 hours.

**Language**: `python3.8`, `golang 1`, `C++ 20`, `Rust`, `Ruby`, `Java`, or `TypeScript`. Choose one of these that will best showcase your work.

A Zipline **Nest** delivers many types of products to many hospitals using a fleet of **Zips**. In order to provide the best experience to our customers, we want to minimize the time-to-deliver. That said, some of our orders are **Emergency** deliveries, which have the potential to be lifesaving, whereas other orders are **Resupply** deliveries, leaving us some flexibility in delivery time.

The reality is that we have a limited number of Zips, and so we need to be more clever than immediately sending out a Zip as each order comes in. To help manage these logistics, the purpose of this exercise will be to write a `ZipScheduler` utility, to determine when and to which hospitals we should send out Zips for delivery.

To make things more interesting, we will also allow each Zip to carry multiple packages at a time. This means that a Zip can take off and deliver to several hospitals on one trip, before flying back to the Nest. Zips are limited by the cumulative distance they can fly on a given trip and have a maximum number of packages they can carry.

## Inputs

The starter code is set up to read these files which live in the `inputs` directory:

### `hospitals.csv`
The locations of the hospitals we are delivering to are provided in a CSV file specifying:

`Hospital Name, North, East`

`North` and `East` are provided in **meters** with our operations center assumed to be at `(0,0)`.

### `orders.csv`
In general operations, we will receive a sequence of orders in real-time. Each order specifies the hospital the delivery needs to go to, and the priority of the delivery. To test your system we are providing a list of orders in a CSV, specified as:

`Received Time, Hospital Name, Priority`

`Received Time` will be specified in seconds-since-midnight, and priority will be either `Emergency` or `Resupply`.

## Assumptions

1. You may assume that the Zip flies a series of straight-line paths, starting at the Nest, passing through each hospital, and then returning to the Nest.
2. The total length of the cumulative path cannot be greater than the maximum range of the Zip (defined in the starter code).
3. Zips travel at a fixed flight speed (also defined in the starter code).
4. Zips can only take off with up to the maximum number of packages (also defined in the starter code).
5. Once they have returned, Zips charge instantly and can be immediately sent out again.
6. The Nest has a limited number of Zips (also defined in the starter code).

## What We're Looking For

### 1. Implement the Scheduler

Your primary deliverable is a simple implementation of a `ZipScheduler` class, which can be used as part of our delivery management system. Your solution does not need to be sophisticated or complex, but instead should focus on being clear, logical, and bug-free. We've started this class, and ask that you fill in the following APIs:

`queue_order(order)` is used to add a new order to our queue, and will be called every time a new order arrives.

`launch_flights(current_time)` will be called periodically (e.g. once a minute), and should return a list of flights that are launched right now, with each flight having an ordered list of orders to serve. All flights returned from this will be launched simultaneously.

### 2. Choose _something_ to go deeper with

In addition to filling out the `ZipScheduler` class, we'd like to give you a chance to show off your software strength and passion. We are giving you the freedom to decide which ways you want to make this tool more useful. Ultimately, we're looking for you to demonstrate the ability to design usable software for either the operator or the engineers developing the system.

Ideas include:
- Making it easy to understand why an order isn't being prioritized
- A grading system to gauge how well various algorithms are working
- Visualizing orders and flight paths
- Writing a more optimal scheduling algorithm
- Algorithm configurability or modularity
- A playground to explore how changing our specs changes our operations (e.g. how more Zips reduces mean time to delivery)
- A suite of tests to prove correctness of your algorithm

### 3. Reasonable tradeoffs in your approach

We are customer obsessed and would love for you to show empathy for the customer. We also care about an answer that is easy to understand, easy to debug, and easy to extend.

We value your time and don't expect you to go very far with this problem. For example, it is ok to leave TODOs that you would come back to or interesting ideas that you'd consider exploring in the future. During the live code review, you will be given a chance to explain your choices and where you would go next with this problem.

## Ready for Take Off!

Feel free to email questions to your recruiter / the engineer who sent you this problem if you have any! We're happy to help.
