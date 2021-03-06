from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from nixnet import _cconsts
from nixnet import _props
from nixnet import constants

from nixnet.db import _collection
from nixnet.db import _signal


class SubFrame(object):

    def __init__(self, handle):
        self._handle = handle
        self._dyn_signals = _collection.DbCollection(
            self._handle, constants.ObjectClass.SIGNAL, _cconsts.NX_PROP_SUBFRM_DYN_SIG_REFS, _signal.Signal)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return 'SubFrame(handle={0})'.format(self._handle)

    @property
    def config_status(self):
        return _props.get_subframe_config_status(self._handle)

    @property
    def dyn_signals(self):
        return self._dyn_signals

    @property
    def frm_ref(self):
        return _props.get_subframe_frm_ref(self._handle)

    @property
    def mux_value(self):
        return _props.get_subframe_mux_value(self._handle)

    @mux_value.setter
    def mux_value(self, value):
        _props.set_subframe_mux_value(self._handle, value)

    @property
    def name(self):
        return _props.get_subframe_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_subframe_name(self._handle, value)

    @property
    def pdu_ref(self):
        return _props.get_subframe_pdu_ref(self._handle)

    @property
    def name_unique_to_cluster(self):
        return _props.get_subframe_name_unique_to_cluster(self._handle)
