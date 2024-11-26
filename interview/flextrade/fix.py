"""
Find the value of a tag in a FIX message.

Given a FIX message as a string, implement a method to find the value of a tag.
Return null if the tag does not exist. Fields are separated by '|'

Example:
8=FIX.4.3|9=251|35=D|34=2476|49=CLIENTID|56=BROKERID|52=20221215-18:41:13.463|11=uAA0002-20221215|15=EUR|21=1|38=500000.00|40=D|44=1.061281|54=1|55=EUR/USD|59=3|64=20221227|117=PRF20XQYVX3HXT_1|60=20221215-18:41:13.462|461=FFCPNO|453=1|448=TEST|447=D|452=13|10=089
"""

from typing import Optional


def get_string_field(msg: str, tag: str) -> Optional[str]:
    for tag_value in msg.split("|"):
        msg_tag, msg_value = tag_value.split("=")
        if tag == msg_tag:
            return msg_value

    return None


def get_string_field(msg: str, tag: str) -> Optional[str]:
    start = 0
    finish = start
    while start < len(msg):
        while finish < len(msg) and msg[finish] != "|":
            finish += 1
        msg_tag, msg_value = msg[start:finish].split("=")
        if tag == msg_tag:
            return msg_value

        start = finish + 1
        finish = start

    return None


tag = "35"
message = "8=FIX.4.3|9=251|35=D|34=2476|49=CLIENTID|56=BROKERID|52=20221215-18:41:13.463|11=uAA0002-20221215|15=EUR|21=1|38=500000.00|40=D|44=1.061281|54=1|55=EUR/USD|59=3|64=20221227|117=PRF20XQYVX3HXT_1|60=20221215-18:41:13.462|461=FFCPNO|453=1|448=TEST|447=D|452=13|10=089"
assert get_string_field(message, tag) == "D"
