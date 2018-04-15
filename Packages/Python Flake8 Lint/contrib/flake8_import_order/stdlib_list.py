STDLIB_NAMES = set((
    "AL",
    "BaseHTTPServer",
    "Bastion",
    "Binary",
    "Boolean",
    "CGIHTTPServer",
    "ColorPicker",
    "ConfigParser",
    "Cookie",
    "DEVICE",
    "DocXMLRPCServer",
    "EasyDialogs",
    "FL",
    "FrameWork",
    "GL",
    "HTMLParser",
    "MacOS",
    "Mapping",
    "MimeWriter",
    "MiniAEFrame",
    "Numeric",
    "Queue",
    "SUNAUDIODEV",
    "ScrolledText",
    "Sequence",
    "Set",
    "SimpleHTTPServer",
    "SimpleXMLRPCServer",
    "SocketServer",
    "StringIO",
    "Text",
    "Tix",
    "Tkinter",
    "UserDict",
    "UserList",
    "UserString",
    "__builtin__",
    "__future__",
    "__main__",
    "_dummy_thread",
    "_thread",
    "abc",
    "aepack",
    "aetools",
    "aetypes",
    "aifc",
    "al",
    "anydbm",
    "argparse",
    "array",
    "ast",
    "asynchat",
    "asyncio",
    "asyncore",
    "atexit",
    "audioop",
    "autoGIL",
    "base64",
    "bdb",
    "binascii",
    "binhex",
    "bisect",
    "bsddb",
    "builtins",
    "bz2",
    "cPickle",
    "cStringIO",
    "calendar",
    "cd",
    "cgi",
    "cgitb",
    "chunk",
    "cmath",
    "cmd",
    "code",
    "codecs",
    "codeop",
    "collections",
    "collections.abc",
    "colorsys",
    "commands",
    "compileall",
    "concurrent.futures",
    "configparser",
    "contextlib",
    "cookielib",
    "copy",
    "copy_reg",
    "copyreg",
    "crypt",
    "csv",
    "ctypes",
    "curses",
    "curses.ascii",
    "curses.panel",
    "curses.textpad",
    "curses.wrapper",
    "datetime",
    "dbhash",
    "dbm",
    "decimal",
    "difflib",
    "dircache",
    "dis",
    "distutils",
    "dl",
    "doctest",
    "dumbdbm",
    "dummy_thread",
    "dummy_threading",
    "email",
    "ensurepip",
    "enum",
    "errno",
    "faulthandler",
    "fcntl",
    "filecmp",
    "fileinput",
    "findertools",
    "fl",
    "flp",
    "fm",
    "fnmatch",
    "formatter",
    "fpectl",
    "fpformat",
    "fractions",
    "ftplib",
    "functools",
    "future_builtins",
    "gc",
    "gdbm",
    "gensuitemodule",
    "getopt",
    "getpass",
    "gettext",
    "gl",
    "glob",
    "grp",
    "gzip",
    "hashlib",
    "heapq",
    "hmac",
    "hotshot",
    "html",
    "html.entities",
    "html.parser",
    "htmlentitydefs",
    "htmllib",
    "http",
    "http.client",
    "http.cookiejar",
    "http.cookies",
    "http.server",
    "httplib",
    "ic",
    "imageop",
    "imaplib",
    "imgfile",
    "imghdr",
    "imp",
    "importlib",
    "imputil",
    "inspect",
    "io",
    "ipaddress",
    "itertools",
    "jpeg",
    "json",
    "keyword",
    "linecache",
    "locale",
    "logging",
    "logging.config",
    "logging.handlers",
    "lzma",
    "macostools",
    "macpath",
    "macurl2path",
    "mailbox",
    "mailcap",
    "marshal",
    "math",
    "md5",
    "mhlib",
    "mimetools",
    "mimetypes",
    "mimify",
    "mmap",
    "modulefinder",
    "msilib",
    "multifile",
    "multiprocessing",
    "mutex",
    "netrc",
    "new",
    "nis",
    "nntplib",
    "nturl2path",
    "numbers",
    "operator",
    "optparse",
    "os",
    "os.path",
    "ossaudiodev",
    "parser",
    "pathlib",
    "pdb",
    "pickle",
    "pickletools",
    "pipes",
    "pkgutil",
    "platform",
    "plistlib",
    "popen2",
    "poplib",
    "posix",
    "posixfile",
    "posixpath",
    "pprint",
    "pty",
    "pwd",
    "py_compile",
    "pyclbr",
    "pydoc",
    "queue",
    "quopri",
    "random",
    "re",
    "readline",
    "repr",
    "reprlib",
    "resource",
    "rexec",
    "rfc822",
    "rlcompleter",
    "robotparser",
    "runpy",
    "sched",
    "select",
    "sets",
    "sgmllib",
    "sha",
    "shelve",
    "shlex",
    "shutil",
    "signal",
    "site",
    "smtpd",
    "smtplib",
    "sndhdr",
    "socket",
    "socketserver",
    "spwd",
    "sqlite3",
    "ssl",
    "stat",
    "statistics",
    "statvfs",
    "string",
    "stringprep",
    "struct",
    "subprocess",
    "sunau",
    "sunaudiodev",
    "symbol",
    "symtable",
    "sys",
    "sysconfig",
    "syslog",
    "tabnanny",
    "tarfile",
    "telnetlib",
    "tempfile",
    "termios",
    "test",
    "test.support",
    "test.test_support",
    "textwrap",
    "thread",
    "threading",
    "time",
    "timeit",
    "tkinter",
    "tkinter.scrolledtext",
    "tkinter.tix",
    "tkinter.ttk",
    "token",
    "tokenize",
    "trace",
    "traceback",
    "tracemalloc",
    "ttk",
    "tty",
    "turtle",
    "types",
    "unicodedata",
    "unittest",
    "unittest.mock",
    "urllib",
    "urllib.error",
    "urllib.parse",
    "urllib.request",
    "urllib.response",
    "urllib.robotparser",
    "urllib2",
    "urlparse",
    "user",
    "uu",
    "uuid",
    "venv",
    "warnings",
    "wave",
    "weakref",
    "webbrowser",
    "whichdb",
    "winsound",
    "wsgiref",
    "xdrlib",
    "xml",
    "xmlrpclib",
    "zipfile",
    "zipimport",
    "zlib",
))
