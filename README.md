
## 🛡️ Password Validator

A simple yet robust Python script that validates user-entered passwords against multiple security criteria. Designed for clarity, modularity, and real-time feedback, this project helps users create secure passwords while reinforcing core Python logic.

---

### 📌 Features

- Interactive loop for continuous password entry
- Real-time feedback for each failed condition
- Short-circuit logic for blank input
- Modular validation checks:
  - Minimum length (≥ 8 characters)
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
- Clean control flow using flags and `continue`
- Easy to extend with special character checks or scoring

---

### 🧠 Validation Logic

| **Rule**                  | **Purpose**                                      | **Code Snippet** |
|---------------------------|--------------------------------------------------|------------------|
| Blank password            | Prevents empty submissions                       | `if not password:` |
| Minimum length            | Ensures basic complexity                         | `len(password) < 8` |
| Uppercase letter required | Prevents all-lowercase passwords                 | `not any(char.isupper() for char in password)` |
| Lowercase letter required | Prevents all-uppercase passwords                 | `not any(char.islower() for char in password)` |
| Digit required            | Adds numeric complexity                         | `not any(char.isdigit() for char in password)` |

---

### 🚀 How to Run

1. Make sure Python is installed.
2. Save the script as `password_validator.py`.
3. Run it in your terminal:

```bash
python password_validator.py
```

---

### 🔧 Future Enhancements

- Add special character validation
- Implement password strength scoring
- Limit retry attempts or add lockout logic
- Export validation results to a log file
- Integrate with a GUI or web form

---

### 👨‍💻 Author

Built by **Siyamthanda Ndzipha (Edison)** — a detail-driven Python developer focused on mastering fundamentals and building real-world tools with clarity and precision.

---

Want to turn this into a GitHub-ready project with a license, contribution guide, and issue tracker? I can help scaffold that too.
