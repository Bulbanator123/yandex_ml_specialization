import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("penguins.csv")

data = data.dropna()

labels = data["species"]
features = data[["bill_length_mm", "bill_depth_mm"]]

train_features, test_features, train_labels, test_labels = train_test_split( 
            features, labels, test_size=0.2, random_state=123)

best_accuracy = -2e9
worst_accuracy = 2e9

for k in range(1, 11):
    for weights in ["uniform", "distance"]:
        model = KNeighborsClassifier(n_neighbors=k, weights=weights)
        model.fit(train_features, train_labels)

        preds = model.predict(test_features)
        acc = accuracy_score(test_labels, preds)

        best_accuracy = max(best_accuracy, acc)
        worst_accuracy = min(worst_accuracy, acc)

print(f"Best accuracy: {best_accuracy:.6f}")
print(f"Worst accuracy: {worst_accuracy:.6f}")
