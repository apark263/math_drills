#!/usr/bin/env python3

from absl import app
from absl import flags
from typing import List, Tuple
import numpy as np
from latex_format import typeset_problems


FLAGS = flags.FLAGS
flags.DEFINE_integer('count', 20, 'Number of questions to generate.')
flags.DEFINE_integer('low', 2, 'High value to use.')
flags.DEFINE_integer('high', 9, 'High value to use.')
flags.DEFINE_string('output', 'problems', 'File to output to.')


# TODO(alex): better sampling to avoid repeated pairs.
def make_questions(low: int, high: int, count: int) -> List[Tuple[int, int]]:
  arg_a = np.random.randint(low, high, count)
  arg_b = np.random.randint(low, high, count)
  return [(a, b) for a, b in zip(arg_a, arg_b)]


def main(argv):
  del argv    # Unused
  problems = make_questions(FLAGS.low, FLAGS.high, FLAGS.count)
  typeset_problems(FLAGS.output, problems)


if __name__ == '__main__':
  app.run(main)
