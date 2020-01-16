import matplotlib.pyplot as plt

class Plotter(object):
  """docstring for Plotter"""
  def __init__(self):
    super(Plotter, self).__init__()

  def plot_perf(self, perf):
    self.perf = perf

    keys = list(perf.history.keys())
    pairs = {}
    for name in keys:
      val_name = 'val_' + name
      if val_name in keys:
        pairs[name] = val_name
    all_keys = set(keys)
    paired_keys = set(list(pairs.keys()) + list(pairs.values()))
    single_keys = all_keys - paired_keys

    plots = []

    for name in single_keys:
      plots.append(self.plot_single(name))

    for name, val_name in pairs.items():
      plots.append(self.plot_pair(name, val_name))

    return plots
  
  def plot_pair(self, name, val_name):
    ys1 = self.perf.history[name]
    ys2 = self.perf.history[val_name]
    epochs = range(1, len(ys1) + 1)
    fig = plt.figure()
    plt.clf()
    plt.plot(epochs, ys1, 'b', label='training %s' % name)
    plt.plot(epochs, ys2, 'r', label='validation %s' % name)
    plt.xlabel('epochs/steps/episodes/t')
    plt.ylabel(name)
    plt.legend()
    plt.savefig('viz_%s.png' % name)
    plt.close()
    return fig

  def plot_single(self, name):
    ys = self.perf.history[name]
    epochs = range(1, len(ys) + 1)
    fig = plt.figure()
    plt.clf()
    plt.plot(epochs, ys, 'b', label='training %s' % name)
    plt.xlabel('epochs/steps/episodes/t')
    plt.ylabel(name)
    plt.legend()
    plt.savefig('viz_%s.png' % name)
    plt.close()
    return fig
