"""This module is the entry point to your assignment. There is some scaffolding
to help you get started. It will call the appropriate method and load the input
data. You can edit or remove as much of this code as you wish to."""

from input_reading import Parser
from sys import stdin
from check_not_exists import check_not_exists
from make_list import make_list
from table import edit_table,show_table,make_table,show_all_variables,finish_table,derivation
from print_line import print_oneline,print_lines,print_noco_line
from stack import Stack

def membership(parser):
    test_strings = make_list(parser.parse_test_strings())
    results = []
    #print(variables)
    for cur_string in test_strings:
        string_len = len(cur_string)
        table = finish_table(start,variables,rules,cur_string,results)
        #print(string_len) start,variable,rules
        S_n = show_all_variables(table,0,string_len - 1)
        if not check_not_exists(S_n,start):
            results.append("1")
        else:
            results.append("0")
        #print(table)
    print_lines(results)
    print("end")

def rightmost_derivation(parser):
    test_string = parser.parse_test_string()
    table = finish_table(start,variables,rules,test_string,[])
    string_len = len(test_string)
    stack = Stack()
    top_table = table[string_len - 1][0]
    new_top = []
    #print(top_table)
    for cur_cell in top_table:
        cur_variable = cur_cell[0]
        if cur_variable == start:
            new_top.append(cur_cell)
    #print(new_top)
    #print(table)
    start_rule = new_top[0][1]
    #print(start_rule)
    start_k = new_top[0][2]
    stack.push([new_top[0],1,string_len,0]) #[current_variable,i,j,current_position]
    print(start)
    derivation(table,start,stack,[start],False)
    print("end")

def ambiguous(parser):
    test_strings = parser.parse_test_strings()
    results = []
    for cur_string in test_strings:
        string_len = len(cur_string)
        table = finish_table(start,variables,rules,cur_string,[])
        string_len = len(cur_string)
        stack = Stack()
        top_table = table[string_len - 1][0]
        new_top = []
        for cur_cell in top_table:
            cur_variable = cur_cell[0]
            if cur_variable == start:
                new_top.append(cur_cell)
        if len(new_top) > 1:
            results.append(1)
            continue
        elif len(new_top) == 0:
            results.append(0)
            continue
        start_rule = new_top[0][1]
        start_k = new_top[0][2]
        stack.push([new_top[0],1,string_len,0])
        results.append(derivation(table,start,stack,[start],True))
    print_lines(results)
    print("end")

if __name__ == '__main__':
    parser = Parser()
    command = parser.parse_command()
    cfg = parser.parse_cfg()
    variables = cfg["variables"]
    terminals = cfg["terminals"]
    start = cfg["start"]
    rules = cfg["rules"]

    if command == 'membership':
        membership(parser)
    elif command == 'rightmost-derivation':
        rightmost_derivation(parser)
    elif command == 'ambiguous':
        ambiguous(parser)
    else:
        print(f'Command {repr(command)} not recognised.')
