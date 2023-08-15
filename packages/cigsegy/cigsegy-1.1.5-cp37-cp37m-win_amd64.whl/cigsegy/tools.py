# Copyright (c) 2023 Jintao Li.
# Computational and Interpretation Group (CIG),
# University of Science and Technology of China (USTC).
# All rights reserved.
#
# github: https://github.com/JintaoLee-Roger


import struct
import numpy as np
from typing import List, Tuple, Dict
from .cigsegy import (Pysegy, fromfile, tofile, create_by_sharing_header,
                      kBinaryHeaderHelp, kTraceHeaderHelp)
import warnings
from . import utils


def create(segy_out: str,
           binary_in: str or np.ndarray,
           shape: Tuple = None,
           format: int = 5,
           dt: int = 2000,
           start_time: int = 0,
           iline_interval: float = 25,
           xline_interval: float = 25,
           min_iline: int = 1,
           min_xline: int = 1,
           custom_info: List[str] = []) -> None:
    """
    Create a segy format file from a binary file or np.ndarray
    
    Parameters
    ----------
    segy_out : str
        out segy format file path
    binary_in : str or np.array
        the input binary file or array
    shape : Tuple
        len == 3
    format : int
        the data format code, 1 for 4 bytes IBM float, 5 for 4 bytes IEEE float
    dt : int
        data sample interval, 2000 means 2ms
    start_time : int
        start time for each trace
    iline_interval : int
        inline interval, will affect cdp x and cdp y
    xline_interval : int
        crossline interval, will affect cdp x and cdp y
    min_iline : int
        the start inline number
    min_xline : int 
        the start crossline number
    custom_info : List[str]
        textual header info by user custom, max: 12 rows each row is less than 76 chars
    """
    if isinstance(binary_in, str):
        assert shape is not None
        assert len(shape) == 3
        segy_create = Pysegy(binary_in, shape[2], shape[1], shape[0])
    elif isinstance(binary_in, np.ndarray):
        assert len(binary_in.shape) == 3
        sizeZ, sizeY, sizeX = binary_in.shape
        segy_create = Pysegy(sizeX, sizeY, sizeZ)
    else:
        raise ValueError(
            f'the input argument: binary_in must be a string or np array')
    segy_create.setDataFormatCode(format)
    segy_create.setSampleInterval(dt)
    segy_create.setStartTime(start_time)
    segy_create.setInlineInterval(iline_interval)
    segy_create.setCrosslineInterval(xline_interval)
    segy_create.setMinInline(min_iline)
    segy_create.setMinCrossline(min_xline)
    if isinstance(binary_in, str):
        segy_create.create(segy_out, custom_info)
    else:
        segy_create.create(segy_out, binary_in, custom_info)


def textual_header(segy_name: str, coding: str = None) -> None:
    """
    Print segy file's 3200 bytes textual header.

    Parameters
    ----------
    segy_name : str
        input segy file
    coding : str
        force the coding as 'a': ascii or 'e': ebcdic. If coding is None, cigsegy will guess the coding
    """
    coding = 'u' if coding is None else coding
    segy = Pysegy(segy_name)
    print(segy.textual_header(coding))
    segy.close_file()


def metaInfo(segy_name: str,
             iline: int = 189,
             xline: int = 193,
             istep: int = 1,
             xstep: int = 1,
             xloc: int = 73,
             yloc: int = 77,
             use_guess: bool = False) -> None:
    """
    print meta info of `segy_name` file

    Parameters
    ----------
    iline : int
        iline location in trace header
    iline : int
        iline location in trace header
    istep : int
        iline step, 2 means iline is like 100, 102, 104, ...
    xstep : int
        xline step
    xloc : int
        cdp x (real world) value location in trace header
    yloc : int
        cdp y (real world) value location in trace header
    use_guess : bool
        if iline/xline/istep/xstep are unknow, you can set use_guess = True to guess them
    """
    if use_guess:
        [iline, xline, istep, xstep] = utils.guess(segy_name)[0]
    segy = Pysegy(segy_name)
    segy.setInlineLocation(iline)
    segy.setCrosslineLocation(xline)
    segy.setSteps(istep, xstep)
    segy.setXLocation(xloc)
    segy.setYLocation(yloc)
    print(segy.metaInfo())
    segy.close_file()


def fromfile_by_guess(segy_name: str) -> np.ndarray:
    """
    reading from a segy file.

    Parameters
    ----------
    segy_name : str
        the input segy file name

    Returns
    -------
    np.ndarray
        3D array data
    """

    loc = utils.guess(segy_name)

    for l in loc:
        try:
            metaInfo(segy_name, l[0], l[1], l[2], l[3])
            d = fromfile(segy_name, l[0], l[1], l[2], l[3])
            return d
        except:
            continue

    raise RuntimeError(
        "Cannot read by guess location, please specify the location")


def tofile_by_guess(segy_name: str, out_name: str) -> None:
    """
    convert a segy file to a binary file

    Parameters
    -----------
    segy_name : str
        the input segy file name
    out_name : str
        the output binary file name
    """
    loc = utils.guess(segy_name)
    finish = False

    for l in loc:
        try:
            metaInfo(segy_name, l[0], l[1], l[2], l[3])
            tofile(out_name, l[0], l[1], l[2], l[3])
            finish = True
            break
        except:
            continue

    if not finish:
        raise RuntimeError(
            "Cannot read by guess location, please specify the location")


def create_by_sharing_header_guess(segy_name: str,
                                   header_segy: str,
                                   src: np.ndarray or str,
                                   shape: list or tuple = None,
                                   offset: list or tuple or dict = None,
                                   custom_info: List[str] = []) -> None:
    """
    create a segy and its header is from an existed segy.

    Parameters
    ----------
    segy_name : str
        the out segy name
    header_segy : str 
        the header segy file
    src : np.ndarray
        source data
    shape : Tuple or List
        if src is str, shape must be specify
    offset : Tuple or List
        the offset of a sub data from a original data, e.g., dsub = d[256:400, 500: 100:], offset = [256, 500, 100]
    custom_info : List[str]
        textual header info by user custom, max: 12 rows each row is less than 76 chars, use it when offset is not None
    """
    if isinstance(src, str) and shape is None:
        raise ValueError("Shape is None!")

    loc = utils.guess(header_segy)
    finish = False

    for l in loc:
        try:
            if isinstance(src, str):
                create_by_sharing_header(segy_name,
                                         header_segy,
                                         src,
                                         shape,
                                         l[0],
                                         l[1],
                                         l[2],
                                         l[3],
                                         offset=offset,
                                         custom_info=custom_info)
            else:
                create_by_sharing_header(segy_name,
                                         header_segy,
                                         src,
                                         l[0],
                                         l[1],
                                         l[2],
                                         l[3],
                                         offset=offset,
                                         custom_info=custom_info)
            finish = True
            break
        except:
            continue

    if not finish:
        raise RuntimeError(
            "Cannot read by guess location, please specify the location")


def plot_region(segy: str or Pysegy,
                mode: str = 'line',
                loc: list = None,
                cdpxy_loc: list = None,
                save: str = None) -> None:
    """
    plot the region map (x and y axis are inline and crossline)

    Parameters
    ----------
    segy : str or Pysegy
        input segy file
    loc : list
        contains 4 values, as [iline, xline, istep, xstep]
    save : str
        save to a png image
    """
    if mode not in ['line', 'cdpxy']:
        raise RuntimeError(f"mode must be 'line' or 'cdpxy', mode = {mode}")

    assert loc is None or len(loc) == 4
    assert cdpxy_loc is None or len(cdpxy_loc) == 2
    cdpx = 73 if cdpxy_loc is None else cdpxy_loc[0]
    cdpy = 77 if cdpxy_loc is None else cdpxy_loc[1]

    if isinstance(segy, Pysegy):
        try:
            segy.scan()
        except:
            loc = utils.guess(segy)[0]
            segy.setInlineLocation(loc[0])
            segy.setCrosslineLocation(loc[1])
            segy.setSteps(loc[2], loc[3])
            segy.scan()
        lineinfo = segy.get_lineInfo()
        is_xline_fast = segy.is_crossline_fast_order
    elif isinstance(segy, str):
        if loc is None:
            loc = utils.guess(segy)[0]
        segy = Pysegy(segy)
        segy.setInlineLocation(loc[0])
        segy.setCrosslineLocation(loc[1])
        segy.setSteps(loc[2], loc[3])
        segy.scan()
        lineinfo = segy.get_lineInfo()
        is_xline_fast = segy.is_crossline_fast_order
    else:
        raise RuntimeError("Invalid type of `segy`")

    if mode == 'line':
        x = np.concatenate((lineinfo[:, 0], lineinfo[::-1, 0]))
        y = np.concatenate((lineinfo[:, 1], lineinfo[::-1, 2]))
        x = np.append(x, x[0])
        y = np.append(y, y[0])
    else:
        ni = lineinfo.shape[0]
        N = ni * 2 + 1
        x = np.zeros(N, dtype=int)
        y = np.zeros(N, dtype=int)
        for i in range(ni):
            x[i] = utils.get_trace_keys(segy, cdpx, lineinfo[i, 3])
            y[i] = utils.get_trace_keys(segy, cdpy, lineinfo[i, 3])
            x[N - i - 2] = utils.get_trace_keys(segy, cdpx, lineinfo[i, 4])
            y[N - i - 2] = utils.get_trace_keys(segy, cdpy, lineinfo[i, 4])
        x[-1] = x[0]
        y[-1] = y[0]

    istep = x[1] - x[0]
    xstep = (lineinfo[0, 2] - lineinfo[0, 1]) // (lineinfo[0, 5] - 1)
    if not is_xline_fast:
        istep, xstep = xstep, istep

    import matplotlib.pyplot as plt

    plt.fill(x, y, color=(0.9, 0.9, 0.9))
    plt.plot(x, y)
    plt.gca().invert_yaxis()
    # plt.gca().xaxis.set_ticks_position('top')

    plt.grid(True, linestyle='--')
    if mode == 'line':
        xlabel = f"Inline Number/interval={istep}"
        ylabel = f"Crossline Number/interval={xstep}"
    else:
        xlabel = f"CDP X"
        ylabel = f"CDP Y"
    if not is_xline_fast:
        xlabel, ylabel = ylabel, xlabel
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Region')
    if save:
        plt.savefig(save, dpi=200, bbox_inches='tight', pad_inches=0.0)
    plt.show()


def read_header(segy: str or Pysegy, type, n=0, printstr=True):
    """
    Read binary or trace header

    Parameters
    ----------
    segy : str or Pysegy
        input segy file
    type: str
        can be one of ['bh', 'th', 't'],
            'bt' means binary header, 'th' means trace header,
            't' means trace (include trace header and trace)
    n : int
        trace number when type is 'th' or t
    printstr : bool
        print header information, if False, return a dict of header's infomation

    Returns
    -------
    Dict or None
    """
    if isinstance(segy, str):
        segy = Pysegy(segy)

    if type == 'bh':
        arr = segy.get_binary_header()
        out = utils.convert_header(arr, kBinaryHeaderHelp, printstr, 3200)
        if printstr:
            for l in out:
                print(l)
            return
        return out
    elif type == 'th':
        arr = segy.get_trace_header(n)
        out = utils.convert_header(arr, kTraceHeaderHelp, printstr)
        if printstr:
            for l in out:
                print(l)
            return
        return out
    elif type == 't':
        arr = segy.get_trace(n)
        out = utils.convert_header(arr[:240], kTraceHeaderHelp, printstr)
        d = utils.convert_trace(arr[240:])
        if printstr:
            for l in out:
                print(l)
            return d
        return out, d


def get_metaInfo(segy_name: str,
                 iline: int = 189,
                 xline: int = 193,
                 istep: int = 1,
                 xstep: int = 1,
                 xloc: int = 73,
                 yloc: int = 77,
                 use_guess: bool = False,
                 apply_scalar: bool = False) -> Dict:
    """
    get metainfo dict of `segy_name` file

    Parameters
    ----------
    segy_name : str
        input segy file
    iline : int
        iline location in trace header
    iline : int
        iline location in trace header
    istep : int
        iline step, 2 means iline is like 100, 102, 104, ...
    xstep : int
        xline step
    xloc : int
        x (real world) value location in trace header
    yloc : int
        y (real world) value location in trace header
    use_guess : bool
        if iline/xline/istep/xstep are unknow, 
            you can set use_guess = True to guess them
    apply_scalar : bool
        apply scalar to 'i-interval' and 'x-interval'

    Returns
    -------
    Dict
        Dict of meta information 
    """
    if use_guess:
        [iline, xline, istep, xstep] = utils.guess(segy_name)[0]
    segy = Pysegy(segy_name)
    segy.setInlineLocation(iline)
    segy.setCrosslineLocation(xline)
    segy.setSteps(istep, xstep)
    segy.setXLocation(xloc)
    segy.setYLocation(yloc)
    segy.scan()
    m = segy.get_metaInfo()
    segy.close_file()

    return utils.metainfo_to_dict(m, apply_scalar)


def trace_count(segy: str or Pysegy) -> int:
    """
    Count the total numbers of a segy file

    Parameters
    ----------
    segy: str or Pysegy
        input segy file

    Returns
    -------
    int
        The total numbers of a segy file
    """
    if isinstance(segy, str):
        segy = Pysegy(segy)
        count = segy.trace_count
        segy.close_file()
        return count

    return segy.trace_count