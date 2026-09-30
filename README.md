# Attendance Skippable Classes Calculator

## Overview

The **Attendance Skippable Classes Calculator** is a simple Python program that helps students determine whether they are currently above or below the required **75% attendance** threshold.

The program takes:
- Total number of classes held so far
- Number of classes attended

It then calculates the current attendance percentage and tells the student either:

1. How many consecutive classes they need to attend to reach 75%, if their attendance is below 75%, or
2. How many upcoming classes they can skip while still maintaining at least 75% attendance.

## Features

- Accepts user input through the terminal.
- Calculates current attendance percentage.
- Checks attendance against the 75% requirement.
- Calculates the number of classes required to reach 75%.
- Calculates the maximum number of classes that can be skipped.
- Uses `math.ceil()` and `math.floor()` to ensure whole-class results.
- Displays attendance with two decimal places.

## Requirements

- Python 3.x
- Python's built-in `math` module

No external packages are required.

## How to Run

1. Save the Python code in a file, for example:

```text
attendance_calculator.py
```

2. Open a terminal in the folder containing the file.

3. Run:

```bash
python attendance_calculator.py
```

4. Enter the requested values.

### Example

```text
Enter total number of classes held so far: 40
Enter number of classes you have attended: 32

Your current attendance is: 80.00%
You can safely skip up to 2 class(es) without dropping below 75%.
```

## Mathematical Logic

Let:

- `T` = total classes held
- `A` = classes attended

Current attendance:

```text
(A / T) × 100
```

### If attendance is below 75%

Suppose `x` additional classes are attended:

```text
(A + x) / (T + x) >= 0.75
```

Solving:

```text
A + x >= 0.75(T + x)
A + x >= 0.75T + 0.75x
0.25x >= 0.75T - A
x >= 3T - 4A
```

Therefore, the program uses:

```python
math.ceil(3 * total_classes - 4 * attended_classes)
```

`ceil()` is used because the student must attend a whole number of classes.

### If attendance is 75% or higher

Suppose `x` future classes are skipped:

```text
A / (T + x) >= 0.75
```

Solving:

```text
A >= 0.75(T + x)
A / 0.75 >= T + x
x <= A / 0.75 - T
```

Therefore, the program uses:

```python
math.floor((attended_classes / 0.75) - total_classes)
```

`floor()` is used because the result must not exceed the maximum safe number of skipped classes.

## Project Structure

```text
attendance-calculator/
├── attendance_calculator.py
├── README.md
└── Attendance_Skippable_Classes_Project_Report.docx
```

## Limitations

- The program assumes that the required attendance percentage is fixed at 75%.
- It does not account for different attendance requirements for different subjects.
- It does not track individual class schedules or dates.
- Inputs are expected to be valid non-negative whole numbers, with total classes greater than zero.

## Future Improvements

Possible improvements include:

- Allowing the user to enter a custom attendance target.
- Adding input validation and error handling.
- Supporting multiple subjects.
- Providing a graphical user interface.
- Tracking attendance over a semester.
- Showing attendance projections for future classes.

## Conclusion

This project demonstrates how Python can be used to solve a practical student problem using user input, arithmetic operations, conditional statements, functions, and the `math` module.
