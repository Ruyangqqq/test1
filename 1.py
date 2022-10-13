# Reading the file all at once
def readit_all(filename = "penguins.csv"):
  """
  Read and parse CSV -- read entire file all at once.
  """
  with open(filename, 'r') as file:
    mylist = file.read().rstrip().split("\n") # rstrip() is needed

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



z_label = "species"
species = set([d[z_label] for d in data])
colormap = {s: ['tab:blue', 'tab:orange', 'tab:green'][i] for i,s in enumerate(species)}

for d in data:
    if d[x_label] == "NA" or d[y_label] == "NA":
        continue

    color = colormap[d[z_label]]
    plt.scatter(float(d[x_label]), float(d[y_label]), color=color)

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()



def process(data, x = "bill_length_mm", y = "flipper_length_mm", z = "species"):
    """
    Extract 2 items/columns, remove missing data "NA" and cast strings to floats
    """
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

  # another way that does the same thing as 2 lines above
  X_subset = [d for i, d in enumerate(X) if s == Z[i]]
  Y_subset = [d for i, d in enumerate(Y) if s == Z[i]]

  plt.scatter(X_subset, Y_subset, label=s)

plt.legend()
plt.show()






