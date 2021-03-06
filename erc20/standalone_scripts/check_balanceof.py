import requests


def main():
    contract_address = "0xcontractAddress"
    api_key = '1122-122-23443-1133'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json',
               'X-API-KEY': api_key}
    rest_api_endpoint = 'https://beta-api.ethvigil.com/v0.1'
    account= '0x774246187E1E2205C5920898eEde0945016080Df'
    method_api_endpoint = f'{rest_api_endpoint}/contract/{contract_address}/balanceOf/{account}'
    r = requests.get(url=method_api_endpoint, headers=headers)
    print(r.text)


if __name__ == '__main__':
    main()