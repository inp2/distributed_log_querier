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

    # Test for infrequent pattern with regex
    def test_grep_infreq(self):
        logging.info("Test1 Begins : Test for infrequent pattern with regex")
        unix_cmd = 'grep "\[31\/[a-zA-Z]\{3\}\/1995:23:16:" /usr/local/mp1/test_log.log'
        client.main_sub("server-names-test.txt", unix_cmd)
        recv_res = (sys.stdout.getvalue()).split("\n")        
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'exp-results/exp_results_infreq_regex.txt')
        exp_result_file = open(filename, "rb")
        exp_res_lines = exp_result_file.readlines()   
        exp_res = []
        exp_result_file.close()
        for line in exp_res_lines:
            line1 = line.strip(b'\n')
            exp_res.append(line1.decode())
            logging.info(line1.decode())
        logging.info("Received result")       
        recv_res_f = recv_res
        final_res = []
        recv_res_f[len(recv_res)-1] = recv_res[len(recv_res)-1].strip("\n")
        for i in range (len(recv_res_f)-1): 
            final_res.append(recv_res_f[i])
        exp_res.sort()
        final_res.sort()
        logging.info("after sort")
        logging.info(len(recv_res_f))
        logging.info(len(exp_res))
        logging.info(exp_res[3])
        logging.info(final_res[3])       
        self.assertEqual(final_res,exp_res)   
        logging.info("Test1 Complete : Test for infrequent pattern with regex")
        

    # Test for Frequent Grep        
    def test_grep_freq(self):
        logging.info("Test2 Begins : Test for GREP with frequent pattern")        
        unix_cmd =  'grep -c  "\.atext\.com" /usr/local/mp1/test_log.log'  
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'exp-results/exp_results_freq.txt')
        exp_result_file = open(filename, "rb")
        exp_res_lines = exp_result_file.readlines()   
        exp_res = []
        exp_result_file.close()
        for line in exp_res_lines:
            line1 = line.strip(b'\n')
            exp_res.append(line1.decode())                        
        client.main_sub("server-names-test.txt", unix_cmd)
        recv_res = (sys.stdout.getvalue()).split("\n")
        final_res = []
        for i in range (len(recv_res)-1): 
            final_res.append(recv_res[i])
        exp_res.sort()
        final_res.sort()
        self.assertEqual(final_res,exp_res)       
        logging.info("Test2 Complete : Test for GREP with frequent pattern")
    
    # Test for Grep with single remote return
    def test_grep_single(self):
        logging.info("Test3 Begins : Test for GREP with single remote return")        
        unix_cmd =  'grep blueberry /usr/local/mp1/test_log.log'  
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'exp-results/exp_results_singlemachine.txt')
        exp_result_file = open(filename, "rb")
        exp_res_lines = exp_result_file.readlines()   
        exp_res = []
        exp_result_file.close()
        for line in exp_res_lines:
            line1 = line.strip(b'\n')
            exp_res.append(line1.decode())                        
        client.main_sub("server-names-test.txt", unix_cmd)  
        recv_res = (sys.stdout.getvalue()).split("\n")
        final_res = []
        for i in range (len(recv_res)-1): 
            final_res.append(recv_res[i])
        exp_res.sort()
        final_res.sort()
        self.assertEqual(final_res,exp_res)            
        logging.info("Test3 Complete : Test for GREP with single remote return")   

    # Test grep with regex with two machines
    def test_grep_twofiles(self):
        logging.info("Test4 Begins : Regex Plus two machines")
        unix_cmd =  'grep "\[10\/Oct\/1995:09:2[89]" /usr/local/mp1/test_log.log'  
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'exp-results/exp_results_twomachines.txt')
        exp_result_file = open(filename, "rb")
        exp_res_lines = exp_result_file.readlines()   
        exp_res = []
        exp_result_file.close()
        for line in exp_res_lines:
            line1 = line.strip(b'\n')
            exp_res.append(line1.decode())            
        client.main_sub("server-names-test.txt", unix_cmd)        
        recv_res = (sys.stdout.getvalue()).split("\n")
        final_res = []
        for i in range (len(recv_res)-1): 
            final_res.append(recv_res[i])
        exp_res.sort()
        final_res.sort()
        self.assertEqual(final_res,exp_res)  
        logging.info("Test4 Complete : Regex Plus two machines")  
   
    # Test grep for tabs
    def xtest_grep_metacharacter(self):
        logging.info("Test5 Begins : Look for lines with tab using Cstring")
        ##Testing grep
        unix_cmd =  'grep $''\t'' -m 2 /usr/local/mp1/test_log.log'
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'exp-results/exp_results_meta.txt')
        exp_result_file = open(filename, "rb")
        exp_res_lines = exp_result_file.readlines()   
        exp_res = []
        exp_result_file.close()
        for line in exp_res_lines:
            line1 = line.strip(b'\n')
            exp_res.append(line1.decode())            
        client.main_sub("server-names-test.txt", unix_cmd)        
        recv_res = (sys.stdout.getvalue()).split("\n")
        final_res = []
        for i in range (len(recv_res)-1): 
            final_res.append(recv_res[i])
        exp_res.sort()
        final_res.sort()
        self.assertEqual(final_res,exp_res) 
        logging.info("Test5 Complete : Tab with Cstring")  
    
    # Test for perl regex
    def xtest_grep_perlregex(self):
        logging.info("Test6 Begins : Look for lines with tab using Perl regex")
        unix_cmd =  'grep -P="\t" -m 2 /usr/local/mp1/test_log.log'  
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'exp-results/exp_results_meta.txt')
        exp_result_file = open(filename, "rb")
        exp_res_lines = exp_result_file.readlines()   
        exp_res = []
        exp_result_file.close()
        for line in exp_res_lines:
            line1 = line.strip(b'\n')
            exp_res.append(line1.decode())            
        client.main_sub("server-names-test.txt", unix_cmd)        
        recv_res = (sys.stdout.getvalue()).split("\n")
        final_res = []
        for i in range (len(recv_res)-1): 
            final_res.append(recv_res[i])
        exp_res.sort()
        final_res.sort()
        self.assertEqual(final_res,exp_res)  
        logging.info("Test6 Complete : Tab with PerlRegex")
  
    # Test for extended regular expressions
    def test_grep_extregex(self):
        logging.info("Test7 Begins : Using Extended regular expression")
        unix_cmd =  'grep -E "[[3][1]/[a-zA-Z]{3}/1995:23:16:" /usr/local/mp1/test_log.log' 
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'exp-results/exp_results_infreq_regex.txt')
        exp_result_file = open(filename, "rb")
        exp_res_lines = exp_result_file.readlines()   
        exp_res = []
        exp_result_file.close()
        for line in exp_res_lines:
            line1 = line.strip(b'\n')
            exp_res.append(line1.decode())            
        client.main_sub("server-names-test.txt", unix_cmd)        
        recv_res = (sys.stdout.getvalue()).split("\n")
        final_res = []
        for i in range (len(recv_res)-1): 
            final_res.append(recv_res[i])
        exp_res.sort()
        final_res.sort()
        self.assertEqual(final_res,exp_res)  
        logging.info("Test7 Ends : Extended regular expression")  
    
    # Test using context switches
    def test_grep_context(self):
        logging.info("Test8 Begins : using context switches")
        unix_cmd =  'grep blueberry --context=2  /usr/local/mp1/test_log.log' 
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'exp-results/exp_results_context.txt')
        exp_result_file = open(filename, "rb")
        exp_res_lines = exp_result_file.readlines()   
        exp_res = []
        exp_result_file.close()
        for line in exp_res_lines:
            line1 = line.strip(b'\n')
            exp_res.append(line1.decode())            
        client.main_sub("server-names-test.txt", unix_cmd)        
        recv_res = (sys.stdout.getvalue()).split("\n")
        final_res = []
        for i in range (len(recv_res)-1): 
            final_res.append(recv_res[i])
        exp_res.sort()
        final_res.sort()
        self.assertEqual(final_res,exp_res)  
        logging.info("Test8 Ends : Using context switches")  
    
    # Test grep with count
    def test_grep_count(self):
        logging.info("Test9 Begins : test count")
        unix_cmd =  'grep -E "[[3][1]/[a-zA-Z]{3}/1995:23:16:" -c /usr/local/mp1/test_log.log'
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'exp-results/exp_results_count.txt')
        exp_result_file = open(filename, "rb")
        exp_res_lines = exp_result_file.readlines()   
        exp_res = []
        exp_result_file.close()
        for line in exp_res_lines:
            line1 = line.strip(b'\n')
            exp_res.append(line1.decode())            
        client.main_sub("server-names-test.txt", unix_cmd)        
        recv_res = (sys.stdout.getvalue()).split("\n")
        final_res = []
        for i in range (len(recv_res)-1): 
            final_res.append(recv_res[i])
        exp_res.sort()
        final_res.sort()
        self.assertEqual(final_res,exp_res) 
        logging.info("Test9 Ends : test count") 
            
    def tearDown(self):
        sys.stdout = self.held
        
        
if __name__ == "__main__":
    # Create a log
    logging.basicConfig(filename = "unittest1.log", level = logging.INFO, filemode = "w")
    unittest.main()
