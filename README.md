# 🐾 LynxScan - Fast & Minimal Port Scanner

**LynxScan** is a fast and minimal Python-based TCP port scanner.  
Like a lynx in the wild, it scans quickly and efficiently — always alert 👀

---

## ⚡ Features

- 🔍 TCP port scanning with custom range  
- ⏱ Adjustable timeout per port  
- 💾 Saves scan results to CSV file  
- 🧼 Clean modular code structure  
- 🐍 Pure Python — no external dependencies (for now!)

---

## 🚀 Installation

Clone the repository:

```
git clone https://github.com/monhacer/LynxScan.git 
cd LynxScan
```

No extra libraries required initially.

---

## 🛠 Usage

Run the tool:

```
python main.py
```

It will:
- Prompt for a target IP  
- Scan ports `20` to `1024`  
- Print the status of each port  
- Save results to a CSV file like: `192.168.1.1_scan_results.csv`

Sample Output:
`Port 22: Open Port 80: Closed ... Results saved to CSV.`

---

## 🔭 Roadmap

- 🏷 Banner grabbing for service detection  
- 🌐 Streamlit-powered web dashboard  
- ⚡ Multithreaded scanning for speed  
- 🕒 Scheduled scans with history

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to fork, enhance, and share 🚀

---

> 🐾 **LynxScan** — Stay sharp. Scan like a lynx.

