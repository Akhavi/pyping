History
-------

2012-06-05
++++++++++

- Cleanup projet (by `Socketubs <http://http://www.socketubs.net/>`_):
  - Add Cli parser
  - Can be used as python library
  - Added to pypi
  - Some Fixes
  - Clean

2011-10-17
++++++++++

- `Bugfix <https://github.com/jedie/python-ping/pull/6>`_ if host is unknown

2011-10-12
++++++++++

- Merge sources and create a seperate github `repository <https://github.com/jedie/python-ping>`_ and add a simple CLI interface.

2011-09-12
++++++++++

- Bugfixes + cleanup by Jens Diemer. Tested with Ubuntu + Windows 7.

2011-09-06
++++++++++

- `Cleanup <http://www.falatic.com/index.php/39/pinging-with-python>`_ by Martin Falatic : 
  - Restored lost comments and docs. Improved functionality: constant time between pings, internal times consistently use milliseconds. Clarified annotations (e.g., in the checksum routine)
  - Using unsigned data in IP & ICMP header pack/unpack unless otherwise necessary.
  - Signal handling
  - Ping-style output formatting and stats

2011-08-03
++++++++++

- Ported to py3k by Zach Ware. Mostly done by 2to3; also minor changes to deal with bytes vs. string changes (no more ord() in checksum() because >source_string< is actually bytes, added .encode() to data in send_one_ping()). That's about it.

2010-03-11
++++++++++

- Changes by Samuel Stauffer:
  - Replaced time.clock with default_timer which is set to time.clock on windows and time.time on other systems.

2009-11-08
++++++++++

- Fixes by `George Notaras <http://www.g-loaded.eu/2009/10/30/python-ping/>`_, reported by `Chris Hallman <http://cdhallman.blogspot.com>`_: 
  - Improved compatibility with GNU/Linux systems.
  - Re-use time.time() instead of time.clock(). The 2007 implementation worked only under Microsoft Windows. Failed on GNU/Linux. time.clock() behaves differently under the two `OSes <http://docs.python.org/library/time.html#time.clock>`_.

2007-06-30
++++++++++

- Little rewrite by `Jens Diemer <http://www.python-forum.de/post-69122.html#69122>`_:
  - Change socket asterisk import to a normal import
  - Replace time.time() with time.clock()
  - Delete "return None" (or change to "return" only)
  - In checksum() rename "str" to "source_string"

2000-12-04
++++++++++

- Changed the struct.pack() calls to pack the checksum and ID as unsigned. My thanks to Jerome Poincheval for the fix.

1997-12-16
++++++++++

For some reason, the checksum bytes are in the wrong order when this is run under Solaris 2.X for SPARC but it works right under Linux x86. Since I don't know just what's wrong, I'll swap the bytes always and then do an htons().

1997-11-22
++++++++++

Initial hack. Doesn't do much, but rather than try to guess what features I (or others) will want in the future, I've only put in what I need now.
