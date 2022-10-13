


def readit_all(filename = "penguins.csv"):
  with open(filename, 'r') as file:
    mylist = file.read().rstrip().split("\n")
  keys = mylist.pop(0).split(",")
  data = []
  for line in mylist:
    values = line.split(",")
    datum = {keys[i]: value for i, value in enumerate(values)}
    data.append(datum)

  return data


import matplotlib.pyplot as plt

data = readit_all()

x_label = "bill_length_mm"
y_label = "bill_depth_mm"

for datum in data:
  if datum[x_label] == "NA" or datum[y_label] == "NA":
    continue
  plt.scatter(float(datum[x_label]), float(datum[y_label]), c="steelblue")

data[0]


import matplotlib.pyplot as plt

data = readit_all()

x_label = "bill_length_mm"
y_label = "bill_depth_mm"

species_list=[dict_sub["species"] for dict_sub in data]
colors = ['blue', 'orange', 'green']
colormap = {s: colors[i] for i, s in enumerate(set(species_list))}



for datum in data:
  if datum[x_label] == "NA" or datum[y_label] == "NA":
    continue
  color = colormap[datum["species"]]
  plt.scatter(float(datum[x_label]), float(datum[y_label]), c=color)

data[0]
plt.legend(colormap)

def process(data, x = "bill_length_mm", y = "flipper_length_mm", z = "species"):
    bad_count = 0
    X = []
    Y = []
    Z = []
    for d in data:
      # Remove missing data
      if "NA" in [d[x], d[y], d[z]]:
          bad_count += 1
          print("Skipping NA --", bad_count, "lines skipped")
          continue
      
      # Convert strings to numbers for the quantitative variables
      X.append(float(d[x]))
      Y.append(float(d[y]))
      Z.append(d[z])

    return X, Y, Z


X, Y, Z = process(data)

for s in species:
  X_subset=[x_sub for x_sub,z_sub in zip(X,Z) if z_sub==s]
  Y_subset=[y_sub for y_sub,z_sub in zip(Y,Z) if z_sub==s]
  
  plt.scatter(X_subset, Y_subset, label=s)

plt.legend()
plt.show()


