### Read in the file "junos_show_arp.xml" using the "lxml" libraary and etree.parse()

```python
In [1]: from lxml import etree

In [2]: my_xml = etree.parse("junos_show_arp.xml")

In [3]: my_xml
Out[3]: <lxml.etree._ElementTree at 0x7fc57cbfdc80>
```

### a. After you have executed etree.parse() use .getroot() to find the root of the XML tree. What 'tag' is the root of this XML tree?

```python
In [5]: xml_root = my_xml.getroot()

In [6]: xml_root.tag
Out[6]: 'rpc-reply'
```

### b. Use tostring() on the root of the tree, to print out the entire XML tree. You should use .decode() to convert this from a byte string to an internal Python string (unicode string).

```python
In [10]: print(etree.tostring(xml_root).decode())
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.4R1/junos">
    <arp-table-information xmlns="http://xml.juniper.net/junos/18.4R1/junos-arp" 
junos:style="normal">
        <arp-table-entry>
            <mac-address>02:00:00:00:00:10</mac-address>
            <ip-address>128.0.0.16</ip-address>
            <hostname>fpc0</hostname>
            <interface-name>em1.0</interface-name>
            <arp-table-entry-flags>
                <none/>
            </arp-table-entry-flags>
        </arp-table-entry>
        <arp-table-entry>
            <mac-address>06:ec:49:d0:bd:27</mac-address>
            <ip-address>172.30.0.1</ip-address>
            <hostname>172.30.0.1</hostname>
            <interface-name>fxp0.0</interface-name>
            <arp-table-entry-flags>
                <none/>
            </arp-table-entry-flags>
        </arp-table-entry>
        <arp-table-entry>
            <mac-address>06:1a:97:b0:c4:89</mac-address>
            <ip-address>172.30.0.219</ip-address>
            <hostname>172.30.0.219</hostname>
            <interface-name>fxp0.0</interface-name>
            <arp-table-entry-flags>
                <none/>
            </arp-table-entry-flags>
        </arp-table-entry>
        <arp-entry-count>3</arp-entry-count>
    </arp-table-information>
    <cli>
        <banner/>
    </cli>
</rpc-reply>
```

### c. Loop over xml_root using .getchildren and print out the two nodes (tag names) of the two direct children.

```python
In [12]: for child in xml_root.getchildren():
    ...:     print(child.tag)
    ...: 
{http://xml.juniper.net/junos/18.4R1/junos-arp}arp-table-information
cli
```
