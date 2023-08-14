import requests


def run_query(query, variables):

    # endpoint where you are making the request
    request = requests.post(' https://api.zora.co/graphql'
                            '',
                            json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))