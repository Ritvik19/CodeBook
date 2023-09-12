def predict_label(examples, features, k, label_key="is_intrusive"):
    k_nearest_neighbors = find_k_nearest_neighbors(examples, features, k)
    k_nearest_neighbors_labels = [examples[pid][label_key] for pid in k_nearest_neighbors]
    return round(sum(k_nearest_neighbors_labels) / k)


def find_k_nearest_neighbors(examples, features, k):
    distances = {pid: euclidean_distance(features, features_label_map["features"]) for pid, features_label_map in examples.items()}
    return sorted(distances, key=distances.get)[:k]

def euclidean_distance(A, B):
    return sum([(a-b)**2 for a, b in zip(A, B)])**0.5