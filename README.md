# Custom Dynamic Array & Sorting Implementation in Python (Using ctypes)

**Author:** Aadarsh Tiwari

---

## 📌 Main Purpose of This Project (Very Important)

The **primary goal of this project** was:

1. To **deeply understand how arrays work internally** (memory, size vs capacity, resizing)
2. To build **my own list class without using Python’s built-in `list`**
3. To understand how a list handles:

   * element storage
   * size growth
   * insertion and deletion operations

For this reason, the `mylist` class was created, which internally behaves like a **dynamic array**.

Sorting is a secondary part of this project, added to demonstrate **algorithmic thinking and optimization**.

---

## 🧠 What is `mylist`?

`mylist` is a **custom list implementation** that:

* Uses `ctypes` for manual memory allocation
* Follows dynamic resizing (capacity doubling strategy)
* Replicates the basic behavior of Python’s built-in `list`

This project is mainly built **for learning purposes**, not to replace Python’s native list.

---

## 🧠 `mylist` Class – Functions & Their Purpose

Below is a clear explanation of **each function implemented inside the `mylist` class**.

---

### 🔹 `__init__(self)`

**Purpose:**

* Initializes an empty dynamic array

---

### 🔹 `__make_array(self, capacity)`

**Purpose:**

* Creates low-level array memory using `ctypes`

---

### 🔹 `__len__(self)`

**Purpose:**

* Returns the current number of elements in the list

---

### 🔹 `append(self, item)`

**Purpose:**

* Adds an element to the end of the list
* Doubles the capacity when the array is full

---

### 🔹 `__str__(self)`

**Purpose:**

* Prints the list in a readable format

---

### 🔹 `__getitem__(self, index)`

**Purpose:**

* Allows element access using indexing

---

### 🔹 `pop(self)`

**Purpose:**

* Removes the last element from the list

---

### 🔹 `clear(self)`

**Purpose:**

* Logically clears the list

---

### 🔹 `find(self, item)`

**Purpose:**

* Finds and returns the index of a given element

---

### 🔹 `insert(self, pos, item)`

**Purpose:**

* Inserts an element at a given position

---

### 🔹 `__delitem__(self, pos)`

**Purpose:**

* Deletes the element at the given index

---

### 🔹 `remove(self, item)`

**Purpose:**

* Removes an element based on its value

---

### 🔹 `max(self)`

**Purpose:**

* Returns the maximum element in the list

---

### 🔹 `min(self)`

**Purpose:**

* Returns the minimum element in the list

---

### 🔹 `sum(self)`

**Purpose:**

* Returns the sum of all elements

---

## 🔽 Sorting Functions (Bubble Sort → Merge Sort)

The purpose of sorting in this project is **not just to change the order**, but to show that:

> As data size increases, more efficient algorithms become necessary.

---

### 🔹 `decen()` – Bubble Sort (Descending Order)

**Purpose:**

* To understand basic sorting logic
* To clearly grasp adjacent element comparison

**Algorithm Used:**

* Bubble Sort

**Time Complexity:**

* ❌ O(n²)

**Note:**

* This implementation is intentionally included for learning purposes

---

### 🔹 `sort()` – Merge Sort (Descending Order)

**Purpose:**

* To reduce the high time complexity of Bubble Sort
* To efficiently sort data in descending order

**Algorithm Used:**

* Merge Sort

**Time Complexity:**

* ✅ O(n log n)

**Important Point:**

* Merge Sort is used because it performs significantly better on large datasets

---

### 🔹 `accen()` – Merge Sort (Ascending Order)

**Purpose:**

* To implement efficient sorting in ascending order
* To strengthen comparison-based logic

**Algorithm Used:**

* Merge Sort

**Time Complexity:**

* ✅ O(n log n)

---

### 🔹 `__resize(self, new_capacity)`

**Purpose:**

* Increases the array capacity
* Copies old data into newly allocated memory

---

## 🧠 Final Conclusion

* The **main focus of this project** was to understand arrays and build a custom list implementation
* Sorting functions were added to:

  * Learn basic sorting using Bubble Sort
  * Improve time complexity using Merge Sort

This project clearly demonstrates that:

> **Better performance comes from choosing better algorithms, not just writing more code.**

---

**Author:** Aadarsh Tiwari
