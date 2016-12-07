# Distributed Log Querier

## Introduction

A company just discovered that distributed systems are hard to debug. We
must build a solution that they can use. They want a system that is fast
and correct.

## Motivation

Debuggers work well mostly in single-threaded programs. The most popular
apporach to debugging distributed systems is logging. This means that
each  machine creates one or more local files into which are accumulated
status messages, error messages, and in general anything that you want
to log. These logs can then be queried remotely.

Any code that we write will have bugs. The industry standard for making
sure that your program accomplishes what you desire, is unit testing.

## Requirements

python3.5

## File List

* exp-results: Folder of experimental results
 * exp_results_context.txt: Context results
 * exp_results_count.txt: Count results
 * exp_results_freq.txt: Frequent grep results file for unit test
 * exp_results_infreq_regex.txt: Infrequent grep with regex results file for unit test
 * exp_results_singlemachine.txt: Grep results file on one machine for unit test
 * exp_results_twomachines.txt: Grep results file on two machines for unit test
* client.py: Client code
* server-names.txt: File input with the hostnames of servers
* server.py: Server code
* testfour.txt: Test four machines for the unit test
* testone.txt: Test one machine for the unit test
* testtwo.txt: Test two mahchines for the unit test
* test1.py: Unit test for various grep parameters across various machines
* test2.py: Unit test for infrequent Grep on an increasing number of machines
* test3.py: Unit test for semi-Frequent Grep on an increasing number of machines
* test4.py: Unit test for a non-existent pattern on an increasing number of machines
* test5.py: Unit test for a null pattern on an increasing number of machines
* test6.py: Unit test for frequent grep on machines

## Basic Code

### Server 

python3.5 server.py &

### Client 

python3.5 client.py server-names.txt 'grep <pattern> <file>'

### Unit Test
# First Suite of Tests

python3.5 test1.py 

# Second Suite of Tests
python3.5 test2.py

# Other tests

python3.5 testx.py, where = 3 to 6

Note: All tests in a single suite run simultaneously. Each test suite has more than one unit test running simultaneously. 

## Code Example

Setup all the servers

python3.5 server.py &

Choose a client machine

### Sample Grep Commands:

##### Grep command is one to many series of strings in command line

python3.5 client server-names.txt 'grep sirius /usr/local/mp1/vm.log'

python3.5 client server-names-test.txt 'grep "\[10\/Oct\/1995:09:2[89]" /usr/local/mp1/test_log.log'

##### Grep as series of string with each string representing a portion of command

python3.5 client server-names-test.txt 'grep' '"\[10\/Oct\/1995:09:2[89]"' '/usr/local/mp1/test_log.log'

##### Grep with regular expression

python3.5 client server-names-test.txt 'grep' '"\[31\/[a-zA-Z]\{3\}\/1995:23:16:"' '/usr/local/mp1/test_log.log'

##### Grep for a pattern with quotes, note that grep command is multiple strings

python3.5 client.py server-names-test.txt 'grep -i -o -m 2' '"\"GET /~scottp/publish.html\""' '/usr/local/mp1/test_log.log'

##### Extended Regular Expression 

python3.5 client.py server-names-test.txt 'grep -m 10 -E' '"[[3][1]/[a-zA-Z]{3}/1995:23:16:"' '/usr/local/mp1/test_log.log'

##### Perl like regular expression, capturing lines with tab

python3.5 client.py server-names-test.txt 'grep -m 10 -P' '"\t"' '/usr/local/mp1/vm.log'


## Unit Test

* Test for infrequent pattern with regex
* Test for GREP with frequent pattern
* Test for GREP with single remote return
* Regex Plus two machines
* Using Extended regular expression
* Using context switches
* Test count (-c)
* Infrequent Grep - Client to 1 Server
* Infrequent Grep - Client to 4 Servers
* Infrequent Grep - Client to 7 Servers
* No Return Grep (pattern: zzzzzz) - Client to 7 Servers
* Null Grep - Client to 7 Servers
* Semi-Frequent Grep - Client to 1 Server
* Semi-Frequent Grep - Client to 4 Servers
* Semi-Frequent Grep - Client to 7 Servers
