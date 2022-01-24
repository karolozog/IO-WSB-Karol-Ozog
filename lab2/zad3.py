from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix

# odległość eukialidedowa
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Obliczanie dystansu pomiędzy punktem x a resztą zbioru treningowego
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Sortowanie wg. dystansu i zwracanie indeksu pierwszego k-sąsiada
        k_idx = np.argsort(distances)[: self.k]
        # Etykiety próbek szkoleniowych
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        # zwróć najczęściej otrzymywaną klasę
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]

if __name__ == "__main__":
    # Imports
    from matplotlib.colors import ListedColormap
    from sklearn import datasets
    from sklearn.model_selection import train_test_split

    # kolory na wykresie
    cmap = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])

    # dokładność
    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # podział na zbiory testowy i treningowy oraz na klasę numeryczną
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.67, random_state=1
    )

    # określanie ilości "najbliższych sąssiadów k= 3. Żeby otrzymać metodę k-NN dla 5 lub 11 sąsiadów za k podstawiamy kolejno 5 lub 11 "
    k = 11
    clf = KNN(k=k)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("Klasyfikacja KNN przy", k, "najbliższych sąsiadach wynosi: ", accuracy(y_test, predictions), "%")

    # macierz błędu
    cf = confusion_matrix(y_test, predictions)
    print("macierz błędu to:")
    print(cf)

    # wykres
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap, edgecolor="k", s=20)
    # oś x
    plt.xlabel('długość ')
    # oś y
    plt.ylabel('szerokość')
    # tytuł
    plt.title('Klasyfikacja KNN Irysów')
    plt.show()


    # macierz błędu
    cf = confusion_matrix(y_test, predictions)
    print("macierz błędu to:")
    print(cf)

    #wykres
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap, edgecolor="k", s=20)
    # oś x
    plt.xlabel('wysokość')
    # oś y
    plt.ylabel('szerokość')
    # tytuł
    plt.title('Klasyfikacja KNN Irysów')
    plt.show()


