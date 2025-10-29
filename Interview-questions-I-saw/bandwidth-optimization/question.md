## DataStream Bandwidth Maximization Problem
#### Context

You are part of an Infrastructure Engineering team managing a set of nodes, each with a given bandwidth capacity.

You need to establish several data streams between these nodes to maximize total bandwidth utilization.

### 🎯 Problem Description

You are given:

A list of integers bandwidths, representing the bandwidth capacity of each node.

An integer dataStreams, representing how many data streams need to be created.

Each data stream:

Connects two nodes: a main connection and a secondary connection.

Its bandwidth is the sum of the two node bandwidths.

You can connect:

A node to itself → e.g. (x, x)

Two different nodes → e.g. (x, y) or (y, x)

Each ordered pair (main, secondary) can be used once only.

Your goal is to select exactly dataStreams pairs that maximize the total bandwidth.

⚙️ Function Signature
def maximizeBandwidth(bandwidths: list[int], dataStreams: int) -> int:
    """
    Given node bandwidths and number of data streams,
    returns the maximum total bandwidth using unique (main, secondary) pairs.
    """

📘 Example 1
Input
bandwidths = [5, 4, 8, 4, 7]
dataStreams = 6

DataStream	Pair (x, y)	Bandwidth
1	(8,8)	16
2	(8,7)	15
3	(7,8)	15
4	(8,5)	13
5	(5,8)	13
6	(7,7)	14

✅ Maximum total bandwidth = 16 + 15 + 15 + 13 + 13 + 14 = 86