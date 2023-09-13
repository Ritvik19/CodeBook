class TreeNode:
    def __init__(self, examples):
        self.examples = examples
        self.left = None
        self.right = None
        self.split_point = None

    def split(self):
        if len(self.examples) == 1:
            return

        best_split_point = {
            "feature": None,
            "value": None,
            "mse": float("inf"),
            "split_index": None,
        }

        for feature in self.examples[0].keys():
            if feature == "bpd":
                continue

            self.examples.sort(key=lambda example: example[feature])

            for i, _ in enumerate(self.examples[:-1]):
                split_point_value = (self.examples[i][feature] + self.examples[i + 1][feature]) / 2
                mse, split_index = self.get_split_point_mse(feature, split_point_value)
                if best_split_point["mse"] > mse:
                    best_split_point = {
                        "feature": feature,
                        "value": split_point_value,
                        "mse": mse,
                        "split_index": split_index,
                    }

        self.split_point = best_split_point

        self.examples.sort(key=lambda example: example[self.split_point["feature"]])

        self.left = TreeNode(self.examples[: self.split_point["split_index"]])
        self.left.split()

        self.right = TreeNode(self.examples[self.split_point["split_index"] :])
        self.right.split()

    def get_split_point_mse(self, feature, split_point_value):
        left_split_labels = [example["bpd"] for example in self.examples if example[feature] <= split_point_value]
        right_split_labels = [example["bpd"] for example in self.examples if example[feature] > split_point_value]

        if not len(left_split_labels) or not len(right_split_labels):
            return None, None

        left_split_mse = get_mse(left_split_labels)
        right_split_mse = get_mse(right_split_labels)
        num_samples = len(left_split_labels) + len(right_split_labels)
        mse = ((len(left_split_labels) * left_split_mse) + (len(right_split_labels) * right_split_mse)) / num_samples
        split_index = len(left_split_labels)

        return mse, split_index


def get_mse(values):
    average = get_average(values)
    return sum([(value - average) ** 2 for value in values]) / len(values)


def get_average(values):
    return sum(values) / len(values)


class RegressionTree:
    def __init__(self, examples):
        self.root = TreeNode(examples)
        self.train()

    def train(self):
        self.root.split()

    def predict(self, example):
        node = self.root

        while node.left and node.right:
            if example[node.split_point["feature"]] <= node.split_point["value"]:
                node = node.left
            else:
                node = node.right

        leaf_labels = [leaf_example["bpd"] for leaf_example in node.examples]
        return sum(leaf_labels) / len(leaf_labels)
