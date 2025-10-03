# 🏦 ATM Simulator

A simple **console-based ATM Simulator** built in Python.  
It uses a **loop-based menu system**, **file I/O** to store balance and transaction history, and **functions for modularity**.

## 📝 Description
The **ATM Simulator** replicates basic ATM functionality in the terminal.  
Users can:
- Deposit money
- Withdraw money
- View account balance
- Check transaction history  

The program handles invalid options and prevents withdrawals when the balance is insufficient.

## ✨ Features
- 🌀 **Loop-based menu system** for continuous interaction
- 💾 **File I/O** to store balance and transaction history
- 🛠️ **Modular code** using Python functions
- ⚠️ Handles **incorrect options** gracefully
- 🚫 Prevents **overdrawing** beyond available balance

## ⚙️ Requirements
- Python 3.x  
- No external libraries required — only Python’s built-in modules like:
  - `os`
  - `time` (if used)
  - `io` / `open` for file handling

## ▶️ How to Run
1. Clone or download this repository.
2. Open the project folder in your terminal or command prompt.
3. Run the following command:
   ```bash
   python main.py
