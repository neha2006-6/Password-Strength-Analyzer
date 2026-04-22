# 🔐 PassGuard — Password Strength Analyzer

> A beginner-friendly Python tool that analyzes the strength of your password and tells you exactly how to make it stronger.

---

## 📌 Description

**PassGuard** is a command-line based Password Strength Analyzer built with Python. It evaluates your password against multiple security criteria — length, character variety, entropy, and common password lists — and gives you a clear strength score with actionable feedback.

Whether you're learning cybersecurity or just want to build safer habits, PassGuard helps you understand what makes a password truly strong.

---

## ✨ Features

- ✅ Checks password length
- ✅ Detects uppercase, lowercase, digits, and special characters
- ✅ Compares against a list of common/leaked passwords
- ✅ Calculates password entropy score
- ✅ Rates password as **Weak / Medium / Strong / Very Strong**
- ✅ Hides password input while typing (using `getpass`)
- ✅ Gives suggestions to improve weak passwords

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| `re` | Regex pattern matching |
| `math` | Entropy calculation |
| `getpass` | Secure hidden input |
| `colorama` | Colored terminal output |

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/passguard.git
cd passguard
```

### 2. Install dependencies
```bash
pip install colorama
```

### 3. Run the program
```bash
python main.py
```

---

## 🧪 Example Output

```
Enter your password:

Analyzing password...

Results:
✅ Length         : 10 characters (Good)
✅ Uppercase      : Found
✅ Lowercase      : Found
✅ Digits         : Found
✅ Special Chars  : Found
✅ Not Common     : Unique password
📊 Entropy Score  : 65.4 bits

🟢 Strength: STRONG

💡 Tip: Add more random characters to make it Very Strong!

## 📚 What I Learned

- Python fundamentals (strings, loops, functions, dictionaries)
- Regex pattern matching with `re`
- Password entropy and security concepts
- Brute force & dictionary attack prevention
- Secure input handling with `getpass`

---

## 🔮 Future Improvements

- [ ] Add a GUI using `tkinter` or `streamlit`
- [ ] Integrate HaveIBeenPwned API for breach checking
- [ ] Generate strong password suggestions
- [ ] Export report as PDF

---
