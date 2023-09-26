from argparse import ArgumentParser
from xai_components.base import SubGraphExecutor
from xai_components.xai_plotting.dist_plot import VisualizeNormalDistribution
from xai_components.xai_tensorflow_probability.normal_distribution import NormalDistribution
from xai_components.xai_utils.utils import Print

def main(args):
    ctx = {}
    ctx['args'] = args
    c_0 = VisualizeNormalDistribution()
    c_1 = NormalDistribution()
    c_2 = Print()
    c_0.samples = c_1.samples
    c_0.title.value = 'This is a plot'
    c_1.loc.value = 0.02
    c_1.scale.value = 1
    c_1.population.value = 100
    c_0.next = c_2
    c_1.next = None
    c_2.next = None
    next_component = c_1
    while next_component:
        next_component = next_component.do(ctx)
if __name__ == '__main__':
    parser = ArgumentParser()
    main(parser.parse_args())
    print('\nFinished Executing')