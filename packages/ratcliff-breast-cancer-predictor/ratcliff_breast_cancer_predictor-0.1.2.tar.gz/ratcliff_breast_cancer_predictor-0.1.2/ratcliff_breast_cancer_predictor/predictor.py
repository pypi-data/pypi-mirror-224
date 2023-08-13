import pandas as pd
import pickle
import pkg_resources
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def get_data_path():
    return pkg_resources.resource_filename(
        __name__, "resources/breast-cancer-wisconsin.data"
    )


def predict(model, values: list) -> str:
    prediction = model.predict(values)
    if prediction == 2:
        return "benign"
    else:
        return "malignant"


def train(modal_path: str, data_path: str | None) -> float:
    if data_path is None:
        data_path = get_data_path()

    df = pd.read_csv(data_path, header=None)
    df = df[(df != "?").all(axis=1)]
    cancer_data = df[[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    cancer_target = df[10]
    X_train, X_test, y_train, y_test = train_test_split(
        cancer_data, cancer_target, random_state=3
    )

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    pickle.dump(knn, open(modal_path, "wb"))
    return knn.score(X_test, y_test)
