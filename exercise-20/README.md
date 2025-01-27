# Problem to Solve  

This program reads a file containing student names and their corresponding participation scores. It processes the data and calculates the total participation score for each student.  

## **Key Points to Consider**  

- The program expects a file where each line contains a student's name followed by their score.  
- It handles **two types of exceptions**:  
  - `BadLine`: Raised when a line contains more than four words (indicating a formatting error).  
  - `FileEmpty`: Raised when the file is empty.  
- If a student's name appears multiple times, their scores are summed.  
- The program displays the total participation score for each student.  
- Handles potential **I/O errors** (e.g., file not found).  
