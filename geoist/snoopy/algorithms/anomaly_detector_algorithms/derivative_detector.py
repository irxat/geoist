# coding=utf-8

import numpy

from geoist.snoopy import utils
from geoist.snoopy.algorithms.anomaly_detector_algorithms import AnomalyDetectorAlgorithm
from geoist.snoopy.constants import DEFAULT_DERI_SMOOTHING_FACTOR
from geoist.snoopy.modules.time_series import TimeSeries


class DerivativeDetector(AnomalyDetectorAlgorithm):

    '''
    Derivative Algorithm.
    This method is the derivative version of Method 1.
    Instead of data point value, it uses the derivative of the data point.
    '''
    def __init__(self, time_series, baseline_time_series=None, smoothing_factor=None):
        """
        Initializer
        :param TimeSeries time_series: a TimeSeries object.
        :param TimeSeries baseline_time_series: baseline TimeSeries.
        :param float smoothing_factor: smoothing factor.
        """
        super(DerivativeDetector, self).__init__(self.__class__.__name__, time_series, baseline_time_series)
        self.smoothing_factor = (smoothing_factor or DEFAULT_DERI_SMOOTHING_FACTOR)
        self.time_series_items = self.time_series.items()

    def _compute_derivatives(self):
        """
        Compute derivatives of the time series.
        """
        derivatives = []
        for i, (timestamp, value) in enumerate(self.time_series_items):
            if i > 0:
                pre_item = self.time_series_items[i - 1]
                pre_timestamp = pre_item[0]
                pre_value = pre_item[1]
                td = timestamp - pre_timestamp
                derivative = (value - pre_value) / td if td != 0 else value - pre_value
                derivative = abs(derivative)
                derivatives.append(derivative)
        # First timestamp is assigned the same derivative as the second timestamp.
        if derivatives:
            derivatives.insert(0, derivatives[0])
        self.derivatives = derivatives

    def _set_scores(self):
        """
        Compute anomaly scores for the time series.
        """
        anom_scores = {}
        self._compute_derivatives()
        derivatives_ema = utils.compute_ema(self.smoothing_factor, self.derivatives)
        for i, (timestamp, value) in enumerate(self.time_series_items):
            anom_scores[timestamp] = abs(self.derivatives[i] - derivatives_ema[i])
        stdev = numpy.std(list(anom_scores.values()))
        if stdev:
                for timestamp in anom_scores.keys():
                    anom_scores[timestamp] /= stdev
        self.anom_scores = TimeSeries(self._denoise_scores(anom_scores))
