import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_excel("marketing_campaign_dataset.xlsx")

# ----------------------------
# Dataset Information
# ----------------------------
print("First 5 Rows:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistics:")
print(df.describe())

# ----------------------------
# Graph 1: Campaign Type Distribution
# ----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="Campaign_Type", data=df)
plt.title("Campaign Type Distribution")
plt.xlabel("Campaign Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# Graph 2: Marketing Channel Distribution
# ----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="Channel_Used", data=df)
plt.title("Marketing Channel Distribution")
plt.xlabel("Channel Used")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# Graph 3: Average ROI by Channel
# ----------------------------
plt.figure(figsize=(8,5))
roi = df.groupby("Channel_Used")["ROI"].mean()
roi.plot(kind="bar")
plt.title("Average ROI by Channel")
plt.xlabel("Channel")
plt.ylabel("Average ROI")
plt.tight_layout()
plt.show()

# ----------------------------
# Graph 4: Average Conversion Rate by Channel
# ----------------------------
plt.figure(figsize=(8,5))
conversion = df.groupby("Channel_Used")["Conversion_Rate"].mean()
conversion.plot(kind="bar")
plt.title("Average Conversion Rate by Channel")
plt.xlabel("Channel")
plt.ylabel("Conversion Rate")
plt.tight_layout()
plt.show()

# ----------------------------
# Graph 5: Clicks vs Impressions
# ----------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(x="Impressions", y="Clicks", data=df)
plt.title("Clicks vs Impressions")
plt.tight_layout()
plt.show()

# ----------------------------
# Graph 6: Customer Segment Distribution
# ----------------------------
plt.figure(figsize=(10,5))
sns.countplot(x="Customer_Segment", data=df)
plt.title("Customer Segment Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# Graph 7: Engagement Score Distribution
# ----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Engagement_Score"], bins=10, kde=True)
plt.title("Engagement Score Distribution")
plt.tight_layout()
plt.show()

# ----------------------------
# Graph 8: Acquisition Cost Distribution
# ----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Acquisition_Cost"], bins=20, kde=True)
plt.title("Acquisition Cost Distribution")
plt.tight_layout()
plt.show()

# ----------------------------
# Graph 9: Correlation Heatmap
# ----------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# ----------------------------
# Graph 10: ROI Distribution
# ----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["ROI"], bins=20, kde=True)
plt.title("ROI Distribution")
plt.tight_layout()
plt.show()


# ----------------------------
# Marketing Funnel
# ----------------------------

# Calculate total values
impressions = df["Impressions"].sum()
clicks = df["Clicks"].sum()

# Estimated conversions
conversions = (df["Clicks"] * df["Conversion_Rate"]).sum()

print("\nMarketing Funnel")
print("Impressions:", impressions)
print("Clicks:", clicks)
print("Conversions:", int(conversions))

# Funnel Chart
plt.figure(figsize=(7,5))

stages = ["Impressions","Clicks","Conversions"]
values = [impressions, clicks, conversions]

plt.bar(stages, values)

plt.title("Marketing Funnel")

plt.ylabel("Total Count")

plt.show()


print("\n----------- BUSINESS INSIGHTS -----------")

print("\nAverage ROI by Channel")
print(df.groupby("Channel_Used")["ROI"].mean())

print("\nAverage Conversion Rate by Channel")
print(df.groupby("Channel_Used")["Conversion_Rate"].mean())

print("\nAverage Acquisition Cost")
print(df.groupby("Channel_Used")["Acquisition_Cost"].mean())

print("\nTop Customer Segments")
print(df["Customer_Segment"].value_counts())

print("\nTop Campaign Types")
print(df["Campaign_Type"].value_counts())
