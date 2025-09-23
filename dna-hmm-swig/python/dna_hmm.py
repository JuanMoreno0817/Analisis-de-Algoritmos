from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _dna_hmm
else:
    import _dna_hmm

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _dna_hmm.delete_SwigPyIterator

    def value(self):
        return _dna_hmm.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _dna_hmm.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _dna_hmm.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _dna_hmm.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _dna_hmm.SwigPyIterator_equal(self, x)

    def copy(self):
        return _dna_hmm.SwigPyIterator_copy(self)

    def next(self):
        return _dna_hmm.SwigPyIterator_next(self)

    def __next__(self):
        return _dna_hmm.SwigPyIterator___next__(self)

    def previous(self):
        return _dna_hmm.SwigPyIterator_previous(self)

    def advance(self, n):
        return _dna_hmm.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _dna_hmm.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _dna_hmm.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _dna_hmm.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _dna_hmm.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _dna_hmm.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _dna_hmm.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _dna_hmm:
_dna_hmm.SwigPyIterator_swigregister(SwigPyIterator)
class HMM(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    N = property(_dna_hmm.HMM_N_get, _dna_hmm.HMM_N_set)
    M = property(_dna_hmm.HMM_M_get, _dna_hmm.HMM_M_set)
    pi = property(_dna_hmm.HMM_pi_get, _dna_hmm.HMM_pi_set)
    A = property(_dna_hmm.HMM_A_get, _dna_hmm.HMM_A_set)
    B = property(_dna_hmm.HMM_B_get, _dna_hmm.HMM_B_set)

    def __init__(self):
        _dna_hmm.HMM_swiginit(self, _dna_hmm.new_HMM())
    __swig_destroy__ = _dna_hmm.delete_HMM

# Register HMM in _dna_hmm:
_dna_hmm.HMM_swigregister(HMM)
class ViterbiResult(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    path = property(_dna_hmm.ViterbiResult_path_get, _dna_hmm.ViterbiResult_path_set)
    logp = property(_dna_hmm.ViterbiResult_logp_get, _dna_hmm.ViterbiResult_logp_set)

    def __init__(self):
        _dna_hmm.ViterbiResult_swiginit(self, _dna_hmm.new_ViterbiResult())
    __swig_destroy__ = _dna_hmm.delete_ViterbiResult

# Register ViterbiResult in _dna_hmm:
_dna_hmm.ViterbiResult_swigregister(ViterbiResult)

def forward_log_prob(seq, pi, A, B):
    return _dna_hmm.forward_log_prob(seq, pi, A, B)

def viterbi_decode(seq, pi, A, B):
    return _dna_hmm.viterbi_decode(seq, pi, A, B)

def hmm_evaluate_logp(seq, pi, A, B):
    return _dna_hmm.hmm_evaluate_logp(seq, pi, A, B)

def hmm_recognize_states(seq, pi, A, B):
    return _dna_hmm.hmm_recognize_states(seq, pi, A, B)
class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _dna_hmm.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _dna_hmm.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _dna_hmm.DoubleVector___bool__(self)

    def __len__(self):
        return _dna_hmm.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _dna_hmm.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _dna_hmm.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _dna_hmm.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _dna_hmm.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _dna_hmm.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _dna_hmm.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _dna_hmm.DoubleVector_pop(self)

    def append(self, x):
        return _dna_hmm.DoubleVector_append(self, x)

    def empty(self):
        return _dna_hmm.DoubleVector_empty(self)

    def size(self):
        return _dna_hmm.DoubleVector_size(self)

    def swap(self, v):
        return _dna_hmm.DoubleVector_swap(self, v)

    def begin(self):
        return _dna_hmm.DoubleVector_begin(self)

    def end(self):
        return _dna_hmm.DoubleVector_end(self)

    def rbegin(self):
        return _dna_hmm.DoubleVector_rbegin(self)

    def rend(self):
        return _dna_hmm.DoubleVector_rend(self)

    def clear(self):
        return _dna_hmm.DoubleVector_clear(self)

    def get_allocator(self):
        return _dna_hmm.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _dna_hmm.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _dna_hmm.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _dna_hmm.DoubleVector_swiginit(self, _dna_hmm.new_DoubleVector(*args))

    def push_back(self, x):
        return _dna_hmm.DoubleVector_push_back(self, x)

    def front(self):
        return _dna_hmm.DoubleVector_front(self)

    def back(self):
        return _dna_hmm.DoubleVector_back(self)

    def assign(self, n, x):
        return _dna_hmm.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _dna_hmm.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _dna_hmm.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _dna_hmm.DoubleVector_reserve(self, n)

    def capacity(self):
        return _dna_hmm.DoubleVector_capacity(self)
    __swig_destroy__ = _dna_hmm.delete_DoubleVector

# Register DoubleVector in _dna_hmm:
_dna_hmm.DoubleVector_swigregister(DoubleVector)
class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _dna_hmm.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _dna_hmm.IntVector___nonzero__(self)

    def __bool__(self):
        return _dna_hmm.IntVector___bool__(self)

    def __len__(self):
        return _dna_hmm.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _dna_hmm.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _dna_hmm.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _dna_hmm.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _dna_hmm.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _dna_hmm.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _dna_hmm.IntVector___setitem__(self, *args)

    def pop(self):
        return _dna_hmm.IntVector_pop(self)

    def append(self, x):
        return _dna_hmm.IntVector_append(self, x)

    def empty(self):
        return _dna_hmm.IntVector_empty(self)

    def size(self):
        return _dna_hmm.IntVector_size(self)

    def swap(self, v):
        return _dna_hmm.IntVector_swap(self, v)

    def begin(self):
        return _dna_hmm.IntVector_begin(self)

    def end(self):
        return _dna_hmm.IntVector_end(self)

    def rbegin(self):
        return _dna_hmm.IntVector_rbegin(self)

    def rend(self):
        return _dna_hmm.IntVector_rend(self)

    def clear(self):
        return _dna_hmm.IntVector_clear(self)

    def get_allocator(self):
        return _dna_hmm.IntVector_get_allocator(self)

    def pop_back(self):
        return _dna_hmm.IntVector_pop_back(self)

    def erase(self, *args):
        return _dna_hmm.IntVector_erase(self, *args)

    def __init__(self, *args):
        _dna_hmm.IntVector_swiginit(self, _dna_hmm.new_IntVector(*args))

    def push_back(self, x):
        return _dna_hmm.IntVector_push_back(self, x)

    def front(self):
        return _dna_hmm.IntVector_front(self)

    def back(self):
        return _dna_hmm.IntVector_back(self)

    def assign(self, n, x):
        return _dna_hmm.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _dna_hmm.IntVector_resize(self, *args)

    def insert(self, *args):
        return _dna_hmm.IntVector_insert(self, *args)

    def reserve(self, n):
        return _dna_hmm.IntVector_reserve(self, n)

    def capacity(self):
        return _dna_hmm.IntVector_capacity(self)
    __swig_destroy__ = _dna_hmm.delete_IntVector

# Register IntVector in _dna_hmm:
_dna_hmm.IntVector_swigregister(IntVector)
class DoubleVector2D(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _dna_hmm.DoubleVector2D_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _dna_hmm.DoubleVector2D___nonzero__(self)

    def __bool__(self):
        return _dna_hmm.DoubleVector2D___bool__(self)

    def __len__(self):
        return _dna_hmm.DoubleVector2D___len__(self)

    def __getslice__(self, i, j):
        return _dna_hmm.DoubleVector2D___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _dna_hmm.DoubleVector2D___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _dna_hmm.DoubleVector2D___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _dna_hmm.DoubleVector2D___delitem__(self, *args)

    def __getitem__(self, *args):
        return _dna_hmm.DoubleVector2D___getitem__(self, *args)

    def __setitem__(self, *args):
        return _dna_hmm.DoubleVector2D___setitem__(self, *args)

    def pop(self):
        return _dna_hmm.DoubleVector2D_pop(self)

    def append(self, x):
        return _dna_hmm.DoubleVector2D_append(self, x)

    def empty(self):
        return _dna_hmm.DoubleVector2D_empty(self)

    def size(self):
        return _dna_hmm.DoubleVector2D_size(self)

    def swap(self, v):
        return _dna_hmm.DoubleVector2D_swap(self, v)

    def begin(self):
        return _dna_hmm.DoubleVector2D_begin(self)

    def end(self):
        return _dna_hmm.DoubleVector2D_end(self)

    def rbegin(self):
        return _dna_hmm.DoubleVector2D_rbegin(self)

    def rend(self):
        return _dna_hmm.DoubleVector2D_rend(self)

    def clear(self):
        return _dna_hmm.DoubleVector2D_clear(self)

    def get_allocator(self):
        return _dna_hmm.DoubleVector2D_get_allocator(self)

    def pop_back(self):
        return _dna_hmm.DoubleVector2D_pop_back(self)

    def erase(self, *args):
        return _dna_hmm.DoubleVector2D_erase(self, *args)

    def __init__(self, *args):
        _dna_hmm.DoubleVector2D_swiginit(self, _dna_hmm.new_DoubleVector2D(*args))

    def push_back(self, x):
        return _dna_hmm.DoubleVector2D_push_back(self, x)

    def front(self):
        return _dna_hmm.DoubleVector2D_front(self)

    def back(self):
        return _dna_hmm.DoubleVector2D_back(self)

    def assign(self, n, x):
        return _dna_hmm.DoubleVector2D_assign(self, n, x)

    def resize(self, *args):
        return _dna_hmm.DoubleVector2D_resize(self, *args)

    def insert(self, *args):
        return _dna_hmm.DoubleVector2D_insert(self, *args)

    def reserve(self, n):
        return _dna_hmm.DoubleVector2D_reserve(self, n)

    def capacity(self):
        return _dna_hmm.DoubleVector2D_capacity(self)
    __swig_destroy__ = _dna_hmm.delete_DoubleVector2D

# Register DoubleVector2D in _dna_hmm:
_dna_hmm.DoubleVector2D_swigregister(DoubleVector2D)

