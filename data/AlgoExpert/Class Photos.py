# O(n log n) O(1)

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    red_blue = bool(redShirtHeights[0] < blueShirtHeights[0])
    for r, b in zip(redShirtHeights, blueShirtHeights):
        if red_blue:
            if r >= b:
                return False
        else:
            if b >= r:
                return False   
    return True


classPhotos(**{
  "redShirtHeights": [5, 8, 1, 3, 4],
  "blueShirtHeights": [6, 9, 2, 4, 5]
})
