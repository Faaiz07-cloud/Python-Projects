# 💬 Chat App (Local GUI + Socket Programming)

A **real-time chat application** built with **Python sockets** for communication and **Tkinter** for the graphical interface.  
The app supports **both Peer-to-Peer (P2P)** and **Client-Server** chat systems, allowing direct connections as well as multi-user broadcasting through a server.

---

## 📝 Description
The **Chat App** demonstrates how to build a real-time messaging system using Python’s **socket programming** capabilities.  

It includes:
- A **P2P chat system** (console and GUI) where two users can chat directly.
- A **Client-Server chat system** where multiple clients can connect to a server and exchange messages that are **broadcast to all connected clients**.
- A **professional Tkinter GUI** for an intuitive chat experience in the P2P mode.

---

## ✨ Features
- 🔗 **Socket-based communication**
- 👥 **Two chat modes:**
  - **P2P Chat:** Direct connection between two clients (available in CLI and GUI)
  - **Client-Server Chat:** A central server broadcasts messages to all connected clients
- 🖥️ **Tkinter-based GUI** for the P2P chat
- 💬 **Real-time messaging**
- 🟢 Handles **multiple clients** seamlessly
- 🚫 Prevents crashes on unexpected client disconnects
- ⚡ **Lightweight and fast**

---

## ⚙️ Requirements
- Python 3.x  
- Built-in Python modules:
  - `socket` – for networking
  - `threading` – for handling multiple clients and real-time updates
  - `tkinter` – for GUI in the P2P mode

👉 No third-party installations required.

---

## ▶️ How to Run

### 🖥️ Running the P2P Chat in GUI Mode
1. Start the 1st Terminal:
   ```bash
   python main.py
   
2. Start the 2nd Terminal:
   ```bash
   python main.py
