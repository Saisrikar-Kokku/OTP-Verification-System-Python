# **OTP Verification System**

## **Project Overview**
The OTP (One-Time Password) Verification System is a Python-based application designed to enhance security by generating a 6-digit OTP and sending it to the user's email address for verification. The user is required to input the received OTP to gain access. This system is ideal for implementing an extra layer of authentication in various applications.

---

## Features
- **Random OTP Generation**: Generates a secure 6-digit random OTP.
- **Email Delivery**: Sends the OTP directly to the user's email using Gmail's SMTP server.
- **Secure Verification**: Verifies the user-entered OTP against the generated OTP.
- **Retry Mechanism**: Allows up to 3 attempts for the user to enter the correct OTP.
- **Error Handling**: Handles errors like missing credentials and failed email delivery gracefully.

---

## Project Structure
```
OTP-Verification-System/
└── OTP-Verification-System.pptx 
├── OTP-Verification-System-Documentation.docx                             # List of dependencies (if any)
├── otp_verification_system.py  # Main script for OTP generation and verification
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
```

---

## How It Works
1. The user provides their email address.
2. A 6-digit OTP is generated and sent to the provided email.
3. The user enters the OTP they received.
4. The system verifies the OTP and grants or denies access based on the result.

---

## Requirements
- Python 3.x
- Internet connection (for email sending)

### Python Libraries Used
- `smtplib`: For sending emails.
- `email.message`: For formatting the email message.
- `os`: For accessing environment variables.
- `random`: For generating the OTP.

---

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/Saisrikar-Kokku/OTP-Verification-System-Python
cd otp-verification-system
```

### 2. Configure Email Credentials
Set up your email credentials securely using environment variables:

#### For Linux/MacOS:
```bash
export EMAIL_ADDRESS="your_email@gmail.com"
export EMAIL_PASSWORD="your_app_password"
```

#### For Windows (Command Prompt):
```cmd
set EMAIL_ADDRESS=your_email@gmail.com
set EMAIL_PASSWORD=your_app_password
```

> **Note**: Use an app-specific password if your email provider requires it.

### 3. Install Dependencies
Ensure you have Python installed along with the required libraries (all are part of the standard library).

### 4. Run the Script
Run the script using:
```bash
python otp_verification_system.py
```

---

## Testing
- Input a valid email address and check your inbox for the OTP.
- Enter the OTP in the program to verify successful authentication.
- Test incorrect OTP entries to ensure the retry mechanism works.

---

## Future Enhancements
- Add a graphical user interface (GUI) using libraries like Tkinter or PyQt.
- Implement OTP expiration for enhanced security.
- Support SMS-based OTP delivery.
- Improve logging for better debugging and monitoring.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.

---

## Author
**Saisrikar-Kokku**  
[GitHub Profile](https://github.com/Saisrikar-Kokku)

---

## Feedback
If you have any feedback, questions, or suggestions, feel free to open an issue or contact me directly!

-K.SAISRIKAR 
-	Email: Saisrikarkokku7674@gmail.com 