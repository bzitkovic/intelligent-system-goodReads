from pandas.core.frame import DataFrame
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import KFold, cross_val_score

feature_columns = ["rating_new", "pages_new", "reviews_new"]


def make_decision_tree(dataframe: DataFrame):
    arrange_data(dataframe)

    X = dataframe[feature_columns]  # Features
    y = dataframe["totalratings_new"]  # Target variable

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1
    )  # 70% training and 30% test

    # Do the cross-validation
    decision_tree_cross_validation(X_train, y_train)

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(max_depth=3)

    # Train Decision Tree Classifer
    clf = clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

    return clf


def make_prediction_total_rating(clf: DecisionTreeClassifier, dataframe: DataFrame):
    return clf.predict(dataframe[feature_columns])


def decision_tree_cross_validation(X: list, y: list):
    max_depth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    cnt = 1
    # Split the dataset into 5 folds
    for train_index, test_index in kf.split(X, y):
        print(f"Fold:{cnt}, Train set: {len(train_index)}, Test set:{len(test_index)}")
        cnt += 1

    # Calculate the accuracy for each fold and overall accuracy
    score = cross_val_score(DecisionTreeClassifier(random_state=42), X, y, cv=kf, scoring="accuracy")
    print(f"Scores for each fold are: {score}")
    print(f'Average score: {"{:.2f}".format(score.mean())}')

    # Calculate the average score for chosing max depth
    for val in max_depth:
        score = cross_val_score(DecisionTreeClassifier(max_depth=val, random_state=42), X, y, cv=kf, scoring="accuracy")
        print(f'Average score({val}): {"{:.3f}".format(score.mean())}')


def arrange_data(dataframe: DataFrame):
    dataframe["rating_new"] = dataframe["rating"]
    dataframe.loc[(dataframe["rating"] <= 1), "rating_new"] = 1
    dataframe.loc[(dataframe["rating"] > 1) & (dataframe["rating"] <= 2), "rating_new"] = 2
    dataframe.loc[(dataframe["rating"] > 2) & (dataframe["rating"] <= 3), "rating_new"] = 3
    dataframe.loc[(dataframe["rating"] > 3) & (dataframe["rating"] <= 4), "rating_new"] = 4
    dataframe.loc[(dataframe["rating"] > 4), "rating_new"] = 5

    dataframe["pages_new"] = dataframe["pages"]
    dataframe.loc[(dataframe["pages"] <= 50), "pages_new"] = 0
    dataframe.loc[(dataframe["pages"] > 50) & (dataframe["pages"] <= 300), "pages_new"] = 1
    dataframe.loc[(dataframe["pages"] > 300), "pages_new"] = 2

    dataframe["reviews_new"] = dataframe["reviews"]
    dataframe.loc[(dataframe["reviews"] <= 50), "reviews_new"] = 0
    dataframe.loc[(dataframe["reviews"] > 50) & (dataframe["reviews"] <= 200), "reviews_new"] = 1
    dataframe.loc[(dataframe["reviews"] > 200), "reviews_new"] = 2

    dataframe["totalratings_new"] = dataframe["totalratings"]
    dataframe.loc[(dataframe["totalratings"] <= 1500), "totalratings_new"] = 0
    dataframe.loc[(dataframe["totalratings"] > 1500) & (dataframe["totalratings"] <= 8000), "totalratings_new"] = 1
    dataframe.loc[(dataframe["totalratings"] > 8000), "totalratings_new"] = 2
