Projeto básico usando python-nmap, o que ele faz é um scan na rede do ip colocado, se você tem um conhecimento maior no nmap é possível executar uns scripts melhores com o próprio nmap.

tipos de scan:
-sS	nmap 192.168.1.1 -sS	TCP SYN port scan (Default)
-sT	nmap 192.168.1.1 -sT	TCP connect port scan (Default without root privilege)
-sU	nmap 192.168.1.1 -sU	UDP port scan
-sA	nmap 192.168.1.1 -sA	TCP ACK port scan
-sW	nmap 192.168.1.1 -sW	TCP Window port scan
-sM	nmap 192.168.1.1 -sM	TCP Maimon port scan
