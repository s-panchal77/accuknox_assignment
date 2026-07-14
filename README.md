# AccuKnox Django Trainee Assessment

This repository contains my solutions for the **AccuKnox Django Trainee Assessment**. The objective of this assessment is to demonstrate the behavior of Django Signals through practical experiments and implement a custom iterable Python class.

---

## Candidate

**Sarthak Panchal**  
📍 Himmatnagar, Gujarat, India  
📧 sarthak7704@gmail.com  
🔗 GitHub: https://github.com/s-panchal77  
🔗 LinkedIn: https://www.linkedin.com/in/sarthak-panchal-69244633b/

---

## Assignment Overview

This repository contains solutions for the following assessment questions:

- **Q1:** Are Django signals synchronous or asynchronous by default?
- **Q2:** Do Django signals execute in the same thread as the caller?
- **Q3:** Do Django signals execute within the same database transaction as the caller?
- **Q4:** Implement an iterable `Rectangle` class using core Python.

---

## Project Structure

```text
accuknox-django-assignment/
│
├── accuknox_project/          # Django project configuration
├── signals_app/               # Solutions for Q1, Q2 and Q3
│   ├── models.py
│   ├── signals.py
│   └── ...
│
├── custom_classes/            # Solution for Q4
│   ├── rectangle.py
│   └── ...
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

## Tech Stack

- Python 3.14
- Django 6
- SQLite3
- Git

---

## Setup

Clone the repository

```bash
git clone https://github.com/s-panchal77/accuknox_assignment.git
cd accuknox_assignment
```

Create virtual environment

```bash
python -m venv venv
```

Activate

**Windows**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start Django shell

```bash
python manage.py shell
```

---

# Question 1

### Objective

Prove that Django Signals execute **synchronously** by default.

### Verification

```python
from signals_app.models import UserProfile

print("Before save")
UserProfile.objects.create(name="SyncTest")
print("After save")
```

Expected behavior

- Signal output appears first.
- `After save` prints only after the signal finishes.

---

# Question 2

### Objective

Prove that Django Signals execute in the **same thread** as the caller.

### Verification

```python
import threading
from signals_app.models import UserProfile

caller = threading.get_ident()

profile = UserProfile.objects.create(name="ThreadTest")

signal = getattr(profile, "signal_thread_id")

print(caller == signal)
```

Expected output

```text
True
```

---

# Question 3

### Objective

Prove that Django Signals execute inside the **same database transaction** as the caller.

### Verification

```python
from django.db import transaction
from signals_app.models import UserProfile

try:
    with transaction.atomic():
        UserProfile.objects.create(name="TxUser")
        raise Exception()

except Exception:
    pass

print(UserProfile.objects.filter(name="TxUser").exists())
```

Expected output

```text
False
```

---

# Question 4

### Objective

Implement a pure Python iterable `Rectangle` class.

### Verification

```python
from custom_classes.rectangle import Rectangle

rectangle = Rectangle(10, 20)

for item in rectangle:
    print(item)
```

Expected output

```text
{'length': 10}
{'width': 20}
```

---

## Design Decisions

- Simple, beginner-friendly implementation
- Focused on demonstrating concepts
- No unnecessary abstractions
- Pure Python implementation for Question 4
- Easy to understand and verify

---

## Submission Status

- ✅ Question 1 Completed
- ✅ Question 2 Completed
- ✅ Question 3 Completed
- ✅ Question 4 Completed
- ✅ Execution verified
- ✅ Documentation completed# AccuKnox Django Trainee Assessment

This repository contains my solutions for the **AccuKnox Django Trainee Assessment**. The objective of this assessment is to demonstrate the behavior of Django Signals through practical experiments and implement a custom iterable Python class.

---

## Candidate

**Sarthak Panchal**  
📍 Himmatnagar, Gujarat, India  
📧 sarthak7704@gmail.com  
🔗 GitHub: https://github.com/s-panchal77  
🔗 LinkedIn: https://www.linkedin.com/in/sarthak-panchal-69244633b/

---

## Assignment Overview

This repository contains solutions for the following assessment questions:

- **Q1:** Are Django signals synchronous or asynchronous by default?
- **Q2:** Do Django signals execute in the same thread as the caller?
- **Q3:** Do Django signals execute within the same database transaction as the caller?
- **Q4:** Implement an iterable `Rectangle` class using core Python.

---

## Project Structure

```text
accuknox-django-assignment/
│
├── accuknox_project/          # Django project configuration
├── signals_app/               # Solutions for Q1, Q2 and Q3
│   ├── models.py
│   ├── signals.py
│   └── ...
│
├── custom_classes/            # Solution for Q4
│   ├── rectangle.py
│   └── ...
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

## Tech Stack

- Python 3.14
- Django 6
- SQLite3
- Git

---

## Setup

Clone the repository

```bash
git clone https://github.com/s-panchal77/accuknox_assignment.git
cd accuknox_assignment
```

Create virtual environment

```bash
python -m venv venv
```

Activate

**Windows**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start Django shell

```bash
python manage.py shell
```

---

# Question 1

### Objective

Prove that Django Signals execute **synchronously** by default.

### Verification

```python
from signals_app.models import UserProfile

print("Before save")
UserProfile.objects.create(name="SyncTest")
print("After save")
```

Expected behavior

- Signal output appears first.
- `After save` prints only after the signal finishes.

---

# Question 2

### Objective

Prove that Django Signals execute in the **same thread** as the caller.

### Verification

```python
import threading
from signals_app.models import UserProfile

caller = threading.get_ident()

profile = UserProfile.objects.create(name="ThreadTest")

signal = getattr(profile, "signal_thread_id")

print(caller == signal)
```

Expected output

```text
True
```

---

# Question 3

### Objective

Prove that Django Signals execute inside the **same database transaction** as the caller.

### Verification

```python
from django.db import transaction
from signals_app.models import UserProfile

try:
    with transaction.atomic():
        UserProfile.objects.create(name="TxUser")
        raise Exception()

except Exception:
    pass

print(UserProfile.objects.filter(name="TxUser").exists())
```

Expected output

```text
False
```

---

# Question 4

### Objective

Implement a pure Python iterable `Rectangle` class.

### Verification

```python
from custom_classes.rectangle import Rectangle

rectangle = Rectangle(10, 20)

for item in rectangle:
    print(item)
```

Expected output

```text
{'length': 10}
{'width': 20}
```

## Design Decisions

- Simple, beginner-friendly implementation
- Focused on demonstrating concepts
- No unnecessary abstractions
- Pure Python implementation for Question 4
- Easy to understand and verify

---

## Submission Status

- ✅ Question 1 Completed
- ✅ Question 2 Completed
- ✅ Question 3 Completed
- ✅ Question 4 Completed
- ✅ Execution verified