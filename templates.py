#!/usr/bin/python2.6

header="""          [Delta Hammer] 
info from '$command' every $delta sec
Start: $start_time | Current: $current_time
Page: $current_page/$last_page

"""

link="""[$name] $ips
    RX  bytes: $rx_bytes ($rx_bytes_abso)
        packets: $rx_packets ($rx_packets_abso)
        errors:$rx_errors ($rx_errors_abso) dropped:$rx_dropped ($rx_dropped_abso) overrun:$rx_overrun ($rx_overrun_abso) mcast:$rx_mcast ($rx_mcast_abso)
    TX  bytes: $tx_bytes ($tx_bytes_abso)
        packets: $tx_packets ($tx_packets_abso)
        errors:$tx_errors ($tx_errors_abso) dropped:$tx_dropped ($tx_dropped_abso) carrier:$tx_carrier ($tx_carrier_abso) collsns:$tx_collsns ($tx_collsns_abso)"""


ip="""SYN_RECV count: $syn_recv_count ($syn_recv_count_abso)

Ip:
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
    InNoRoutes: $InNoRoutes ($InNoRoutes_abso)
    InMcastPkts: $InMcastPkts ($InMcastPkts_abso)
    OutMcastPkts: $OutMcastPkts ($OutMcastPkts_abso)
    InBcastPkts: $InBcastPkts ($InBcastPkts_abso)
    InOctets: $InOctets ($InOctets_abso)
    OutOctets: $OutOctets ($OutOctets_abso)
    InMcastOctets: $InMcastOctets ($InMcastOctets_abso)
    OutMcastOctets: $OutMcastOctets ($OutMcastOctets_abso)
    InBcastOctets: $InBcastOctets ($InBcastOctets_abso)"""

tcpv="""Tcp:
    $activeconnectionsopenings ($activeconnectionsopenings_abso) active connections openings
    $passiveconnectionopenings ($passiveconnectionopenings_abso) passive connection openings
    $failedconnectionattempts ($failedconnectionattempts_abso) failed connection attempts
    $connectionresetsreceived ($connectionresetsreceived_abso) connection resets received
    $connectionsestablished ($connectionsestablished_abso) connections established
    $segmentsreceived ($segmentsreceived_abso) segments received
    $segmentssendout ($segmentssendout_abso) segments send out
    $segmentsretransmited ($segmentsretransmited_abso) segments retransmited
    $badsegmentsreceived ($badsegmentsreceived_abso) bad segments received.
    $resetssent ($resetssent_abso) resets sent
TcpExt:
    $SYNcookiessent ($SYNcookiessent_abso) SYN cookies sent
    $SYNcookiesreceived ($SYNcookiesreceived_abso) SYN cookies received
    $invalidSYNcookiesreceived ($invalidSYNcookiesreceived_abso) invalid SYN cookies received
    $resetsreceivedforembryonicSYNRECVsockets ($resetsreceivedforembryonicSYNRECVsockets_abso) resets received for embryonic SYN_RECV sockets
    $packetsprunedfromreceivequeuebecauseofsocketbufferoverrun ($packetsprunedfromreceivequeuebecauseofsocketbufferoverrun_abso) packets pruned from receive queue because of socket buffer overrun
    $packetsprunedfromreceivequeue ($packetsprunedfromreceivequeue_abso) packets pruned from receive queue
    $packetsdroppedfromoutoforderqueuebecauseofsocketbufferoverrun ($packetsdroppedfromoutoforderqueuebecauseofsocketbufferoverrun_abso) packets dropped from out-of-order queue because of socket buffer overrun
    $ICMPpacketsdroppedbecausetheywereoutofwindow ($ICMPpacketsdroppedbecausetheywereoutofwindow_abso) ICMP packets dropped because they were out-of-window
    $ICMPpacketsdroppedbecausesocketwaslocked ($ICMPpacketsdroppedbecausesocketwaslocked_abso) ICMP packets dropped because socket was locked
    $TCPsocketsfinishedtimewaitinfasttimer ($TCPsocketsfinishedtimewaitinfasttimer_abso) TCP sockets finished time wait in fast timer
    $timewaitsocketsrecycledbytimestamp ($timewaitsocketsrecycledbytimestamp_abso) time wait sockets recycled by time stamp
    $TCPsocketsfinishedtimewaitinslowtimer ($TCPsocketsfinishedtimewaitinslowtimer_abso) TCP sockets finished time wait in slow timer
    $packetsrejectsinestablishedconnectionsbecauseoftimestamp ($packetsrejectsinestablishedconnectionsbecauseoftimestamp_abso) packets rejects in established connections because of timestamp
    $delayedackssent ($delayedackssent_abso) delayed acks sent
    $delayedacksfurtherdelayedbecauseoflockedsocket ($delayedacksfurtherdelayedbecauseoflockedsocket_abso) delayed acks further delayed because of locked socket
    Quick ack mode was activated $Quickackmodewasactivatedtimes ($Quickackmodewasactivatedtimes_abso) times
    $timesthelistenqueueofasocketoverflowed ($timesthelistenqueueofasocketoverflowed_abso) times the listen queue of a socket overflowed
    $SYNstoLISTENsocketsignored ($SYNstoLISTENsocketsignored_abso) SYNs to LISTEN sockets ignored
    $packetsdirectlyqueuedtorecvmsgprequeue ($packetsdirectlyqueuedtorecvmsgprequeue_abso) packets directly queued to recvmsg prequeue.
    $bytesdirectlyreceivedinprocesscontextfromprequeue ($bytesdirectlyreceivedinprocesscontextfromprequeue_abso) bytes directly received in process context from prequeue
    $packetsdirectlyreceivedfrombacklog ($packetsdirectlyreceivedfrombacklog_abso) packets directly received from backlog
    $packetsdirectlyreceivedfromprequeue ($packetsdirectlyreceivedfromprequeue_abso) packets directly received from prequeue
    $packetsdroppedfromprequeue ($packetsdroppedfromprequeue_abso) packets dropped from prequeue
    $packetsheaderpredicted ($packetsheaderpredicted_abso) packet headers predicted
    $packetheaderspredicted ($packetheaderspredicted_abso) packet headers predicted
    $packetsheaderpredictedanddirectlyqueuedtouser ($packetsheaderpredictedanddirectlyqueuedtouser_abso) packets header predicted and directly queued to user
    $acknowledgmentsnotcontainingdatareceived ($acknowledgmentsnotcontainingdatareceived_abso) acknowledgments not containing data payload received
    $acknowledgmentsnotcontainingdatapayloadreceived ($acknowledgmentsnotcontainingdatapayloadreceived_abso) acknowledgments not containing data payload received
    $predictedacknowledgments ($predictedacknowledgments_abso) predicted acknowledgments
    $timesrecoveredfrompacketlossbyselectiveacknowledgements ($timesrecoveredfrompacketlossbyselectiveacknowledgements_abso) times recovered from packet loss by selective acknowledgements
    $timesrecoveredfrompacketlossduetofastretransmit ($timesrecoveredfrompacketlossduetofastretransmit_abso) times recovered from packet loss due to fast retransmit
    $timesrecoveredfrompacketlossduetoSACKdata ($timesrecoveredfrompacketlossduetoSACKdata_abso) times recovered from packet loss due to SACK data
    $badSACKsreceived ($badSACKsreceived_abso) bad SACKs received
    Detected reordering $DetectedreorderingtimesusingFACK ($DetectedreorderingtimesusingFACK_abso) times using FACK
    Detected reordering $DetectedreorderingtimesusingSACK ($DetectedreorderingtimesusingSACK_abso) times using SACK
    Detected reordering $Detectedreorderingtimesusingrenofastretransmit ($Detectedreorderingtimesusingrenofastretransmit_abso) times using reno fast retransmit
    Detected reordering $Detectedreorderingtimesusingtimestamp ($Detectedreorderingtimesusingtimestamp_abso) times using time stamp
    $congestionwindowsfullyrecovered ($congestionwindowsfullyrecovered_abso) congestion windows fully recovered
    $congestionwindowspartiallyrecoveredusingHoeheuristic ($congestionwindowspartiallyrecoveredusingHoeheuristic_abso) congestion windows partially recovered using Hoe heuristic
    TCPDSACKUndo: $TCPDSACKUndo ($TCPDSACKUndo_abso)
    $congestionwindowsrecoveredwithoutslowstartbyDSACK ($congestionwindowsrecoveredwithoutslowstartbyDSACK_abso) congestion windows recovered without slow start by DSACK
    $congestionwindowsrecoveredwithoutslowstartafterpartialack ($congestionwindowsrecoveredwithoutslowstartafterpartialack_abso) congestion windows recovered without slow start after partial ack
    $congestionwindowsrecoveredafterpartialack ($congestionwindowsrecoveredafterpartialack_abso) congestion windows recovered after partial ack
    $TCPdatalossevents ($TCPdatalossevents_abso) TCP data loss events
    TCPLostRetransmit: $TCPLostRetransmit ($TCPLostRetransmit_abso)
    $timeoutsafterrenofastretransmit ($timeoutsafterrenofastretransmit_abso) timeouts after reno fast retransmit
    $timeoutsafterSACKrecovery ($timeoutsafterSACKrecovery_abso) timeouts after SACK recovery
    $timeoutsinlossstate ($timeoutsinlossstate_abso) timeouts in loss state
    $fastretransmits ($fastretransmits_abso) fast retransmits
    $forwardretransmits ($forwardretransmits_abso) forward retransmits
    $retransmitsinslowstart ($retransmitsinslowstart_abso) retransmits in slow start
    $otherTCPtimeouts ($otherTCPtimeouts_abso) other TCP timeouts
    TCPRenoRecoveryFail: $TCPRenoRecoveryFail ($TCPRenoRecoveryFail_abso)
    $sackretransmitsfailed ($sackretransmitsfailed_abso) sack retransmits failed
    $timesreceiverscheduledtoolatefordirectprocessing ($timesreceiverscheduledtoolatefordirectprocessing_abso) times receiver scheduled too late for direct processing
    $packetscollapsedinreceivequeueduetolowsocketbuffer ($packetscollapsedinreceivequeueduetolowsocketbuffer_abso) packets collapsed in receive queue due to low socket buffer
    $DSACKssentforoldpackets ($DSACKssentforoldpackets_abso) DSACKs sent for old packets
    $DSACKssentforoutoforderpackets ($DSACKssentforoutoforderpackets_abso) DSACKs sent for out of order packets
    $DSACKsreceived ($DSACKsreceived_abso) DSACKs received
    $DSACKsforoutoforderpacketsreceived ($DSACKsforoutoforderpacketsreceived_abso) DSACKs for out of order packets received
    $connectionsresetduetounexpectedSYN ($connectionsresetduetounexpectedSYN_abso) connections reset due to unexpected SYN
    $connectionsresetduetounexpecteddata ($connectionsresetduetounexpecteddata_abso) connections reset due to unexpected data
    $connectionsresetduetoearlyuserclose ($connectionsresetduetoearlyuserclose_abso) connections reset due to early user close
    $connectionsabortedduetotimeout ($connectionsabortedduetotimeout_abso) connections aborted due to timeout
    $timesunabledtosendRSTduetonomemory ($timesunabledtosendRSTduetonomemory_abso) times unabled to send RST due to no memory
    TCP ran low on memory $TCPranlowonmemorytimes ($TCPranlowonmemorytimes_abso) times
    TCPSACKDiscard: $TCPSACKDiscard ($TCPSACKDiscard_abso) 
    TCPDSACKIgnoredOld: $TCPDSACKIgnoredOld ($TCPDSACKIgnoredOld_abso) 
    TCPDSACKIgnoredNoUndo: $TCPDSACKIgnoredNoUndo ($TCPDSACKIgnoredNoUndo_abso) 
    TCPSpuriousRTOs: $TCPSpuriousRTOs ($TCPSpuriousRTOs_abso) 
    TCPSackShifted: $TCPSackShifted ($TCPSackShifted_abso) 
    TCPSackMerged: $TCPSackMerged ($TCPSackMerged_abso) 
    TCPSackShiftFallback: $TCPSackShiftFallback ($TCPSackShiftFallback_abso) 
    TCPBacklogDrop: $TCPBacklogDrop ($TCPBacklogDrop_abso)
    TCPRcvCoalesce: $TCPRcvCoalesce ($TCPRcvCoalesce_abso)
    TCPOFOQueue: $TCPOFOQueue ($TCPOFOQueue_abso)
    TCPChallengeACK: $TCPChallengeACK ($TCPChallengeACK_abso)
    TCPSYNChallenge: $TCPSYNChallenge ($TCPSYNChallenge_abso)"""
