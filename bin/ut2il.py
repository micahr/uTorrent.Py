#!/usr/bin/env python
# -*- coding: utf-8 -*-

#	ut2il.py
#	Copyright (C) 2006-2010 Rob Crowther <weilawei@gmail.com>
#
#	This library is free software; you can redistribute it and/or modify
# 	it under the terms of the GNU Lesser General Public License as
#	published by the Free Software Foundation; either version 2.1 of the
#	License, or (at your option) any later version.
#
#	This library is distributed in the hope that it will be useful, but
#	WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#	Lesser General Public License for more details.
#
#	You should have received a copy of the GNU Lesser General Public 
#	License along with this library; if not, write to the Free Software 
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


#	ut2il.py is a set of methods (with command line opts) to display useful
#	development/debugging information from �Torrent

#	ut2il.py <- �T util (the name derivation) [makes it easier to tab to]

#   % ut2il.py --help
#	Usage: ut2il.py [options]
#
#	Options:
#	--version             show program's version number and exit
#  	-h, --help            show this help message and exit
#  	-m HOST, --host=HOST  set the webui host
#  	-p PORT, --port=PORT  set the webui port
# 	-u USERNAME, --username=USERNAME
#                         set the webui username
#  	-k PASSWORD, --password=PASSWORD
#                         set the webui password
#  	-g, --go              start all loaded torrents
#  	-f, --files           list all files
#  	-q, --qstats          display uTorrent quick stats
#  	-s, --settings        display uTorrent settings

#####################################################################
#                                                                   #
#	SET YOUR WEBUI VARIABLES!!!                                     #
#																	#
#####################################################################

host 		= 'localhost'
port 		= '44800'
username 	= 'admin'
password 	= 'passy'

#####################################################################
#                                                                   #
#	DONE! GET ON WITH YOUR LIFE! CODE, FOR GODS'S SAKE MAN! CODE!	#
#                                                                   #
#####################################################################

from uTorrent import *
from optparse import OptionParser

parser = OptionParser(version="%prog 0.1.0")

parser.add_option("-m", "--host", action='store', dest='host', help='set the webui host')
parser.add_option("-p", "--port", action='store', dest='port', help='set the webui port')
parser.add_option("-u", "--username", action='store', dest='username', help='set the webui username')
parser.add_option("-k", "--password", action='store', dest='password', help='set the webui password')
parser.add_option("-g", "--go", action='store_true', dest='is_start_all', help='start all loaded torrents')
parser.add_option("-f", "--files", action='store_true', dest='is_list_files', help='list all files')
parser.add_option("-q", "--qstats", action='store_true', dest='is_quick_stats', help='display uTorrent quick stats')
parser.add_option("-s", "--settings", action='store_true', dest='is_list_settings', help='display uTorrent settings')
parser.set_defaults(host=host)
parser.set_defaults(port=port)
parser.set_defaults(username=username)
parser.set_defaults(password=password)
parser.set_defaults(is_start_all=False)
parser.set_defaults(is_list_files=False)
parser.set_defaults(is_quick_stats=False)
parser.set_defaults(is_list_settings=False)

(options, args) = parser.parse_args()
uTorrent_handle = uTorrent(host=options.host, port=options.port, username=options.username, password=options.password)

def start_torrents():
	current_torrents = uTorrent_handle.webui_ls()

	for torrent in current_torrents:
		uTorrent_handle.webui_start_torrent(torrent[UT_TORRENT_PROP_HASH])

def list_files():
	current_torrents = uTorrent_handle.uls_torrents()

	for torrent in current_torrents:
		file_list = uTorrent_handle.uls_files(torrent_name=torrent)

		for file_name in file_list:
			print "[%s] - %s" % (torrent, file_name)

def list_settings():
	for setting in uTorrent_handle.webui_get():
		print "[%s] %s" % (setting[0], setting[2])

def quick_stats():
	current_torrents 	= uTorrent_handle.webui_ls()

	print '\n uTorrent Quick Stats'

	for torrent in current_torrents:
		print "\n [QUEUE]  %s" 				% torrent[UT_TORRENT_STAT_QUEUE_POS]
		print " [NAME]   %s" 				% torrent[UT_TORRENT_PROP_NAME]
		print " [HASH]   %s" 				% torrent[UT_TORRENT_PROP_HASH]
		print " [LABLE]  %s" 				% torrent[UT_TORRENT_PROP_LABEL]
		print " [STATE]  %s" 				% torrent[UT_TORRENT_PROP_STATE]
		print " [SIZE]   %s bytes" 			% torrent[UT_TORRENT_STAT_BYTES_SIZE]
		print " [LEFT]   %s bytes" 			% torrent[UT_TORRENT_STAT_BYTES_LEFT]
		print " [RECV]   %s bytes" 			% torrent[UT_TORRENT_STAT_BYTES_RECV]
		print " [SENT]   %s bytes" 			% torrent[UT_TORRENT_STAT_BYTES_SENT]
		print " [DOWN]   %s kB/s" 			% (float(torrent[UT_TORRENT_STAT_SPEED_DOWN]) / 1000)
		print " [UP]     %s kB/s" 			% (float(torrent[UT_TORRENT_STAT_SPEED_UP]) / 1000)
		print " [DONE]   %s%% done" 		% (float(torrent[UT_TORRENT_STAT_P1000_DONE]) / 10)
		print " [SEEDS]  %s of %s active" 	% (torrent[UT_TORRENT_STAT_SEED_CONN], torrent[UT_TORRENT_STAT_SEED_AVAIL])
		print " [PEERS]  %s of %s active" 	% (torrent[UT_TORRENT_STAT_PEER_CONN], torrent[UT_TORRENT_STAT_PEER_AVAIL])
		print " [ETA]    %s seconds"		% torrent[UT_TORRENT_STAT_ETA]
		print " [AVAIL]  %s" 				% torrent[UT_TORRENT_STAT_AVAILABLE]
		print " [RATIO]  %s" 				% (float(torrent[UT_TORRENT_STAT_RATIO]) / 1000)

if (options.is_start_all == True):
	start_torrents()
	
if (options.is_list_files == True):
	list_files()
	
if (options.is_quick_stats == True):
	quick_stats()
	
if (options.is_list_settings == True):
	list_settings()
