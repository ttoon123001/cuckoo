# Copyright (C) 2017 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file "docs/LICENSE" for copying permission.

from cuckoo.processing.platform.linux import StapParser
import datetime


def test_staplog():
    with open("files/stap.log") as fd:
        assert list(StapParser(fd)) == [
            {
                "api": "execve",
                "arguments": {
                    "p0": "/usr/bin/sh",
                    "p1": ["sh", "-c", "/tmp/helloworld.sh"],
                    "p2": "[/* 7 vars */]"
                },
                "instruction_pointer": "b774dcf9",
                "pid": 680,
                "process_name": "python",
                "raw": "Mon Jun 19 16:58:31 2017.445170 python@b774dcf9[680] execve(\"/usr/bin/sh\", [\"sh\", \"-c\", \"/tmp/helloworld.sh\"], [/* 7 vars */]) = -2 (ENOENT)\n",
                "return_value": "-2",
                "status": "ENOENT",
                "time": datetime.datetime(2017, 6, 19, 16, 58, 31, 445170),
                "type": "apicall"
            },
            {
                "api": "brk",
                "arguments": {
                    "p0": "0x0"
                },
                "instruction_pointer": "b77825f7",
                "pid": 680,
                "process_name": "sh",
                "raw": "Mon Jun 19 16:58:31 2017.517266 sh@b77825f7[680] brk(0x0) = -2118402048\n",
                "return_value": "-2118402048",
                "status": "",
                "time": datetime.datetime(2017, 6, 19, 16, 58, 31, 517266),
                "type": "apicall"
            },
            {
                "api": "access",
                "arguments": {
                    "p0": "/etc/ld.so.nohwcap",
                    "p1": "F_OK"
                },
                "instruction_pointer": "b77838c1",
                "pid": 680,
                "process_name": "sh",
                "raw": "Mon Jun 19 16:58:31 2017.521264 sh@b77838c1[680] access(\"/etc/ld.so.nohwcap\", F_OK) = -2 (ENOENT)\n",
                "return_value": "-2",
                "status": "ENOENT",
                "time": datetime.datetime(2017, 6, 19, 16, 58, 31, 521264),
                "type": "apicall"},
            {
                "api": "mmap2",
                "arguments": {
                    "p0": "0x0",
                    "p1": "12288",
                    "p2": "PROT_READ|PROT_WRITE",
                    "p3": "MAP_PRIVATE|MAP_ANONYMOUS",
                    "p4": "-1",
                    "p5": "0"
                },
                "instruction_pointer": "b7783970",
                "pid": 680,
                "process_name": "sh",
                "raw": "Mon Jun 19 16:58:31 2017.550890 sh@b7783970[680] mmap2(0x0, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7764000\n",
                "return_value": "0xb7764000",
                "status": "",
                "time": datetime.datetime(2017, 6, 19, 16, 58, 31, 550890),
                "type": "apicall"
            },
            {
                "api": "write",
                "arguments": {
                    "p0": "1",
                    "p1": "h3ll0 w0rld!\n",
                    "p2": "13"
                },
                "instruction_pointer": "b7768cf9",
                "pid": 681,
                "process_name": "helloworld.sh",
                "raw": "Mon Jun 19 16:58:32 2017.036988 helloworld.sh@b7768cf9[681] write(1, \"h3ll0 w0rld!\\n\", 13) = 13\n",
                "return_value": "13",
                "status": "",
                "time": datetime.datetime(2017, 6, 19, 16, 58, 32, 36988),
                "type": "apicall"
            },
            {
                "api": "read",
                "arguments": {
                    "p0": "10",
                    "p1": "0x800665c0",
                    "p2": "8192"
                },
                "instruction_pointer": "b7768cf9",
                "pid": 681,
                "process_name": "helloworld.sh",
                "raw": "Mon Jun 19 16:58:32 2017.037596 helloworld.sh@b7768cf9[681] read(10, 0x800665c0, 8192) = 0\n",
                "return_value": "0",
                "status": "",
                "time": datetime.datetime(2017, 6, 19, 16, 58, 32, 37596),
                "type": "apicall"
            },
            {
                "api": "exit_group",
                "arguments": {
                    "p0": "0"
                },
                "instruction_pointer": "b7768cf9",
                "pid": 681,
                "process_name": "helloworld.sh",
                "raw": "Mon Jun 19 16:58:32 2017.037898 helloworld.sh@b7768cf9[681] exit_group(0) =\n",
                "return_value": "",
                "status": "",
                "time": datetime.datetime(2017, 6, 19, 16, 58, 32, 37898),
                "type": "apicall"
            },
            {
                "api": "wait4",
                "arguments": {
                    "p0": "-1",
                    "p1": "0xbfd4a134",
                    "p2": "0x0",
                    "p3": "0x0"
                },
                "instruction_pointer": "b7769cf9",
                "pid": 680,
                "process_name": "sh",
                "raw": "Mon Jun 19 16:58:31 2017.850098 sh@b7769cf9[680] wait4(-1, 0xbfd4a134, 0x0, 0x0) = 681\n",
                "return_value": "681",
                "status": "",
                "time": datetime.datetime(2017, 6, 19, 16, 58, 31, 850098),
                "type": "apicall"
            },
            {
                "api": "sigreturn",
                 "arguments": { },
                 "instruction_pointer": "b7769cf9",
                 "pid": 680,
                 "process_name": "sh",
                 "raw": "Mon Jun 19 16:58:32 2017.051317 sh@b7769cf9[680] sigreturn() = 681\n",
                 "return_value": "681",
                 "status": "",
                 "time": datetime.datetime(2017, 6, 19, 16, 58, 32, 51317),
                 "type": "apicall"
            },
            {
                "api": "exit_group",
                "arguments": {
                    "p0": "0"
                },
                "instruction_pointer": "b7769cf9",
                "pid": 680,
                "process_name": "sh",
                "raw": "Mon Jun 19 16:58:32 2017.051973 sh@b7769cf9[680] exit_group(0) =\n",
                "return_value": "",
                "status": "",
                "time": datetime.datetime(2017, 6, 19, 16, 58, 32, 51973),
                "type": "apicall"
            }
        ]
