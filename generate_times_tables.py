#!/usr/bin/env python3

from absl import app
from absl import flags
from typing import List, Tuple
import numpy as np
from latex_format import typeset_problems_vertical, typeset_problems_horizontal


FLAGS = flags.FLAGS
flags.DEFINE_integer('count', 20, 'Number of questions to generate.')
flags.DEFINE_integer('low', 2, 'High value to use.')
flags.DEFINE_integer('high', 9, 'High value to use.')
flags.DEFINE_string('output', 'problems', 'File to output to.')
flags.DEFINE_enum('layout', 'vertical', ['vertical', 'horizontal'], 'Whether to print vertical or horizontal.')


# TODO(alex): better sampling to avoid repeated pairs.
def make_questions(low: int, high: int, count: int) -> List[Tuple[int, int]]:
  arg_a = np.random.randint(low, high + 1, count)
  arg_b = np.random.randint(low, high + 1, count)
  return [(a, b) for a, b in zip(arg_a, arg_b)]


def main(argv):
  del argv    # Unused
  problems = make_questions(FLAGS.low, FLAGS.high, FLAGS.count)
  if FLAGS.layout == 'vertical':
    typeset_problems_vertical(FLAGS.output, problems)
  else:
    typeset_problems_horizontal(FLAGS.output, problems)


if __name__ == '__main__':
  app.run(main)
