# O(n log n) O(1)

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=(fastest))
    total_speed = 0
    for r, b in zip(redShirtSpeeds, blueShirtSpeeds):
        total_speed += max(r, b)
    return total_speed
tandemBicycle(**{
  "redShirtSpeeds": [5, 5, 3, 9, 2],
  "blueShirtSpeeds": [3, 6, 7, 2, 1],
  "fastest": True
})