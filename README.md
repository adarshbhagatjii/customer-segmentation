# 📊 Customer Segmentation Dashboard using K-Means

A **Machine Learning based Customer Segmentation Web App** built with **Python, Scikit-Learn, and Streamlit**.  
This application groups customers into different clusters based on their behavior such as **Annual Income** and **Spending Score**, helping businesses understand customer types and design targeted marketing strategies.

---

## 🚀 Project Overview

This project uses the **K-Means Clustering algorithm** to automatically segment customers from a dataset.  
Users can upload their own dataset, select features, and visualize customer clusters interactively.

### The dashboard provides:
- 📄 Data preview  
- 🎯 Feature selection  
- 🔍 Automatic cluster detection  
- 📈 Cluster insights and statistics  
- 🧠 PCA dimensionality reduction  
- 💾 Downloadable segmented dataset  

Customer segmentation helps companies identify groups such as **high-value customers, potential buyers, and budget customers**, enabling targeted marketing strategies.

---

## 🧠 Machine Learning Algorithm: K-Means Clustering

K-Means is an **unsupervised machine learning algorithm** used to group similar data points into clusters.

**Steps used in this project:**
1. Data preprocessing  
2. Feature scaling  
3. Elbow Method for optimal cluster selection  
4. K-Means clustering  
5. Cluster evaluation using Silhouette Score  
6. Visualization of clusters  

---

## 📂 Features

✅ Upload custom CSV dataset  
✅ Select features for clustering  
✅ Automatic preprocessing (encoding + scaling)  
✅ Elbow Method for optimal cluster detection  
✅ Silhouette Score for cluster evaluation  
✅ Interactive Plotly cluster visualization  
✅ Cluster distribution charts  
✅ Cluster insights and statistics  
✅ PCA visualization for high-dimensional data  
✅ Download clustered dataset  

---

## 🛠️ Technologies Used

| Technology   | Purpose                        |
|--------------|--------------------------------|
| Python       | Programming language           |
| Pandas       | Data manipulation              |
| Scikit-learn | Machine learning               |
| Streamlit    | Web application framework      |
| Plotly       | Interactive visualizations     |
| Kneed        | Optimal cluster detection      |
| PCA          | Dimensionality reduction       |

---

## 📊 Dataset Format

Your dataset should contain numerical features such as:

| Column              | Description                  |
|---------------------|------------------------------|
| Age                 | Customer age                 |
| Gender              | Customer gender              |
| Annual Income (k$)  | Customer income              |
| Spending Score (1-100) | Customer spending behavior |

**Example dataset:**

```csv
CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100)
1, Male, 19, 15, 39
2, Male, 21, 15, 81
3, Female, 20, 16, 6
```
# 📸 Application Workflow

1️⃣ Upload your dataset  
2️⃣ Select features for clustering  
3️⃣ Preprocess the data automatically  
4️⃣ Determine optimal clusters using the Elbow Method  
5️⃣ Perform K-Means clustering  
6️⃣ Visualize clusters using interactive plots  
7️⃣ Analyze cluster insights  
8️⃣ Download the clustered dataset  

---

# 📈 Visualizations Included

- 📉 Elbow Method Graph  
- 📊 Cluster Scatter Plot  
- 📦 Cluster Distribution Chart  
- 🧠 PCA Cluster Visualization  
- 📋 Cluster Insights Table  

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/customer-segmentation-dashboard.git
cd customer-segmentation-dashboard
```
Install dependencies:
``` 
pip install -r requirements.txt
```
## ▶️ Run the Application
Start the Streamlit app:
```
streamlit run app.py
```
- The app will open in your browser:
👉 http://localhost:8501

📁 Project Structure
```
Customer-Segmentation-Dashboard
│
├── app.py
├── image1.jpg
├── requirements.txt
├── README.md
└── sample_dataset.csv   
```

## 📥 Example Requirements.txt

- streamlit
- pandas
- scikit-learn
- plotly
- kneed


## 🌟 Future Improvements
- AI-generated marketing recommendations

- Customer persona generation

- Real-time dashboard analytics

- Integration with CRM systems

- Auto report generation

## 👨‍💻 Author
**Adarsh Bhagat** 
*Full Stack Developer | Machine Learning Enthusiast*

## ⭐ If you like this project, give it a star on GitHub and feel free to contribute!
``` 

Would you like me to add a **badges section** (Python version, Streamlit, License, etc.) at the very top so the README looks more professional and eye-catching?
```
