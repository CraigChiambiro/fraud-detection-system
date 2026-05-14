import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("data/creditcard.csv")

print("\n=== DATA OVERVIEW ===")
print(df.head())

print("\n=== DATA SHAPE ===")
print(df.shape)

print("\n=== TARGET DISTRIBUTION ===")
print(df["Class"].value_counts())

# =========================
# FEATURES / TARGET
# =========================
X = df.drop("Class", axis=1)

y = df["Class"]

# =========================
# TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# MODEL
# =========================
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=8,
    class_weight="balanced",
    random_state=42
)

# =========================
# TRAIN
# =========================
model.fit(X_train, y_train)

# =========================
# PREDICT
# =========================
y_pred = model.predict(X_test)

# =========================
# EVALUATION
# =========================
accuracy = accuracy_score(y_test, y_pred)

print("\n====================")
print("MODEL ACCURACY:", round(accuracy, 4))
print("====================\n")

print("\n=== CONFUSION MATRIX ===")
print(confusion_matrix(y_test, y_pred))

print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred))

# =========================
# SAVE MODEL
# =========================
joblib.dump(model, "models/model.pkl")

joblib.dump(X.columns.tolist(), "models/features.pkl")

print("\nModel saved successfully!")
print("Features saved successfully!")