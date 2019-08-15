# MIT License
#
# Copyright (C) IBM Corporation 2018
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import unittest

import numpy as np

from art.classifiers import Classifier, ClassifierNeuralNetwork, ClassifierGradients
from art.utils import master_seed

logger = logging.getLogger('testLogger')


class ClassifierInstance(Classifier):
    def __init__(self):
        super(ClassifierInstance, self).__init__()

    def fit(self, x, y, **kwargs):
        pass

    def predict(self, x):
        pass

    def save(self, filename, path=None):
        pass


class ClassifierNeuralNetworkInstance(ClassifierNeuralNetwork, ClassifierGradients, Classifier):
    def __init__(self, clip_values, channel_index=1):
        super(ClassifierNeuralNetworkInstance, self).__init__(clip_values=clip_values, channel_index=channel_index)

    def class_gradient(self, x, label=None, **kwargs):
        pass

    def fit(self, x, y, batch_size=128, nb_epochs=20, **kwargs):
        pass

    def get_activations(self, x, layer, batch_size):
        pass

    def loss_gradient(self, x, y, **kwargs):
        pass

    def predict(self, x, batch_size=128, **kwargs):
        pass

    def save(self, filename, path=None):
        pass

    def layer_names(self):
        pass

    def set_learning_phase(self, train):
        pass


class TestClassifier(unittest.TestCase):
    def setUp(self):
        master_seed(1234)

    def test_preprocessing_normalisation(self):
        classifier = ClassifierInstance()

        x = np.random.rand(100, 200)
        new_x = classifier._apply_preprocessing_standardisation(x)
        self.assertEqual(np.sum(x - new_x), 0)

    def test_repr(self):
        classifier = ClassifierInstance()

        repr_ = repr(classifier)
        self.assertIn('ClassifierInstance', repr_)
        self.assertIn('clip_values=None', repr_)
        self.assertIn('defences=None', repr_)
        self.assertIn('preprocessing=None', repr_)


class TestClassifierNeuralNetwork(unittest.TestCase):
    def setUp(self):
        master_seed(1234)

    def test_preprocessing_normalisation(self):
        classifier = ClassifierNeuralNetworkInstance((0, 1))

        x = np.random.rand(100, 200)
        new_x = classifier._apply_preprocessing_standardisation(x)
        self.assertEqual(np.sum(x - new_x), 0)

    def test_repr(self):
        classifier = ClassifierNeuralNetworkInstance((0, 1))

        repr_ = repr(classifier)

        print(repr_)

        self.assertIn('ClassifierNeuralNetworkInstance', repr_)
        self.assertIn('channel_index=1', repr_)
        self.assertIn('clip_values=(0, 1)', repr_)
        self.assertIn('defences=None', repr_)
        self.assertIn('preprocessing=None', repr_)