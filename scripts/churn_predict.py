import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/customer_churn.csv")

# Preprocess
df.dropna(inplace=True)
label = LabelEncoder()
df['Gender'] = label.fit_transform(df['Gender'])  # Male=1, Female=0
X = df.drop(['CustomerID', 'Churn'], axis=1)
y = df['Churn']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
