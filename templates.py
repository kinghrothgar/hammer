#!/usr/bin/python2.6

header="""          [Delta Hammer] 
info from '$command' every $delta sec
Start: $start_time | Current: $current_time

"""

link="""[$name] $ips
    RX  bytes: $rx_bytes ($rx_bytes_abso)
        packets: $rx_packets ($rx_packets_abso)
        errors:$rx_errors ($rx_errors_abso) dropped:$rx_dropped ($rx_dropped_abso) overrun:$rx_overrun ($rx_overrun_abso) mcast:$rx_mcast ($rx_mcast_abso)
    TX  bytes: $tx_bytes ($tx_bytes_abso)
        packets: $tx_packets ($tx_packets_abso)
        errors:$tx_errors ($tx_errors_abso) dropped:$tx_dropped ($tx_dropped_abso) carrier:$tx_carrier ($tx_carrier_abso) collsns:$tx_collsns ($tx_collsns_abso)"""


ip="""Ip:
    $totalpacketsreceived ($totalpacketsreceived_abso) total packets received
    $withinvalidaddresses ($withinvalidaddresses_abso) with invalid addresses 
    $forwarded ($forwarded_abso) forwarded
    $incomingpacketsdiscarded ($incomingpacketsdiscarded_abso) incoming packets discarded
    $incomingpacketsdelivered ($incomingpacketsdelivered_abso) requests sent out
    $requestssentout ($requestssentout_abso) requests sent out
    $outgoingpacketsdropped ($outgoingpacketsdropped_abso) outgoing packets dropped
    $fragmentsdroppedaftertimeout ($fragmentsdroppedaftertimeout_abso) fragments dropped after timeout
    $reassembliesrequired ($reassembliesrequired_abso) reassemblies required
    $packetsreassembledok ($packetsreassembledok_abso) packets reassembled ok
    $packetreassemblesfailed ($packetreassemblesfailed_abso) packet reassembles failed
    $fragmentsreceivedok ($fragmentsreceivedok_abso) fragments received ok
    $fragmentsfailed ($fragmentsfailed_abso) fragments failed
    $fragmentscreated ($fragmentscreated_abso) fragments created
IpExt:
    InMcastPkts: $InMcastPkts ($InMcastPkts_abso)
    InBcastPkts: $InBcastPkts ($InBcastPkts_abso)
    InOctets: $InOctets ($InOctets_abso)
    OutOctets: $OutOctets ($OutOctets_abso)
    InMcastOctets: $InMcastOctets ($InMcastOctets_abso)
    InBcastOctets: $InBcastOctets ($InBcastOctets_abso)"""
