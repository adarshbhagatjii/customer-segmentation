
# ============================================
# IMPORT LIBRARIES
# ============================================

import pandas as pd
import streamlit as st
import plotly.express as px

from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

from kneed import KneeLocator


# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Segmentation using K-Means")

st.write(
    "Upload a dataset and automatically segment customers using **Machine Learning (K-Means Clustering)**."
)


# ============================================
# FILE UPLOAD
# ============================================

st.subheader("📂 Upload Dataset")

file = st.file_uploader("Upload CSV file", type=["csv"])

df = None

if file:
    df = pd.read_csv(file)
if st.button("Use Sample Dataset"):
    df=pd.read_csv("Mall_Customers_.csv")


# ============================================
# SIDEBAR
# ============================================

with st.sidebar:

    st.title("⚙️ Settings")

    st.image("image1.jpg")

    if df is not None:

        features = st.multiselect(
            "Select Features for Clustering",
            options=df.columns,
            default=["Annual Income (k$)", "Spending Score (1-100)"]
        )


# ============================================
# PREPROCESSING
# ============================================

def preprocessing(df):

    df = df.dropna()

    for col in df.columns:

        if df[col].dtype == "object":

            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])

    scaler = StandardScaler()

    scaled = scaler.fit_transform(df)

    return pd.DataFrame(scaled, columns=df.columns)


# ============================================
# ELBOW METHOD
# ============================================

def elbow_method(data):

    inertia = []

    k_values = range(1, 11)

    for k in k_values:

        model = KMeans(n_clusters=k, random_state=42)

        model.fit(data)

        inertia.append(model.inertia_)

    kl = KneeLocator(
        k_values,
        inertia,
        curve="convex",
        direction="decreasing"
    )

    elbow_df = pd.DataFrame({
        "K": k_values,
        "Inertia": inertia
    })

    st.subheader("📉 Elbow Method")

    st.line_chart(elbow_df, x="K", y="Inertia")

    return kl.elbow


# ============================================
# MAIN APP
# ============================================

if df is not None:

    if len(features) < 2:

        st.warning("Please select at least 2 features")

        st.stop()

    df = df.loc[:, features]

    st.subheader("🔍 Data Preview")

    st.dataframe(df.head())

    # preprocessing
    df_processed = preprocessing(df)


    # ============================================
    # FIND OPTIMAL K
    # ============================================

    k = elbow_method(df_processed)

    st.success(f"Optimal number of clusters: {k}")


    # ============================================
    # KMEANS MODEL
    # ============================================

    model = KMeans(n_clusters=k, random_state=42)

    model.fit(df_processed)

    labels = model.labels_

    df["Cluster"] = labels


    # ============================================
    # SILHOUETTE SCORE
    # ============================================

    score = silhouette_score(df_processed, labels)

    st.metric(
        "Silhouette Score",
        round(score, 3)
    )


    # ============================================
    # SCATTER PLOT
    # ============================================

    st.subheader("📊 Customer Segments Visualization")

    fig = px.scatter(
        df,
        x=df.columns[0],
        y=df.columns[1],
        color="Cluster",
        title="Customer Segmentation"
    )

    st.plotly_chart(fig, use_container_width=True)


    # ============================================
    # CLUSTER DISTRIBUTION
    # ============================================

    st.subheader("📦 Cluster Distribution")

    st.bar_chart(df["Cluster"].value_counts())


    # ============================================
    # CLUSTER INSIGHTS
    # ============================================

    # st.subheader("📊 Cluster Insights")

    # cluster_summary = df.groupby("Cluster").mean()

    # st.dataframe(cluster_summary)


    # ============================================
    # PCA VISUALIZATION
    # ============================================

    st.subheader("🧠 PCA Visualization")

    pca = PCA(n_components=2)

    pca_data = pca.fit_transform(df_processed)

    pca_df = pd.DataFrame(
        pca_data,
        columns=["PC1", "PC2"]
    )

    pca_df["Cluster"] = labels

    fig2 = px.scatter(
        pca_df,
        x="PC1",
        y="PC2",
        color="Cluster",
        title="PCA Cluster Visualization"
    )

    st.plotly_chart(fig2, use_container_width=True)


    # ============================================
    # DOWNLOAD DATA
    # ============================================

    st.subheader("⬇️ Download Results")

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Clustered Data",
        data=csv,
        file_name="customer_segments.csv",
        mime="text/csv"
    )
