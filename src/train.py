import json
import subprocess
import joblib
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

def get_git_commit_sha():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
    except Exception:
        return "unknown"

def main():
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    seed = params["seed"]
    test_size = params["split"]["test_size"]
    n_estimators = params["train"]["n_estimators"]
    max_depth = params["train"]["max_depth"]

    df = pd.read_csv("data/raw/WineQT.csv")
    X = df.drop(columns=["quality", "Id"], errors="ignore")
    y = (df["quality"] >= 7).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=seed, stratify=y
    )

    clf = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=seed
    )
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    metrics = {
        "git_sha": get_git_commit_sha(),
        "accuracy": round(accuracy_score(y_test, y_pred), 4),
        "f1": round(f1_score(y_test, y_pred, average="binary"), 4)
    }

    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    joblib.dump(clf, "models/model.joblib")
    print(f"Training complete. Metrics: {metrics}")

if __name__ == "__main__":
    main()
