"""Data stores for input from ByteBlower Triggers (frame blasting use case)."""
from typing import Optional, Sequence  # for type hinting

from pandas import Timestamp  # for type hinting
from pandas import DataFrame

from .data_store import DataStore


class FrameCountData(DataStore):

    __slots__ = (
        '_df_tx',
        '_df_rx',
        '_total_tx_bytes',
        '_total_rx_bytes',
        '_total_tx_vlan_bytes',
        '_total_rx_vlan_bytes',
        '_total_tx_packets',
        '_total_rx_packets',
        '_timestamp_tx_first',
        '_timestamp_tx_last',
        '_timestamp_rx_first',
        '_timestamp_rx_last',
    )

    def __init__(self) -> None:
        self._df_tx = DataFrame(
            columns=[
                "Duration total",
                "Packets total",
                "Bytes total",
                "Duration interval",
                "Packets interval",
                "Bytes interval",
            ]
        )
        self._df_rx = DataFrame(
            columns=[
                "Duration total",
                "Packets total",
                "Bytes total",
                "Duration interval",
                "Packets interval",
                "Bytes interval",
            ]
        )
        self._total_tx_bytes: Optional[int] = None
        self._total_rx_bytes: Optional[int] = None
        self._total_tx_vlan_bytes: Optional[int] = None
        self._total_rx_vlan_bytes: Optional[int] = None
        self._total_tx_packets: Optional[int] = None
        self._total_rx_packets: Optional[int] = None
        self._timestamp_tx_first: Optional[Timestamp] = None
        self._timestamp_tx_last: Optional[Timestamp] = None
        self._timestamp_rx_first: Optional[Timestamp] = None
        self._timestamp_rx_last: Optional[Timestamp] = None

    @property
    def df_tx(self) -> DataFrame:
        """
        Return ``DataFrame`` of transmitter over time results.

        Includes:

        * Total duration since first packet transmitted
        * Cumulative number of packets transmitted
        * Cumulative number of bytes transmitted
        * Duration per interval
        * Number of packets transmitted per interval
        * Number of bytes transmitted per interval
        """
        return self._df_tx

    @property
    def df_rx(self) -> DataFrame:
        """
        Return ``DataFrame`` of receiver over time results.

        Includes:

        * Total duration since first packet received
        * Cumulative number of packets received
        * Cumulative number of bytes received
        * Duration per interval
        * Number of packets received per interval
        * Number of bytes received per interval
        """
        return self._df_rx

    @property
    def total_tx_bytes(self) -> int:
        """Return total transmitted number of bytes."""
        return self._total_tx_bytes

    @property
    def total_rx_bytes(self) -> int:
        """Return total received number of bytes."""
        return self._total_rx_bytes

    @property
    def total_tx_vlan_bytes(self) -> int:
        """Return total number of bytes transmitted in Layer2.5 VLAN header."""
        return self._total_tx_vlan_bytes

    @property
    def total_rx_vlan_bytes(self) -> int:
        """Return total number of bytes received in Layer2.5 VLAN header."""
        return self._total_rx_vlan_bytes

    @property
    def total_tx_packets(self) -> int:
        """Return total transmitted number of packets."""
        return self._total_tx_packets

    @property
    def total_rx_packets(self) -> int:
        """Return total received number of packets."""
        return self._total_rx_packets

    @property
    def timestamp_tx_first(self) -> Optional[Timestamp]:
        """Return the timestamp of the first transmitted packet."""
        return self._timestamp_tx_first

    @property
    def timestamp_tx_last(self) -> Optional[Timestamp]:
        """Return the timestamp of the last transmitted packet."""
        return self._timestamp_tx_last

    @property
    def timestamp_rx_first(self) -> Optional[Timestamp]:
        """Return the timestamp of the first received packet."""
        return self._timestamp_rx_first

    @property
    def timestamp_rx_last(self) -> Optional[Timestamp]:
        """Return the timestamp of the last received packet."""
        return self._timestamp_rx_last


class LatencyData(DataStore):

    __slots__ = (
        '_df_latency',
        '_final_min_latency',
        '_final_max_latency',
        '_final_avg_latency',
        '_final_avg_jitter',
        '_final_packet_count_valid',
        '_final_packet_count_invalid',
    )

    def __init__(self) -> None:
        self._df_latency = DataFrame(
            columns=[
                "Minimum",
                "Maximum",
                "Average",
                "Jitter",
            ]
        )
        self._final_min_latency: Optional[float] = None
        self._final_max_latency: Optional[float] = None
        self._final_avg_latency: Optional[float] = None
        self._final_avg_jitter: Optional[float] = None
        self._final_packet_count_valid: Optional[int] = None
        self._final_packet_count_invalid: Optional[int] = None

    @property
    def df_latency(self) -> DataFrame:
        """Return the latency statistics over time.

        Includes result snapshots with content:

        * Index: "Timestamp": Snapshot timestamp
        * "Minimum": Maximum latency within the duration of this snapshot.
        * "Maximum": Maximum latency within the duration of this snapshot.
        * "Average": Average latency within the duration of this snapshot.
        * "Jitter": Average latency jitter within the duration of this snapshot.

        .. note::
           Used for machine-readable detailed reporting.
        """
        return self._df_latency

    @property
    def final_min_latency(self) -> Optional[float]:
        """Return the minimum latency in milliseconds."""
        return self._final_min_latency

    @property
    def final_max_latency(self) -> Optional[float]:
        """Return the maximum latency in milliseconds."""
        return self._final_max_latency

    @property
    def final_avg_latency(self) -> Optional[float]:
        """Return the average latency in milliseconds."""
        return self._final_avg_latency

    @property
    def final_avg_jitter(self) -> Optional[float]:
        """Return the average jitter in milliseconds."""
        return self._final_avg_jitter

    @property
    def final_packet_count_valid(self) -> int:
        """Return the number of packets with valid latency tag."""
        return self._final_packet_count_valid

    @property
    def final_packet_count_invalid(self) -> int:
        """Return the number of packets with invalid latency tag."""
        return self._final_packet_count_invalid


class LatencyDistributionData(DataStore):

    __slots__ = (
        '_bucket_width',
        '_packet_count_buckets',
        '_final_min_latency',
        '_final_max_latency',
        '_final_avg_latency',
        '_final_avg_jitter',
        '_final_packet_count_valid',
        '_final_packet_count_invalid',
        '_final_packet_count_below_min',
        '_final_packet_count_above_max',
    )

    def __init__(self) -> None:
        self._bucket_width: int = None
        self._packet_count_buckets: Sequence[int] = None
        self._final_min_latency: Optional[float] = None
        self._final_max_latency: Optional[float] = None
        self._final_avg_latency: Optional[float] = None
        self._final_avg_jitter: Optional[float] = None
        self._final_packet_count_valid: Optional[int] = None
        self._final_packet_count_invalid: Optional[int] = None
        self._final_packet_count_below_min: Optional[int] = None
        self._final_packet_count_above_max: Optional[int] = None

    @property
    def bucket_width(self) -> int:
        """Return the bucket width in nanoseconds."""
        return self._bucket_width

    @property
    def packet_count_buckets(self) -> Sequence[int]:
        """Return the list of packet counts per bucket."""
        return self._packet_count_buckets

    @property
    def final_min_latency(self) -> Optional[float]:
        """Return the minimum latency in milliseconds."""
        return self._final_min_latency

    @property
    def final_max_latency(self) -> Optional[float]:
        """Return the maximum latency in milliseconds."""
        return self._final_max_latency

    @property
    def final_avg_latency(self) -> Optional[float]:
        """Return the average latency in milliseconds."""
        return self._final_avg_latency

    @property
    def final_avg_jitter(self) -> Optional[float]:
        """Return the average jitter in milliseconds."""
        return self._final_avg_jitter

    @property
    def final_packet_count_valid(self) -> int:
        """Return the number of packets received with valid latency tag."""
        return self._final_packet_count_valid

    @property
    def final_packet_count_invalid(self) -> int:
        """Return the number of packets received with invalid latency tag."""
        return self._final_packet_count_invalid

    @property
    def final_packet_count_below_min(self) -> int:
        """Return the number of packets received with latency below minimum."""
        return self._final_packet_count_below_min

    @property
    def final_packet_count_above_max(self) -> int:
        """Return the number of packets received with latency above maximum."""
        return self._final_packet_count_above_max
