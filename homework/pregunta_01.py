import pandas as pd

def pregunta_01():
  
  def parse_lines(lines):
    rows = []
    current_row = []
    new_row = True

    for line in lines:
      line = line.strip()
      tokens = line.split()

      if tokens and new_row:
        current_row = [
          int(tokens[0]),
          int(tokens[1]),
          float(tokens[2].replace(',', '.')),
          " ".join(tokens[4:]),
        ]
        new_row = False
      elif tokens:
        current_row[-1] += " " + " ".join(tokens)
      else:
        current_row[-1] = current_row[-1].replace('.', '')
        rows.append(current_row)
        current_row = []
        new_row = True
    return rows

  with open("files/input/clusters_report.txt", 'r') as file:
    raw_lines = file.readlines()

  content_lines = raw_lines[4:]
  rows = parse_lines(content_lines)
  columns = [
    'cluster',
    'cantidad_de_palabras_clave',
    'porcentaje_de_palabras_clave',
    'principales_palabras_clave'
  ]
  return pd.DataFrame(rows, columns=columns)
