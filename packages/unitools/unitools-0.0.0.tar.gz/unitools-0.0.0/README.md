
# Unitools

`unitools` is a cohesive collection of utility tools designed for Python 3, encapsulating various utility functions developed over the years. Given the absence of such tools in earlier times, `unitools` serves as a treasure trove for developers seeking a unified solution for various tasks.

## Installation

You can install `unitools` via pip:
```bash
pip install unitools
```


## Modules

`unitools` comprises multiple modules, each designed for a specific purpose. Below is a description of the `ICMPv4` module.

### ICMPv4 Module

The `ICMPv4` module offers a way to generate and handle ICMP (Internet Control Message Protocol) echo requests, commonly known as "pings". It has been built to be cross-platform compatible, seamlessly operating on both Windows and Linux.

#### Features

- **Ping Utility**: Send ICMP echo requests and retrieve the response.
- **Dynamic Packet Creation**: Build ICMP packets on the fly based on the operating system.
- **Response Handling**: Decode ICMP responses and provide a structured representation.

#### Usage

```python
from unitools.ICMPv4 import Request

icmp_request = Request(address="8.8.8.8")
response = icmp_request.ping()

print(response)
```

#### Methods
-   **ping**: Initiates an ICMP request and awaits its response.
-   **create_socket**: Establishes the required socket for ICMP communication.
-   **create_icmp_packet**: Constructs the ICMP packet ready for transmission.
-   **send_on_socket**: Sends the constructed ICMP packet.

#### ICMPv4.Response

An inner class, `Response`, embodies the ICMP reply, furnishing details like the responder's IP address, byte size of the packet, round-trip time, and TTL (Time-to-Live).

## Contribute

Contributions to `unitools` are always welcome. Feel free to submit pull requests or raise issues.

## License
[MIT License](https://github.com/MrTwister96/unitools/blob/main/LICENSE)