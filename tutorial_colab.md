## **Tutorial: How to Use Google Colab with GitHub**

### **Objective**:
This tutorial will guide you step-by-step on how to **clone a GitHub repository to Google Colab**, **edit the notebooks** directly in Colab, and **push the changes back to GitHub**.

### **Prerequisites**:
- You should have a **GitHub account**.
- You should have a **GitHub repository** containing the notebooks you want to edit.
- You should have **Google Colab** set up in your browser.

---

### **Workflow to Use Colab with GitHub**

#### **Step 1: Clone the GitHub Repository to Google Colab**

1. **Open Google Colab**:
   - Go to [Google Colab](https://colab.research.google.com/).

2. **Clone the GitHub Repository**:
   - If you want to work with an existing repository, you can **clone it directly in Colab**.
   - Open a new code cell and run the following command to clone the repository:

   ```bash
   !git clone https://github.com/92username/practice_python_repeat_a_lot.git
   ```

   - This will **clone** the repository from GitHub into the Google Colab environment.

3. **Navigate to the Repository Directory**:
   - After cloning the repository, you can **navigate to the directory** in Colab using the command:

   ```bash
   %cd practice_python_repeat_a_lot
   ```

#### **Step 2: Edit the Notebooks in Google Colab**

1. **Open the Notebook**:
   - In Colab, you can open the notebook directly from the cloned repository. If the repository contains a file like `Lista_exercicios_if_else.ipynb`, navigate to that file and **open it** in Colab to edit.

2. **Edit the Code**:
   - Make the necessary changes to your exercises. Google Colab allows you to edit, run, and save notebooks directly.

#### **Step 3: Save Changes to GitHub**

1. **Save a Copy to GitHub**:
   After editing the notebook, you can easily **save the changes to GitHub** directly from Colab. To do this:
   - Click on **File > Save a copy in GitHub**.
   - A window will appear where you can select:
     - The **repository** where you want to save the file.
     - The **branch** (usually `main` or `master`).
     - The **filename** (you can keep the default name or rename it).

   After this, the **notebook will be saved directly to GitHub** in the specified repository.

2. **Use Git Directly in Colab** (Optional):
   If you want more **manual control** over the **commit** and **push** process, you can use Git commands directly in Colab.

   **Set Up Git in Colab**:
   First, set your name and email for Git configuration (if you haven't already):

   ```bash
   !git config --global user.name "Your Name"
   !git config --global user.email "your-email@example.com"
   ```

   **Commit and Push the Changes**:
   After editing the notebook, use the following commands to **add**, **commit**, and **push** the changes back to your GitHub repository.

   ```bash
   # Navigate to the repository directory (if necessary)
   %cd practice_python_repeat_a_lot

   # Add the changes
   !git add .

   # Commit the changes
   !git commit -m "Updated notebook with new if-else exercises"

   # Push the changes to GitHub
   !git push origin main  # or the corresponding branch
   ```

   These commands will **send the edited notebook** back to your GitHub repository.

#### **Step 4: View Changes on GitHub**

After pushing the changes, go to your GitHub repository to **verify the changes**. You will be able to see the commit history and view the updated notebook directly in GitHub.

---

### **Summary Workflow:**

1. **Clone the repository** in Google Colab with the `git clone` command.
2. **Edit the notebook** in Colab as needed.
3. **Save the changes to GitHub**:
   - Use the **"Save a copy in GitHub"** option or,
   - Use **Git directly in Colab** to **commit and push**.
4. **Check GitHub** to verify that the changes have been saved correctly.

---

### **Important Tips:**

- **Public Repositories**: If your repository is public, anyone can access the content and use the notebooks. Ensure your repository is set up appropriately if you want others to benefit from or contribute to your content.
  
- **GitHub Credentials**: When using Git directly in Colab, you may need to authenticate with GitHub if you haven’t already configured your authentication credentials in Colab. You can use authentication tokens or your GitHub credentials.

---

### **Conclusion**:

This tutorial provides a **simple and efficient workflow** to integrate **Google Colab** with **GitHub**, allowing you to edit, save, and push your Python notebooks easily to your GitHub repository. This makes it easier for you to **store code**, **share with others**, and **version control** your practice exercises.

If you have any questions or need further details on setting something up, feel free to ask via issues! 😄
