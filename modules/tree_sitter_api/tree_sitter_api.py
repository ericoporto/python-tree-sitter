# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_tree_sitter_api')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_tree_sitter_api')
    _tree_sitter_api = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_tree_sitter_api', [dirname(__file__)])
        except ImportError:
            import _tree_sitter_api
            return _tree_sitter_api
        try:
            _mod = imp.load_module('_tree_sitter_api', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _tree_sitter_api = swig_import_helper()
    del swig_import_helper
else:
    import _tree_sitter_api
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

TREE_SITTER_LANGUAGE_VERSION = _tree_sitter_api.TREE_SITTER_LANGUAGE_VERSION
TSInputEncodingUTF8 = _tree_sitter_api.TSInputEncodingUTF8
TSInputEncodingUTF16 = _tree_sitter_api.TSInputEncodingUTF16
TSSymbolTypeRegular = _tree_sitter_api.TSSymbolTypeRegular
TSSymbolTypeAnonymous = _tree_sitter_api.TSSymbolTypeAnonymous
TSSymbolTypeAuxiliary = _tree_sitter_api.TSSymbolTypeAuxiliary
class TSPoint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSPoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSPoint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["row"] = _tree_sitter_api.TSPoint_row_set
    __swig_getmethods__["row"] = _tree_sitter_api.TSPoint_row_get
    if _newclass:
        row = _swig_property(_tree_sitter_api.TSPoint_row_get, _tree_sitter_api.TSPoint_row_set)
    __swig_setmethods__["column"] = _tree_sitter_api.TSPoint_column_set
    __swig_getmethods__["column"] = _tree_sitter_api.TSPoint_column_get
    if _newclass:
        column = _swig_property(_tree_sitter_api.TSPoint_column_get, _tree_sitter_api.TSPoint_column_set)

    def __init__(self):
        this = _tree_sitter_api.new_TSPoint()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_TSPoint
    __del__ = lambda self: None
TSPoint_swigregister = _tree_sitter_api.TSPoint_swigregister
TSPoint_swigregister(TSPoint)

class TSRange(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSRange, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSRange, name)
    __repr__ = _swig_repr
    __swig_setmethods__["start_point"] = _tree_sitter_api.TSRange_start_point_set
    __swig_getmethods__["start_point"] = _tree_sitter_api.TSRange_start_point_get
    if _newclass:
        start_point = _swig_property(_tree_sitter_api.TSRange_start_point_get, _tree_sitter_api.TSRange_start_point_set)
    __swig_setmethods__["end_point"] = _tree_sitter_api.TSRange_end_point_set
    __swig_getmethods__["end_point"] = _tree_sitter_api.TSRange_end_point_get
    if _newclass:
        end_point = _swig_property(_tree_sitter_api.TSRange_end_point_get, _tree_sitter_api.TSRange_end_point_set)
    __swig_setmethods__["start_byte"] = _tree_sitter_api.TSRange_start_byte_set
    __swig_getmethods__["start_byte"] = _tree_sitter_api.TSRange_start_byte_get
    if _newclass:
        start_byte = _swig_property(_tree_sitter_api.TSRange_start_byte_get, _tree_sitter_api.TSRange_start_byte_set)
    __swig_setmethods__["end_byte"] = _tree_sitter_api.TSRange_end_byte_set
    __swig_getmethods__["end_byte"] = _tree_sitter_api.TSRange_end_byte_get
    if _newclass:
        end_byte = _swig_property(_tree_sitter_api.TSRange_end_byte_get, _tree_sitter_api.TSRange_end_byte_set)

    def __init__(self):
        this = _tree_sitter_api.new_TSRange()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_TSRange
    __del__ = lambda self: None
TSRange_swigregister = _tree_sitter_api.TSRange_swigregister
TSRange_swigregister(TSRange)

class TSInput(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSInput, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSInput, name)
    __repr__ = _swig_repr
    __swig_setmethods__["payload"] = _tree_sitter_api.TSInput_payload_set
    __swig_getmethods__["payload"] = _tree_sitter_api.TSInput_payload_get
    if _newclass:
        payload = _swig_property(_tree_sitter_api.TSInput_payload_get, _tree_sitter_api.TSInput_payload_set)
    __swig_setmethods__["read"] = _tree_sitter_api.TSInput_read_set
    __swig_getmethods__["read"] = _tree_sitter_api.TSInput_read_get
    if _newclass:
        read = _swig_property(_tree_sitter_api.TSInput_read_get, _tree_sitter_api.TSInput_read_set)
    __swig_setmethods__["encoding"] = _tree_sitter_api.TSInput_encoding_set
    __swig_getmethods__["encoding"] = _tree_sitter_api.TSInput_encoding_get
    if _newclass:
        encoding = _swig_property(_tree_sitter_api.TSInput_encoding_get, _tree_sitter_api.TSInput_encoding_set)

    def __init__(self):
        this = _tree_sitter_api.new_TSInput()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_TSInput
    __del__ = lambda self: None
TSInput_swigregister = _tree_sitter_api.TSInput_swigregister
TSInput_swigregister(TSInput)

TSLogTypeParse = _tree_sitter_api.TSLogTypeParse
TSLogTypeLex = _tree_sitter_api.TSLogTypeLex
class TSLogger(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSLogger, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSLogger, name)
    __repr__ = _swig_repr
    __swig_setmethods__["payload"] = _tree_sitter_api.TSLogger_payload_set
    __swig_getmethods__["payload"] = _tree_sitter_api.TSLogger_payload_get
    if _newclass:
        payload = _swig_property(_tree_sitter_api.TSLogger_payload_get, _tree_sitter_api.TSLogger_payload_set)
    __swig_setmethods__["log"] = _tree_sitter_api.TSLogger_log_set
    __swig_getmethods__["log"] = _tree_sitter_api.TSLogger_log_get
    if _newclass:
        log = _swig_property(_tree_sitter_api.TSLogger_log_get, _tree_sitter_api.TSLogger_log_set)

    def __init__(self):
        this = _tree_sitter_api.new_TSLogger()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_TSLogger
    __del__ = lambda self: None
TSLogger_swigregister = _tree_sitter_api.TSLogger_swigregister
TSLogger_swigregister(TSLogger)

class TSInputEdit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSInputEdit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSInputEdit, name)
    __repr__ = _swig_repr
    __swig_setmethods__["start_byte"] = _tree_sitter_api.TSInputEdit_start_byte_set
    __swig_getmethods__["start_byte"] = _tree_sitter_api.TSInputEdit_start_byte_get
    if _newclass:
        start_byte = _swig_property(_tree_sitter_api.TSInputEdit_start_byte_get, _tree_sitter_api.TSInputEdit_start_byte_set)
    __swig_setmethods__["old_end_byte"] = _tree_sitter_api.TSInputEdit_old_end_byte_set
    __swig_getmethods__["old_end_byte"] = _tree_sitter_api.TSInputEdit_old_end_byte_get
    if _newclass:
        old_end_byte = _swig_property(_tree_sitter_api.TSInputEdit_old_end_byte_get, _tree_sitter_api.TSInputEdit_old_end_byte_set)
    __swig_setmethods__["new_end_byte"] = _tree_sitter_api.TSInputEdit_new_end_byte_set
    __swig_getmethods__["new_end_byte"] = _tree_sitter_api.TSInputEdit_new_end_byte_get
    if _newclass:
        new_end_byte = _swig_property(_tree_sitter_api.TSInputEdit_new_end_byte_get, _tree_sitter_api.TSInputEdit_new_end_byte_set)
    __swig_setmethods__["start_point"] = _tree_sitter_api.TSInputEdit_start_point_set
    __swig_getmethods__["start_point"] = _tree_sitter_api.TSInputEdit_start_point_get
    if _newclass:
        start_point = _swig_property(_tree_sitter_api.TSInputEdit_start_point_get, _tree_sitter_api.TSInputEdit_start_point_set)
    __swig_setmethods__["old_end_point"] = _tree_sitter_api.TSInputEdit_old_end_point_set
    __swig_getmethods__["old_end_point"] = _tree_sitter_api.TSInputEdit_old_end_point_get
    if _newclass:
        old_end_point = _swig_property(_tree_sitter_api.TSInputEdit_old_end_point_get, _tree_sitter_api.TSInputEdit_old_end_point_set)
    __swig_setmethods__["new_end_point"] = _tree_sitter_api.TSInputEdit_new_end_point_set
    __swig_getmethods__["new_end_point"] = _tree_sitter_api.TSInputEdit_new_end_point_get
    if _newclass:
        new_end_point = _swig_property(_tree_sitter_api.TSInputEdit_new_end_point_get, _tree_sitter_api.TSInputEdit_new_end_point_set)

    def __init__(self):
        this = _tree_sitter_api.new_TSInputEdit()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_TSInputEdit
    __del__ = lambda self: None
TSInputEdit_swigregister = _tree_sitter_api.TSInputEdit_swigregister
TSInputEdit_swigregister(TSInputEdit)

class TSNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["context"] = _tree_sitter_api.TSNode_context_set
    __swig_getmethods__["context"] = _tree_sitter_api.TSNode_context_get
    if _newclass:
        context = _swig_property(_tree_sitter_api.TSNode_context_get, _tree_sitter_api.TSNode_context_set)
    __swig_setmethods__["id"] = _tree_sitter_api.TSNode_id_set
    __swig_getmethods__["id"] = _tree_sitter_api.TSNode_id_get
    if _newclass:
        id = _swig_property(_tree_sitter_api.TSNode_id_get, _tree_sitter_api.TSNode_id_set)
    __swig_setmethods__["tree"] = _tree_sitter_api.TSNode_tree_set
    __swig_getmethods__["tree"] = _tree_sitter_api.TSNode_tree_get
    if _newclass:
        tree = _swig_property(_tree_sitter_api.TSNode_tree_get, _tree_sitter_api.TSNode_tree_set)

    def __init__(self):
        this = _tree_sitter_api.new_TSNode()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_TSNode
    __del__ = lambda self: None
TSNode_swigregister = _tree_sitter_api.TSNode_swigregister
TSNode_swigregister(TSNode)

class TSTreeCursor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSTreeCursor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSTreeCursor, name)
    __repr__ = _swig_repr
    __swig_setmethods__["tree"] = _tree_sitter_api.TSTreeCursor_tree_set
    __swig_getmethods__["tree"] = _tree_sitter_api.TSTreeCursor_tree_get
    if _newclass:
        tree = _swig_property(_tree_sitter_api.TSTreeCursor_tree_get, _tree_sitter_api.TSTreeCursor_tree_set)
    __swig_setmethods__["id"] = _tree_sitter_api.TSTreeCursor_id_set
    __swig_getmethods__["id"] = _tree_sitter_api.TSTreeCursor_id_get
    if _newclass:
        id = _swig_property(_tree_sitter_api.TSTreeCursor_id_get, _tree_sitter_api.TSTreeCursor_id_set)
    __swig_setmethods__["context"] = _tree_sitter_api.TSTreeCursor_context_set
    __swig_getmethods__["context"] = _tree_sitter_api.TSTreeCursor_context_get
    if _newclass:
        context = _swig_property(_tree_sitter_api.TSTreeCursor_context_get, _tree_sitter_api.TSTreeCursor_context_set)

    def __init__(self):
        this = _tree_sitter_api.new_TSTreeCursor()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_TSTreeCursor
    __del__ = lambda self: None
TSTreeCursor_swigregister = _tree_sitter_api.TSTreeCursor_swigregister
TSTreeCursor_swigregister(TSTreeCursor)


def ts_parser_new():
    return _tree_sitter_api.ts_parser_new()
ts_parser_new = _tree_sitter_api.ts_parser_new

def ts_parser_delete(arg1):
    return _tree_sitter_api.ts_parser_delete(arg1)
ts_parser_delete = _tree_sitter_api.ts_parser_delete

def ts_parser_language(arg1):
    return _tree_sitter_api.ts_parser_language(arg1)
ts_parser_language = _tree_sitter_api.ts_parser_language

def ts_parser_set_language(arg1, arg2):
    return _tree_sitter_api.ts_parser_set_language(arg1, arg2)
ts_parser_set_language = _tree_sitter_api.ts_parser_set_language

def ts_parser_logger(arg1):
    return _tree_sitter_api.ts_parser_logger(arg1)
ts_parser_logger = _tree_sitter_api.ts_parser_logger

def ts_parser_set_logger(arg1, arg2):
    return _tree_sitter_api.ts_parser_set_logger(arg1, arg2)
ts_parser_set_logger = _tree_sitter_api.ts_parser_set_logger

def ts_parser_print_dot_graphs(arg1, arg2):
    return _tree_sitter_api.ts_parser_print_dot_graphs(arg1, arg2)
ts_parser_print_dot_graphs = _tree_sitter_api.ts_parser_print_dot_graphs

def ts_parser_halt_on_error(arg1, arg2):
    return _tree_sitter_api.ts_parser_halt_on_error(arg1, arg2)
ts_parser_halt_on_error = _tree_sitter_api.ts_parser_halt_on_error

def ts_parser_parse(arg1, arg2, arg3):
    return _tree_sitter_api.ts_parser_parse(arg1, arg2, arg3)
ts_parser_parse = _tree_sitter_api.ts_parser_parse

def ts_parser_parse_string(arg1, arg2, arg3, arg4):
    return _tree_sitter_api.ts_parser_parse_string(arg1, arg2, arg3, arg4)
ts_parser_parse_string = _tree_sitter_api.ts_parser_parse_string

def ts_parser_parse_string_encoding(arg1, arg2, arg3, arg4, arg5):
    return _tree_sitter_api.ts_parser_parse_string_encoding(arg1, arg2, arg3, arg4, arg5)
ts_parser_parse_string_encoding = _tree_sitter_api.ts_parser_parse_string_encoding

def ts_parser_cancellation_flag(arg1):
    return _tree_sitter_api.ts_parser_cancellation_flag(arg1)
ts_parser_cancellation_flag = _tree_sitter_api.ts_parser_cancellation_flag

def ts_parser_set_cancellation_flag(arg1, arg2):
    return _tree_sitter_api.ts_parser_set_cancellation_flag(arg1, arg2)
ts_parser_set_cancellation_flag = _tree_sitter_api.ts_parser_set_cancellation_flag

def ts_parser_timeout_micros(arg1):
    return _tree_sitter_api.ts_parser_timeout_micros(arg1)
ts_parser_timeout_micros = _tree_sitter_api.ts_parser_timeout_micros

def ts_parser_set_timeout_micros(arg1, arg2):
    return _tree_sitter_api.ts_parser_set_timeout_micros(arg1, arg2)
ts_parser_set_timeout_micros = _tree_sitter_api.ts_parser_set_timeout_micros

def ts_parser_reset(arg1):
    return _tree_sitter_api.ts_parser_reset(arg1)
ts_parser_reset = _tree_sitter_api.ts_parser_reset

def ts_parser_set_included_ranges(arg1, arg2, arg3):
    return _tree_sitter_api.ts_parser_set_included_ranges(arg1, arg2, arg3)
ts_parser_set_included_ranges = _tree_sitter_api.ts_parser_set_included_ranges

def ts_parser_included_ranges(arg1, arg2):
    return _tree_sitter_api.ts_parser_included_ranges(arg1, arg2)
ts_parser_included_ranges = _tree_sitter_api.ts_parser_included_ranges

def ts_tree_copy(arg1):
    return _tree_sitter_api.ts_tree_copy(arg1)
ts_tree_copy = _tree_sitter_api.ts_tree_copy

def ts_tree_delete(arg1):
    return _tree_sitter_api.ts_tree_delete(arg1)
ts_tree_delete = _tree_sitter_api.ts_tree_delete

def ts_tree_root_node(arg1):
    return _tree_sitter_api.ts_tree_root_node(arg1)
ts_tree_root_node = _tree_sitter_api.ts_tree_root_node

def ts_tree_edit(arg1, arg2):
    return _tree_sitter_api.ts_tree_edit(arg1, arg2)
ts_tree_edit = _tree_sitter_api.ts_tree_edit

def ts_tree_get_changed_ranges(arg1, arg2, arg3):
    return _tree_sitter_api.ts_tree_get_changed_ranges(arg1, arg2, arg3)
ts_tree_get_changed_ranges = _tree_sitter_api.ts_tree_get_changed_ranges

def ts_tree_print_dot_graph(arg1, arg2):
    return _tree_sitter_api.ts_tree_print_dot_graph(arg1, arg2)
ts_tree_print_dot_graph = _tree_sitter_api.ts_tree_print_dot_graph

def ts_tree_language(arg1):
    return _tree_sitter_api.ts_tree_language(arg1)
ts_tree_language = _tree_sitter_api.ts_tree_language

def ts_node_start_byte(arg1):
    return _tree_sitter_api.ts_node_start_byte(arg1)
ts_node_start_byte = _tree_sitter_api.ts_node_start_byte

def ts_node_start_point(arg1):
    return _tree_sitter_api.ts_node_start_point(arg1)
ts_node_start_point = _tree_sitter_api.ts_node_start_point

def ts_node_end_byte(arg1):
    return _tree_sitter_api.ts_node_end_byte(arg1)
ts_node_end_byte = _tree_sitter_api.ts_node_end_byte

def ts_node_end_point(arg1):
    return _tree_sitter_api.ts_node_end_point(arg1)
ts_node_end_point = _tree_sitter_api.ts_node_end_point

def ts_node_symbol(arg1):
    return _tree_sitter_api.ts_node_symbol(arg1)
ts_node_symbol = _tree_sitter_api.ts_node_symbol

def ts_node_type(arg1):
    return _tree_sitter_api.ts_node_type(arg1)
ts_node_type = _tree_sitter_api.ts_node_type

def ts_node_string(arg1):
    return _tree_sitter_api.ts_node_string(arg1)
ts_node_string = _tree_sitter_api.ts_node_string

def ts_node_eq(arg1, arg2):
    return _tree_sitter_api.ts_node_eq(arg1, arg2)
ts_node_eq = _tree_sitter_api.ts_node_eq

def ts_node_is_null(arg1):
    return _tree_sitter_api.ts_node_is_null(arg1)
ts_node_is_null = _tree_sitter_api.ts_node_is_null

def ts_node_is_named(arg1):
    return _tree_sitter_api.ts_node_is_named(arg1)
ts_node_is_named = _tree_sitter_api.ts_node_is_named

def ts_node_is_missing(arg1):
    return _tree_sitter_api.ts_node_is_missing(arg1)
ts_node_is_missing = _tree_sitter_api.ts_node_is_missing

def ts_node_has_changes(arg1):
    return _tree_sitter_api.ts_node_has_changes(arg1)
ts_node_has_changes = _tree_sitter_api.ts_node_has_changes

def ts_node_has_error(arg1):
    return _tree_sitter_api.ts_node_has_error(arg1)
ts_node_has_error = _tree_sitter_api.ts_node_has_error

def ts_node_parent(arg1):
    return _tree_sitter_api.ts_node_parent(arg1)
ts_node_parent = _tree_sitter_api.ts_node_parent

def ts_node_child(arg1, arg2):
    return _tree_sitter_api.ts_node_child(arg1, arg2)
ts_node_child = _tree_sitter_api.ts_node_child

def ts_node_named_child(arg1, arg2):
    return _tree_sitter_api.ts_node_named_child(arg1, arg2)
ts_node_named_child = _tree_sitter_api.ts_node_named_child

def ts_node_child_count(arg1):
    return _tree_sitter_api.ts_node_child_count(arg1)
ts_node_child_count = _tree_sitter_api.ts_node_child_count

def ts_node_named_child_count(arg1):
    return _tree_sitter_api.ts_node_named_child_count(arg1)
ts_node_named_child_count = _tree_sitter_api.ts_node_named_child_count

def ts_node_next_sibling(arg1):
    return _tree_sitter_api.ts_node_next_sibling(arg1)
ts_node_next_sibling = _tree_sitter_api.ts_node_next_sibling

def ts_node_next_named_sibling(arg1):
    return _tree_sitter_api.ts_node_next_named_sibling(arg1)
ts_node_next_named_sibling = _tree_sitter_api.ts_node_next_named_sibling

def ts_node_prev_sibling(arg1):
    return _tree_sitter_api.ts_node_prev_sibling(arg1)
ts_node_prev_sibling = _tree_sitter_api.ts_node_prev_sibling

def ts_node_prev_named_sibling(arg1):
    return _tree_sitter_api.ts_node_prev_named_sibling(arg1)
ts_node_prev_named_sibling = _tree_sitter_api.ts_node_prev_named_sibling

def ts_node_first_child_for_byte(arg1, arg2):
    return _tree_sitter_api.ts_node_first_child_for_byte(arg1, arg2)
ts_node_first_child_for_byte = _tree_sitter_api.ts_node_first_child_for_byte

def ts_node_first_named_child_for_byte(arg1, arg2):
    return _tree_sitter_api.ts_node_first_named_child_for_byte(arg1, arg2)
ts_node_first_named_child_for_byte = _tree_sitter_api.ts_node_first_named_child_for_byte

def ts_node_descendant_for_byte_range(arg1, arg2, arg3):
    return _tree_sitter_api.ts_node_descendant_for_byte_range(arg1, arg2, arg3)
ts_node_descendant_for_byte_range = _tree_sitter_api.ts_node_descendant_for_byte_range

def ts_node_named_descendant_for_byte_range(arg1, arg2, arg3):
    return _tree_sitter_api.ts_node_named_descendant_for_byte_range(arg1, arg2, arg3)
ts_node_named_descendant_for_byte_range = _tree_sitter_api.ts_node_named_descendant_for_byte_range

def ts_node_descendant_for_point_range(arg1, arg2, arg3):
    return _tree_sitter_api.ts_node_descendant_for_point_range(arg1, arg2, arg3)
ts_node_descendant_for_point_range = _tree_sitter_api.ts_node_descendant_for_point_range

def ts_node_named_descendant_for_point_range(arg1, arg2, arg3):
    return _tree_sitter_api.ts_node_named_descendant_for_point_range(arg1, arg2, arg3)
ts_node_named_descendant_for_point_range = _tree_sitter_api.ts_node_named_descendant_for_point_range

def ts_node_edit(arg1, arg2):
    return _tree_sitter_api.ts_node_edit(arg1, arg2)
ts_node_edit = _tree_sitter_api.ts_node_edit

def ts_tree_cursor_new(arg1):
    return _tree_sitter_api.ts_tree_cursor_new(arg1)
ts_tree_cursor_new = _tree_sitter_api.ts_tree_cursor_new

def ts_tree_cursor_delete(arg1):
    return _tree_sitter_api.ts_tree_cursor_delete(arg1)
ts_tree_cursor_delete = _tree_sitter_api.ts_tree_cursor_delete

def ts_tree_cursor_reset(arg1, arg2):
    return _tree_sitter_api.ts_tree_cursor_reset(arg1, arg2)
ts_tree_cursor_reset = _tree_sitter_api.ts_tree_cursor_reset

def ts_tree_cursor_current_node(arg1):
    return _tree_sitter_api.ts_tree_cursor_current_node(arg1)
ts_tree_cursor_current_node = _tree_sitter_api.ts_tree_cursor_current_node

def ts_tree_cursor_goto_parent(arg1):
    return _tree_sitter_api.ts_tree_cursor_goto_parent(arg1)
ts_tree_cursor_goto_parent = _tree_sitter_api.ts_tree_cursor_goto_parent

def ts_tree_cursor_goto_next_sibling(arg1):
    return _tree_sitter_api.ts_tree_cursor_goto_next_sibling(arg1)
ts_tree_cursor_goto_next_sibling = _tree_sitter_api.ts_tree_cursor_goto_next_sibling

def ts_tree_cursor_goto_first_child(arg1):
    return _tree_sitter_api.ts_tree_cursor_goto_first_child(arg1)
ts_tree_cursor_goto_first_child = _tree_sitter_api.ts_tree_cursor_goto_first_child

def ts_tree_cursor_goto_first_child_for_byte(arg1, arg2):
    return _tree_sitter_api.ts_tree_cursor_goto_first_child_for_byte(arg1, arg2)
ts_tree_cursor_goto_first_child_for_byte = _tree_sitter_api.ts_tree_cursor_goto_first_child_for_byte

def ts_language_symbol_count(arg1):
    return _tree_sitter_api.ts_language_symbol_count(arg1)
ts_language_symbol_count = _tree_sitter_api.ts_language_symbol_count

def ts_language_symbol_name(arg1, arg2):
    return _tree_sitter_api.ts_language_symbol_name(arg1, arg2)
ts_language_symbol_name = _tree_sitter_api.ts_language_symbol_name

def ts_language_symbol_for_name(arg1, arg2):
    return _tree_sitter_api.ts_language_symbol_for_name(arg1, arg2)
ts_language_symbol_for_name = _tree_sitter_api.ts_language_symbol_for_name

def ts_language_symbol_type(arg1, arg2):
    return _tree_sitter_api.ts_language_symbol_type(arg1, arg2)
ts_language_symbol_type = _tree_sitter_api.ts_language_symbol_type

def ts_language_version(arg1):
    return _tree_sitter_api.ts_language_version(arg1)
ts_language_version = _tree_sitter_api.ts_language_version
class p_uint32_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, p_uint32_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, p_uint32_t, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _tree_sitter_api.new_p_uint32_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_p_uint32_t
    __del__ = lambda self: None

    def assign(self, value):
        return _tree_sitter_api.p_uint32_t_assign(self, value)

    def value(self):
        return _tree_sitter_api.p_uint32_t_value(self)

    def cast(self):
        return _tree_sitter_api.p_uint32_t_cast(self)
    if _newclass:
        frompointer = staticmethod(_tree_sitter_api.p_uint32_t_frompointer)
    else:
        frompointer = _tree_sitter_api.p_uint32_t_frompointer
p_uint32_t_swigregister = _tree_sitter_api.p_uint32_t_swigregister
p_uint32_t_swigregister(p_uint32_t)

def p_uint32_t_frompointer(t):
    return _tree_sitter_api.p_uint32_t_frompointer(t)
p_uint32_t_frompointer = _tree_sitter_api.p_uint32_t_frompointer

class p_TSTreeCursor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, p_TSTreeCursor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, p_TSTreeCursor, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _tree_sitter_api.new_p_TSTreeCursor()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_p_TSTreeCursor
    __del__ = lambda self: None

    def assign(self, value):
        return _tree_sitter_api.p_TSTreeCursor_assign(self, value)

    def value(self):
        return _tree_sitter_api.p_TSTreeCursor_value(self)

    def cast(self):
        return _tree_sitter_api.p_TSTreeCursor_cast(self)
    if _newclass:
        frompointer = staticmethod(_tree_sitter_api.p_TSTreeCursor_frompointer)
    else:
        frompointer = _tree_sitter_api.p_TSTreeCursor_frompointer
p_TSTreeCursor_swigregister = _tree_sitter_api.p_TSTreeCursor_swigregister
p_TSTreeCursor_swigregister(p_TSTreeCursor)

def p_TSTreeCursor_frompointer(t):
    return _tree_sitter_api.p_TSTreeCursor_frompointer(t)
p_TSTreeCursor_frompointer = _tree_sitter_api.p_TSTreeCursor_frompointer

class p_TSTree(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, p_TSTree, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, p_TSTree, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _tree_sitter_api.new_p_TSTree()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_p_TSTree
    __del__ = lambda self: None

    def assign(self, value):
        return _tree_sitter_api.p_TSTree_assign(self, value)

    def value(self):
        return _tree_sitter_api.p_TSTree_value(self)

    def cast(self):
        return _tree_sitter_api.p_TSTree_cast(self)
    if _newclass:
        frompointer = staticmethod(_tree_sitter_api.p_TSTree_frompointer)
    else:
        frompointer = _tree_sitter_api.p_TSTree_frompointer
p_TSTree_swigregister = _tree_sitter_api.p_TSTree_swigregister
p_TSTree_swigregister(p_TSTree)

def p_TSTree_frompointer(t):
    return _tree_sitter_api.p_TSTree_frompointer(t)
p_TSTree_frompointer = _tree_sitter_api.p_TSTree_frompointer

class p_TSNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, p_TSNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, p_TSNode, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _tree_sitter_api.new_p_TSNode()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_p_TSNode
    __del__ = lambda self: None

    def assign(self, value):
        return _tree_sitter_api.p_TSNode_assign(self, value)

    def value(self):
        return _tree_sitter_api.p_TSNode_value(self)

    def cast(self):
        return _tree_sitter_api.p_TSNode_cast(self)
    if _newclass:
        frompointer = staticmethod(_tree_sitter_api.p_TSNode_frompointer)
    else:
        frompointer = _tree_sitter_api.p_TSNode_frompointer
p_TSNode_swigregister = _tree_sitter_api.p_TSNode_swigregister
p_TSNode_swigregister(p_TSNode)

def p_TSNode_frompointer(t):
    return _tree_sitter_api.p_TSNode_frompointer(t)
p_TSNode_frompointer = _tree_sitter_api.p_TSNode_frompointer

class p_TSRange(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, p_TSRange, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, p_TSRange, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _tree_sitter_api.new_p_TSRange()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_p_TSRange
    __del__ = lambda self: None

    def assign(self, value):
        return _tree_sitter_api.p_TSRange_assign(self, value)

    def value(self):
        return _tree_sitter_api.p_TSRange_value(self)

    def cast(self):
        return _tree_sitter_api.p_TSRange_cast(self)
    if _newclass:
        frompointer = staticmethod(_tree_sitter_api.p_TSRange_frompointer)
    else:
        frompointer = _tree_sitter_api.p_TSRange_frompointer
p_TSRange_swigregister = _tree_sitter_api.p_TSRange_swigregister
p_TSRange_swigregister(p_TSRange)

def p_TSRange_frompointer(t):
    return _tree_sitter_api.p_TSRange_frompointer(t)
p_TSRange_frompointer = _tree_sitter_api.p_TSRange_frompointer

class a_TSRange(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, a_TSRange, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, a_TSRange, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _tree_sitter_api.new_a_TSRange(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _tree_sitter_api.delete_a_TSRange
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _tree_sitter_api.a_TSRange___getitem__(self, index)

    def __setitem__(self, index, value):
        return _tree_sitter_api.a_TSRange___setitem__(self, index, value)

    def cast(self):
        return _tree_sitter_api.a_TSRange_cast(self)
    if _newclass:
        frompointer = staticmethod(_tree_sitter_api.a_TSRange_frompointer)
    else:
        frompointer = _tree_sitter_api.a_TSRange_frompointer
a_TSRange_swigregister = _tree_sitter_api.a_TSRange_swigregister
a_TSRange_swigregister(a_TSRange)

def a_TSRange_frompointer(t):
    return _tree_sitter_api.a_TSRange_frompointer(t)
a_TSRange_frompointer = _tree_sitter_api.a_TSRange_frompointer


def fopen(filename, mode):
    return _tree_sitter_api.fopen(filename, mode)
fopen = _tree_sitter_api.fopen

def fclose(arg1):
    return _tree_sitter_api.fclose(arg1)
fclose = _tree_sitter_api.fclose
# This file is compatible with both classic and new-style classes.


