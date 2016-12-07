import sys
import unittest
from io import StringIO
import logging
import client
import os
import subprocess


class test_sample(unittest.TestCase):
    def setUp(self):
        
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_sgrep_vmlog(self):
        # Semi-frequent grep on vm.log to test from client to 1 server
        logging.info("Test1: Semi-Frequent Grep - Client to 1 Server")
        unix_cmd = 'grep russadam.clark.net /usr/local/mp1/vm.log'
        recv = client.main_sub("testone.txt", unix_cmd)        
        exp = 27
        self.assertEqual(recv,exp)  
        logging.info("Test1 Complete : Test for Semi-Frequent Grep on vm.log")

    def test_sgrep_m_vmlog(self):
        # Semi-frequent grep on vm.log to test from client to 1 server
        logging.info("Test2: Semi-Frequent Grep - Client to 4 Servers")
        unix_cmd = 'grep russadam.clark.net /usr/local/mp1/vm.log'
        recv = client.main_sub("testfour.txt", unix_cmd)        
        exp = 139
        self.assertEqual(recv,exp)  
        logging.info("Test2 Complete : Test for Semi-Frequent Grep on vm.log")

    def test_sgrep_a_vmlog(self):
        # Semi-frequent grep on vm.log to test from client to 1 server
        logging.info("Test3: Semi-Frequent Grep - Client to 7 Servers")
        unix_cmd = 'grep russadam.clark.net /usr/local/mp1/vm.log'
        recv = client.main_sub("server-names.txt", unix_cmd)        
        exp = 154
        self.assertEqual(recv,exp)  
        logging.info("Test3 Complete : Test for Semi-Frequent Grep on vm.log")
    
    def tearDown(self):
        sys.stdout = self.held
        
if __name__ == "__main__":
    # Create a log
    logging.basicConfig(filename = "unittest3.log", level = logging.INFO, filemode = "w")
    unittest.main()
