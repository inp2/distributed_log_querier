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
    
    def test_fgrep_vmlog(self):
        # Frequent grep on vm.log to test from client to one server
        logging.info("Test1: Frequent Grep - Client to 1 Server")
        unix_cmd = 'grep .gif /usr/local/mp1/vm.log'
        recv = client.main_sub("testone.txt", unix_cmd)        
        exp = 111997 
        self.assertEqual(recv,exp)  
        logging.info("Test1 Complete : Test for frequent pattern on vm.log")

    def tearDown(self):
        sys.stdout = self.held
        
        
if __name__ == "__main__":
    logging.basicConfig(filename = "unitest6.log", level = logging.INFO, filemode = "w")
    unittest.main()
