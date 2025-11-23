# Broadcast Signal Encoding and Transmission Using UDP

## Abstract
This project implements **broadcast signal encoding and transmission using UDP**. Multiple input chains are combined via a broadcast-style XOR operation and converted into ±1 digital signals. Encoded signals are sent over UDP to a receiver, which reconstructs them as Python lists, demonstrating real-time digital signal processing and network-based communication.

## File Descriptions

- **encode.py** – Generates chain code signals, applies broadcast XOR encoding, converts bits to ±1, and sends the encoded signal to a receiver via UDP.
- **decode.py** – Receives UDP data, decodes the incoming bytes back into Python lists, and prints or processes the received signals.

## How to Run

1. Open **two separate command prompt/terminal windows**.
2. In the first window, run the receiver:
   ```bash
   python decode.py
