from toposort import toposort_flatten
import os.path


def get_flattened(lines):
    graph = {}
    for l in lines:
        t = l.strip().replace('->', '')
        s = t.replace('  ', ' ')
        nodes = s.split(' ')
        if graph.get(nodes[0]) is None:
            graph[nodes[0]] = {nodes[1]}
        else:
            graph[nodes[0]].add(nodes[1])        
    return toposort_flatten(graph)


def load_file(fname):
    with open(fname) as f:
        lines = [l for l in f.readlines() if '->' in l]
        linesfilt = [l for l in lines if not 'NEFU' in l]
        g = get_flattened(lines)
#        print(g)
        gf = get_flattened(linesfilt)
#        print(gf)
        # note does not support empty lists
        return (g, gf, g == gf, g[0] == gf[0] and g[-1] == gf[-1])

        
def check_graphs():
#    files = [f for f in os.listdir('.') if (os.path.isfile(f) and '.dot' in f[-4:])]
#    for fname in files:


    for folder, subs, files in os.walk('.'):
        for filename in [f for f in  files if '.dot' in f[-4:]]:
            fname = os.path.join(folder, filename) 
            res = load_file(fname)
            print (fname, res[1], res[2])

if __name__ == "__main__":
    check_graphs()



