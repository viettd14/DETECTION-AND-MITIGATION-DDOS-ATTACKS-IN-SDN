from mininet.topo import Topo
from mininet.net import Mininet
# from mininet.node import CPULimitedHost
from mininet.link import TCLink
# from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSKernelSwitch, RemoteController
# from time import sleep

class MyTopo( Topo ):

    def build( self ):

        s1 = self.addSwitch( 's1', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h1 = self.addHost( 'h1', cpu=1.0/20,mac="00:00:00:00:00:01", ip="10.0.0.1/24" )
        h2 = self.addHost( 'h2', cpu=1.0/20, mac="00:00:00:00:00:02", ip="10.0.0.2/24" )   

        s2 = self.addSwitch( 's2', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h3 = self.addHost( 'h3', cpu=1.0/20, mac="00:00:00:00:00:03", ip="10.0.0.3/24" ) 
        h4 = self.addHost( 'h4', cpu=1.0/20, mac="00:00:00:00:00:04", ip="10.0.0.4/24" )


        s3 = self.addSwitch( 's3', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h5 = self.addHost( 'h5', cpu=1.0/20, mac="00:00:00:00:00:05", ip="10.0.0.5/24" )
        h6 = self.addHost( 'h6', cpu=1.0/20, mac="00:00:00:00:00:06", ip="10.0.0.6/24" )

        # Add links

        self.addLink( h1, s1 )
        self.addLink( h2, s1 )

        self.addLink( h3, s2 )
        self.addLink( h4, s2 )

        self.addLink( h5, s3 )
        self.addLink( h6, s3 )

        self.addLink( s1, s2 )
        self.addLink( s2, s3 )

def startNetwork():

    topo = MyTopo()
    c0 = RemoteController('c0', ip='192.168.0.104', port=6653)
    net = Mininet(topo=topo, link=TCLink, controller=c0)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    startNetwork()

topos = {'mytopo': MyTopo}
