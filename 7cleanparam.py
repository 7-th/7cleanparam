#!/usr/bin/env python3

from urllib.parse import urlparse
import sys

def clear_parameter_value(url : str):
    question_mark_index = url.find('?')
    parameters = url[question_mark_index:].split('&')
    full_path = urlparse(url)._replace(query="").geturl() + "?"
    if url.count('&') >= 1:
        urls = []
        for p in parameters:
            all_params = (url[question_mark_index+1:].lstrip(p))
            if all_params != '&':
                p = p.strip('?')
                equal_index = p.find('=')
                if parameters[0] == '?' + p:
                    full_parameter = full_path + all_params[1:].rstrip() + '&' + p[:equal_index+1]
                    urls.append(full_parameter.strip())
                else:
                    full_path = urlparse(url)._replace(query="").geturl()
                    params = url[question_mark_index:]
                    all_params = (params.strip(p))
                    current_param_index = all_params.find(p.strip())
                    next_and_of_current_param = all_params[current_param_index:].find('&')
                    if current_param_index == -1:
                        full_parameter = full_path + all_params.strip(p[:p.find('=')+1]) + p[:p.find('=')+1]
                        urls.append(full_parameter.strip())
                    else:
                        full_current_param = all_params[current_param_index:(next_and_of_current_param + current_param_index + 1)].strip()
                        new_params = all_params.replace(full_current_param, '')
                        if parameters[-1] != p:
                            full_parameter = (full_path) + (new_params).rstrip() + ('&') + (p[:p.find('=')+1])
                        else:
                            full_parameter = (full_path) + (new_params).rstrip() + (p[:p.find('=')+1])
                        urls.append(full_parameter.strip())
        return urls
    else:
        equal_index = url.find('=')
        full_parameter = url[:equal_index+1]
        return [full_parameter,]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":

    final_results_set = set()

    for line in sys.stdin:
        
        line = line.strip()
        results = clear_parameter_value(line)

        for result in results:
            final_results_set.add(result)

    for result in final_results_set:
        sys.stdout.write(result + "\n")

