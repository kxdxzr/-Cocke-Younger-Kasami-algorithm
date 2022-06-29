from check_not_exists import check_not_exists
from stack import Stack
from print_line import print_noco_line

def make_table(string_len):
    table = []
    counter = 0
    while counter < string_len:
        counter2 = 0
        buf_table = []
        while counter2 < string_len:
            #buf_table.append("")
            buf_table.append([])
            counter2 += 1
        table.append(buf_table)
        counter += 1
    return table

def edit_table(table,i,j,cur_variable):
    #table[j-i][i]=cur_variable
    if check_not_exists(table[j-i][i],cur_variable):
        table[j-i][i].append(cur_variable)
    return table

def show_table(table,i,j):
    return table[j-i][i]

def show_all_variables(table,i,j):
    cur_cell = show_table(table,i,j)
    out_put = []
    for cur_variable in cur_cell:
        out_put.append(cur_variable[0])
    return out_put

def finish_table(start,variables,rules,cur_string,results):
    table = []
    string_len = len(cur_string)
    if string_len == 0:
        start_rule = rules[start]
        if check_not_exists(start_rule,["epsilon"]):
            results.append("0")
        else:
            results.append("1")
        return []
    else:
        table = make_table(string_len)
        counter = 0
        while counter < len(cur_string):
            cur_terminal = cur_string[counter]
            for cur_variable in variables:
                cur_variable_rule = rules[cur_variable]
                if not check_not_exists(cur_variable_rule,[cur_terminal]):
                    #print(cur_variable_rule)
                    table = edit_table(table,counter,counter,[cur_variable,[cur_terminal],0]) #[variable,rule,k]
            counter += 1
    counter_l = 2
    while counter_l < string_len + 1:
        counter_i = 1
        while counter_i < string_len - counter_l + 2:
            j = counter_i + counter_l - 1
            counter_k = counter_i
            while counter_k < j:
                for cur_variable in variables:
                    cur_variable_rules = rules[cur_variable]
                    for cur_rule in cur_variable_rules:
                        cur_position_one = show_all_variables(table,counter_i-1,counter_k-1)
                        cur_position_two = show_all_variables(table,counter_k,j-1)
                        if not (check_not_exists(cur_position_one,cur_rule[0]) or check_not_exists(cur_position_two,cur_rule[1])):
                            edit_table(table,counter_i-1,j-1,[cur_variable,cur_rule,counter_k]) #
                counter_k += 1
            counter_i += 1
        counter_l += 1
    #print(table)
    return table

def derivation(table,start,stack,steps,ambiguous_mode):
    while stack.show_length() != 0:
        cur_variable = stack.show_current()
        current_i = cur_variable[1]
        current_j = cur_variable[2]
        #print(cur_variable)
        current_position = cur_variable[3]
        current_k = cur_variable[0][2]
        #print(cur_variable)
        if current_i == current_j:
            steps[current_position] = cur_variable[0][1][0]
            stack.pop()
        else:
            if ambiguous_mode:
                cur_all_variables = show_all_variables(table,current_i-1,current_k-1)
                new_all_variables = []
                for cur_all_variable in cur_all_variables:
                    if cur_all_variable != start:
                        new_all_variables.append(cur_all_variable)
                if len(new_all_variables) > 1:
                    return 1
            steps[current_position] = cur_variable[0][1][0]
            steps.insert(current_position + 1,cur_variable[0][1][1])
            stack.pop()
            stack.push([show_table(table,current_i-1,current_k-1)[0],current_i,current_k,current_position])
            stack.push([show_table(table,current_k,current_j - 1)[0],current_k + 1,current_j,current_position+1])
        if not ambiguous_mode:
            print_noco_line(steps)
    return 0
