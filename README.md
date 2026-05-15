# 💰 Loan Application Portal

A Django-based web application designed to simplify the loan application process for users by reducing repeated visits to the bank.  

The platform allows users to explore different loan schemes, calculate EMI, and connect with agents who assist with document verification and application processing before final submission to the bank.

---

## 🚀 Project Overview

Applying for a loan often requires multiple visits to the bank for understanding loan options, checking eligibility, and document verification.

This project solves that by providing an online system where:

- Users can check available loan types
- Calculate estimated monthly EMI
- Submit loan requests online
- Agents assist with verification and guidance
- Verified applications are forwarded to the bank

---

## ✨ Features

### User Portal
- User registration & login
- Browse loan categories
- View detailed loan information
- EMI calculator
- Submit loan applications
- Track application progress

### Agent Portal
- Review submitted applications
- Verify customer documents
- Assist applicants with next steps
- Forward verified applications to bank

### Admin Portal
- Manage loan types
- Manage users and agents
- Monitor applications
- Update loan information

---

## 🛠 Tech Stack

- Backend: Django
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite
- Language: Python

---

## 📊 EMI Calculator

The EMI calculator helps users estimate monthly repayment before applying.

Formula used:

:contentReference[oaicite:0]{index=0}

Where:

- **P** = Loan amount  
- **R** = Monthly interest rate  
- **N** = Loan duration in months  

---

## 🔄 Workflow

1. User creates account
2. Selects loan type
3. Checks loan details
4. Uses EMI calculator
5. Applies online
6. Agent verifies documents
7. Application sent to bank
8. Final approval process

---

## 📷 Screenshots

Create `assets/` folder and add screenshots.

### Homepage
![Homepage](assets/homepage.png)

### Loan Types
![Loan Types](assets/loan-types.png)

### EMI Calculator
![EMI](assets/emi.png)

### Agent Dashboard
![Dashboard](assets/agent-dashboard.png)

---

## 🎥 Demo Video

[![Watch Demo](assets/demo-thumbnail.png)](https://youtu.be/YOUR_VIDEO_LINK)

---

## ⚙ Installation

```bash
git clone https://github.com/yourusername/loan-application-portal.git
cd loan-application-portal
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
