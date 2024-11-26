data = {
    # Timestamp Team        Market      Ticker          PnL
    (123456789, "TEAM A", "NYSE", "GME"): 123.123,
    (123456789, "TEAM B", "NASDAQ", "AMC"): 123000.123,
    (123456790, "TEAM A", "TSX", "AAPL"): 12.12,
    (123456791, "TEAM C", "NYSE", "BB"): 1.0,
    ...(123456800, "TEAM B", "HKEX", "CHINA#1"): 0.0,
}
# O(N), where N = number of rows


# TEAM -> {A...Z}
# MARKET -> hundreds+
# TICKERS -> thousands+
# TIMESTAMPS -> millions+

data = {
    "TEAM A": {
        "NYSE": {
            "GME": {
                123456789: 123.123,
                123456790: 125.123,
                123456791: 126.123,
            },
        }
    }
}
# O(T) where T = number of teams

# Hash combination of "team,market,ticker"
# ("TEAM A", "NYSE", "GME") -> id
#
# Example:
# "TEAM A,NYSE,GME" -> 111
# "TEAM B,NASDAQ,AMC" -> 222

# Query all PnL for a given time range?
data = {123456789: [111, 222]}
