#### Yakob Yakov (R) GPU v3
import datetime 
from datetime import datetime
import jpype
from jpype import java
from jpype import javax
import os, sys, time
import json

HOST='localhost'
PORT=8386
USER='admin'
PASS='mypass'

URL = "service:jmx:rmi:///jndi/rmi://%s:%d/jmxrmi" % (HOST, PORT)
jpype.startJVM("/System/Library/Frameworks/JavaVM.framework/Libraries/libjvm_compat.dylib")
java.lang.System.out.println("JVM load OK")
while true:

    jhash = java.util.HashMap()
    jarray=jpype.JArray(java.lang.String)([USER,PASS])
    jhash.put (javax.management.remote.JMXConnector.CREDENTIALS, jarray);
    jmxurl = javax.management.remote.JMXServiceURL(URL)
    jmxsoc = javax.management.remote.JMXConnectorFactory.connect(jmxurl,jhash)
    connection = jmxsoc.getMBeanServerConnection();

    object="java.lang:type=Threading"
    attribute="ThreadCount"
    attr=connection.getAttribute(javax.management.ObjectName(object),attribute)
    print  attribute, attr

    object="java.lang:type=Memory"
    attribute="HeapMemoryUsage"
    attr=connection.getAttribute(javax.management.ObjectName(object),attribute)
    used_memory = attr.contents.get("used")

    import socket
    hostname = socket.gethostname()
    print hostname
    a['Hostname'] = hostname
    b['Used Memory'] = used_memory
    c =  time.time()

    metronome = json.dumps(a, b, c) 

    req = requests.post('http://elasticsearch:9200/index/name',data=metronome(item,'rb').read())
    time.sleep(10)