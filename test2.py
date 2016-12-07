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
        
    def test_grep_vmlog(self):
        # Infrequent Grep on vm.log to test from client to one server
        logging.info("Test1: Infrequent Grep - Client to 1 Server")
        unix_cmd = 'grep slip4063.sirius.com /usr/local/mp1/vm.log'
        recv = client.main_sub("testone.txt", unix_cmd)        
        exp = 1   
        self.assertEqual(recv,exp)  
        logging.info("Test1 Complete : Test for infrequent pattern on vm.log")

    def test_grep_m_vmlog(self):
        # Infrequent Grep on vm.log to test from client to four server
        logging.info("Test2: Infrequent Grep - Client to 1 Server")
        unix_cmd = 'grep slip4063.sirius.com /usr/local/mp1/vm.log'
        recv = client.main_sub("testfour.txt", unix_cmd)        
        exp = 2   
        self.assertEqual(recv,exp)  
        logging.info("Test2 Complete : Test for infrequent pattern on vm.log")

    def test_grep_a_vmlog(self):
        # Infrequent Grep on vm.log to test from client to seven servers
        logging.info("Test3: Infrequent Grep - Client to 7 Servers")
        unix_cmd = 'grep slip4063.sirius.com /usr/local/mp1/vm.log'
        recv = client.main_sub("server-names.txt", unix_cmd)        
        exp = 2   
        self.assertEqual(recv,exp)  
        logging.info("Test3 Complete : Test for infrequent pattern on vm.log")
    
    def tearDown(self):
        sys.stdout = self.held
        
        
if __name__ == "__main__":
    # Create a log file for the results
    logging.basicConfig(filename = "unittest2.log", level = logging.INFO, filemode = "w")
    unittest.main()
