import datetime
import re

import piexif

from image2gps.config import (
    TimeType,
    MIN_TIME,
    MAX_TIMEDELTA,
    DATE_STAMP_PATTENS,
    TIME_STAMP_PATTENS,
    TIME_STAMP_BASIC_PATTERN,
)
from image2gps.failed import on_fail


def parse_time(exif: dict) -> TimeType:
    zero_th = exif.get('0th', {})
    date_time = zero_th.get(piexif.ImageIFD.DateTime)
    try:
        if date_time is None:
            date_time = parse_from_gps_exif(exif)
        else:
            date_time = parse_from_ordinary_exif(date_time)
    except Exception as e:
        date_time_hash = hash(str(date_time))
        on_fail(date_time_hash, f'Failed to parse time "{date_time}" due to {e} ({type(e)})')
        return None
    if date_time is None:
        return None
    max_date_time = datetime.datetime.now() + MAX_TIMEDELTA
    if date_time < MIN_TIME or date_time > max_date_time:
        time_hash = hash(str(date_time))
        on_fail(time_hash, f'Date "{date_time}" is out of range')
        return None
    return date_time


def parse_from_gps_exif(exif: dict) -> TimeType:
    gps = exif.get('GPS')
    if gps is None or len(gps) == 0:
        return None

    date = gps.get(piexif.GPSIFD.GPSDateStamp)
    if date is None:
        return None
    date = _parse_date_stamp(date.decode(), throw=True)

    time = gps.get(piexif.GPSIFD.GPSTimeStamp)
    time = _parse_gps_time_stamp(time) if time is not None else datetime.time()
    return datetime.datetime.combine(date, time, tzinfo=None)


def _parse_gps_time_stamp(value: tuple) -> datetime.time:
    hours, minutes, seconds = [
        numerator // denominator
        for numerator, denominator in value
    ]
    hours, minutes, seconds = _normalize_time_parts(hours, minutes, seconds)
    return datetime.time(hours, minutes, seconds)


def parse_from_ordinary_exif(date_time: bytes) -> TimeType:
    date_time = date_time.replace(b'\x00', b'').strip().decode()
    date_time = re.sub(r'\s{2,}', ' ', date_time).removesuffix('Z').removesuffix(' г.')
    if len(date_time) == 0 or date_time.startswith('0000:00:00'):
        return None
    try:
        return _parse_datetime_basic(date_time)
    except Exception:
        pass

    if ' ' not in date_time:
        date = _parse_date_stamp(date_time, throw=True)
        return datetime.datetime.combine(date, datetime.time(), tzinfo=None)
    date, time = date_time.rsplit(' ', maxsplit=1)
    date = _parse_date_stamp(date, throw=False)
    if date is None:
        date = _parse_date_stamp(date_time, throw=True)
        return datetime.datetime.combine(date, datetime.time(), tzinfo=None)
    time = _parse_time_stamp(time)
    return datetime.datetime.combine(date, time, tzinfo=None)


def _parse_datetime_basic(value: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(value).replace(tzinfo=None)


def _parse_date_stamp(value: str, throw: bool) -> datetime.date | None:
    for pattern, timelike in DATE_STAMP_PATTENS.items():
        if pattern.match(value):
            return datetime.datetime.strptime(value, timelike).replace(tzinfo=None).date()
    if throw:
        raise ValueError(f'Failed to parse date "{value}"')


def _parse_time_stamp(value: str) -> datetime.time:
    value = _fix_time_stamp_overflow(value)
    for pattern, timelike in TIME_STAMP_PATTENS.items():
        if pattern.match(value):
            return datetime.datetime.strptime(value, timelike).replace(tzinfo=None).time()
    return datetime.time()


def _fix_time_stamp_overflow(value: str) -> str:
    time = TIME_STAMP_BASIC_PATTERN.search(value)
    if time is None:
        return value
    time = time.group()
    hours, minutes, seconds = map(int, time.split(':'))
    if hours in range(24) and minutes in range(60) and seconds in range(60):
        return value
    hours, minutes, seconds = _normalize_time_parts(hours, minutes, seconds)
    return _replace_rightmost(value, time, f'{hours:02}:{minutes:02}:{seconds:02}')


def _normalize_time_parts(hours: int, minutes: int, seconds: int) -> tuple[int, int, int]:
    return hours % 24, minutes % 60, seconds % 60


def _replace_rightmost(value: str, old: str, new: str, count: int = 1) -> str:
    return new.join(value.rsplit(old, count))
