import copy
from tarjan import tarjan, tc


def serialize(obj):
    if callable(obj):
        data = copy.copy(obj.__dict__)
        data['name'] = obj.__name__
    else:
        data = obj

    return data

def resolve(steps):
    """ Translate needs into dependencies. """

    dependencies = {}

    for this in steps:
        dependencies[this['name']] = this.get('dependencies', [])

        for that in steps:
            needs = set(that.get('provides', [])).intersection(this.get('needs', []))

            if len(needs):
                dependencies[this['name']].append(that['name'])

    return dependencies

def sort(items):
    descriptions = map(serialize, items)
    names = map(lambda item: item['name'], descriptions)
    resolved_descriptions = resolve(descriptions)
    topological_sort = tarjan(resolved_descriptions)
    flattened_sort = sum(topological_sort, [])

    def find(name):
        i = names.index(name)
        return items[i]

    return map(find, flattened_sort)
