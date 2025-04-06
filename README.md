
<p align="center">
  <img src="https://github.com/natidever/velox/blob/main/logo.jpg" alt="Velox Banner"  />
</p>
---

# ⚡️ Velox - The Fastest Solana Telegram Trading Bot

Velox is an **async-first**, ultra-fast trading bot built for **Telegram** users who want to interact with the **Solana blockchain**—right from their chat window.

---

### 🚀 Features

- 🔐 **Create Your Own Wallet**  
  Instantly generate a Solana wallet within Telegram. No external tools required.

- 💸 **Deposit SOL Securely**  
  Top up your Velox wallet with SOL to begin trading with lightning speed.

- 📊 **Live Price Tracking**  
  Integrated with **Dexscreener** to fetch the **latest token prices** on Solana.

- 🔄 **Swap Instantly**  
  Execute fast, gas-efficient swaps directly on the **Solana blockchain**, powered by **Jito validator** infrastructure.

- ⚡️ **Async-First Architecture**  
  Built with speed and scalability in mind using Python’s asyncio stack.

---

### 📦 Tech Stack

- 🐍 Python (asyncio, aiohttp, aiogram)
- 💬 Telegram Bot API
- 🌊 Solana JSON RPC + WebSockets
- 🧠 Dexscreener API
- 🏎️ Jito Validator
- 🔁 SPL Token Swap logic

---

### 🧪 Getting Started

1. **Clone the repo**

```bash
git clone https://github.com/your-username/velox.git
cd velox
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file and add your config:

```env
TELEGRAM_BOT_TOKEN=your_bot_token

```

4. **Run the bot**

```bash
python bot.py
```

---

### 🛡️ Security Notice

Velox allows users to create and manage wallets inside Telegram. While this is highly convenient, remember:
- **Private keys are stored temporarily and safely** but never share your credentials.
- This bot is for **educational purposes**; use at your own risk in production or with mainnet assets.

---

### 💡 Roadmap

- [x] Wallet creation & deposit
- [x] Swap functionality
- [x] Live token prices from Dexscreener
- [ ] Raydium/Orca liquidity support


---

### 🧠 Credits

Built with love for the Solana degens by [@natidever](https://github.com/natidever)


---

### 📜 License

MIT License

---
