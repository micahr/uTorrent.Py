#	UTORRENT CONSTANTS
#	modify these at your own peril
UT_DEBUG					= True

#	file priorities
UT_FILE_PRIO_SKIP 				= r'0'
UT_FILE_PRIO_LOW 				= r'1'
UT_FILE_PRIO_NORMAL 			= r'2'
UT_FILE_PRIO_HIGH 				= r'3'

#	torrent states
UT_TORRENT_STATE_START			= 0x00
UT_TORRENT_STATE_FORCESTART		= 0x01
UT_TORRENT_STATE_PAUSE      	= 0x02
UT_TORRENT_STATE_STOP       	= 0x03

#	individual torrent properties
UT_TORRENT_DETAIL_HASH 			= 0
UT_TORRENT_DETAIL_TRACKERS 		= 1
UT_TORRENT_DETAIL_ULRATE 		= 2
UT_TORRENT_DETAIL_DLRATE 		= 3
UT_TORRENT_DETAIL_SUPERSEED 	= 4
UT_TORRENT_DETAIL_DHT 			= 5
UT_TORRENT_DETAIL_PEX 			= 6
UT_TORRENT_DETAIL_SEED_OVERRIDE	= 7
UT_TORRENT_DETAIL_SEED_RATIO 	= 8
UT_TORRENT_DETAIL_SEED_TIME 	= 9
UT_TORRENT_DETAIL_ULSLOTS 		= 10


#	torrent info/stats
UT_TORRENT_PROP_HASH        	= 0
UT_TORRENT_PROP_NAME        	= 2
UT_TORRENT_PROP_LABEL			= 11
UT_TORRENT_PROP_STATE			= 1
UT_TORRENT_STAT_BYTES_SIZE		= 3
UT_TORRENT_STAT_BYTES_LEFT		= 18
UT_TORRENT_STAT_BYTES_RECV		= 5
UT_TORRENT_STAT_BYTES_SENT		= 6
UT_TORRENT_STAT_SPEED_UP    	= 8
UT_TORRENT_STAT_SPEED_DOWN 		= 9
UT_TORRENT_STAT_P1000_DONE		= 4
UT_TORRENT_STAT_ETA				= 10
UT_TORRENT_STAT_AVAILABLE		= 16
UT_TORRENT_STAT_QUEUE_POS		= 17
UT_TORRENT_STAT_RATIO			= 7
UT_TORRENT_STAT_SEED_AVAIL		= 15
UT_TORRENT_STAT_PEER_AVAIL  	= 13
UT_TORRENT_STAT_SEED_CONN		= 14
UT_TORRENT_STAT_PEER_CONN		= 12
