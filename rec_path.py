def rec_path(pred, origin, destiny):
  aux = destiny
  path = [destiny]
  while aux != origin:
    if pred[destiny] is None:
      return []
    aux = pred[aux]
    path.insert(0, aux)
  return path


def rec_path_floyd(pred, origin, destiny):
  path = [destiny]
  aux = destiny
  while aux != origin:
    if pred[origin][aux] is None:
      return []
    aux = pred[origin][aux]
    path.insert(0, aux)
  return path
