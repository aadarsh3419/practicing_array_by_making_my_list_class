# Custom Dynamic Array & Sorting Implementation in Python (Using ctypes)

**Author:** Aadarsh Tiwari

---

## 📌 Main Purpose of This Project (Very Important)

Is project ka **sabse main purpose** yeh tha:

1. **Array ko deeply samajhna** (memory, size vs capacity, resizing)
2. **Python ki built-in `list` use kiye bina** apni **khud ki list class** banana
3. Ye samajhna ki list ke andar:

   * elements kaise store hote hain
   * size kaise badhta hai
   * insert / delete kaise kaam karta hai

Isliye `mylist` class banayi gayi hai — jo internally **dynamic array** ki tarah kaam karti hai.

Sorting is project ka secondary part hai, jiska purpose **algorithm thinking aur optimization** dikhana hai.

---

## 🧠 What is `mylist`?

`mylist` ek **custom list implementation** hai jo:

* `ctypes` ka use karke manual memory allocate karti hai
* Dynamic resizing follow karti hai (capacity double)
* Python `list` ke basic features replicate karti hai

Ye project mainly **learning ke liye** banaya gaya hai, na ki built-in list ko replace karne ke liye.

---

## 🧠 `mylist` Class – Functions & Their Purpose

Neeche diye gaye har function ka **clear kaam** bataya gaya hai.

---

### 🔹 `__init__(self)`

**Purpose:**

* Empty dynamic array initialize karna

---

### 🔹 `__make_array(self, capacity)`

**Purpose:**

* Low-level array memory create karna

---

### 🔹 `__len__(self)`

**Purpose:**

* Current number of elements batana

---

### 🔹 `append(self, item)`

**Purpose:**

* List ke end me element add karna
* Agar capacity full ho jaaye to size double karna

---

### 🔹 `__str__(self)`

**Purpose:**

* List ko readable format me print karna

---

### 🔹 `__getitem__(self, index)`

**Purpose:**

* Index ke through element access karna

---

### 🔹 `pop(self)`

**Purpose:**

* Last element remove karna

---

### 🔹 `clear(self)`

**Purpose:**

* List ko logically empty karna

---

### 🔹 `find(self, item)`

**Purpose:**

* Given element ka index find karna

---

### 🔹 `insert(self, pos, item)`

**Purpose:**

* Given position par element insert karna

---

### 🔹 `__delitem__(self, pos)`

**Purpose:**

* Given index ka element delete karna

---

### 🔹 `remove(self, item)`

**Purpose:**

* Value ke basis par element remove karna

---

### 🔹 `max(self)`

**Purpose:**

* Maximum element nikalna

---

### 🔹 `min(self)`

**Purpose:**

* Minimum element nikalna

---

### 🔹 `sum(self)`

**Purpose:**

* Sabhi elements ka sum nikalna

---

## 🔽 Sorting Functions (Bubble Sort → Merge Sort)

Sorting ka purpose yahan **sirf order change karna nahi** tha, balki ye dikhana tha ki:

> jaise-jaise data bada hota hai, waise-waise better algorithm ki zarurat padti hai

---

### 🔹 `decen()` – Bubble Sort (Descending Order)

**Purpose:**

* Basic sorting logic samajhna
* Adjacent comparison ka concept clear karna

**Algorithm Used:**

* Bubble Sort

**Time Complexity:**

* ❌ O(n²)

**Note:**

* Ye intentionally banaya gaya hai learning ke liye

---

### 🔹 `sort()` – Merge Sort (Descending Order)

**Purpose:**

* Bubble Sort ki high time complexity kam karna
* Same descending order ko efficient banana

**Algorithm Used:**

* Merge Sort

**Time Complexity:**

* ✅ O(n log n)

**Important Point:**

* Merge Sort isliye use kiya gaya kyunki data bada hone par performance better rehti hai

---

### 🔹 `accen()` – Merge Sort (Ascending Order)

**Purpose:**

* Ascending order sorting implement karna
* Comparison logic ko aur strong banana

**Algorithm Used:**

* Merge Sort

**Time Complexity:**

* ✅ O(n log n)

---

### 🔹 `__resize(self, new_capacity)`

**Purpose:**

* Array ki capacity badhana
* Purane data ko new memory me copy karna

---

## 🧠 Final Conclusion

* Is project ka **main focus array aur custom list banana** tha
* Sorting functions isliye add kiye gaye taaki:

  * Bubble Sort se base clear ho
  * Merge Sort se time complexity improve ho

Is project se yeh clear hota hai ki:

> **Better performance ke liye sirf code nahi, algorithm change karna padta hai**

---

**Author:** Aadarsh Tiwari
