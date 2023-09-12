class Metrics():
   def euclidean_distance(self, X, Y):
       return sum([(x-y)**2 for x, y in zip(X, Y)])**0.5

   def manhattan_distance(self, X, Y):
       return sum([abs(x-y) for x, y in zip(X, Y)])

   def cosine_similarity(self, X, Y):
       return sum([x*y for x, y in zip(X, Y)]) / (sum([x*x for x in X])**0.5 * sum([y*y for y in Y])**0.5)

   def jaccard_similarity(self, X, Y):
       return len(set(X) & set(Y)) / len(set(X) | set(Y))


def distances_and_similarities(X, Y):
   metrics = Metrics()
   return [metrics.euclidean_distance(X, Y),
           metrics.manhattan_distance(X, Y),
           metrics.cosine_similarity(X, Y),
           metrics.jaccard_similarity(X, Y)]
