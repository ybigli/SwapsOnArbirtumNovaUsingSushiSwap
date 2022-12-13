from web3 import Web3
from termcolor import cprint
import json


def check_balance(privatekey):
    try:
        RPC = 'https://nova.arbitrum.io/rpc'
        web3 = Web3(Web3.HTTPProvider(RPC))
        address = web3.eth.account.privateKeyToAccount(privatekey).address
        balance = web3.eth.get_balance(address)
        humanReadable = web3.fromWei(balance, 'ether')

        cprint(f'{address} : {humanReadable}', 'yellow')

    except Exception as error:
        cprint(f'error : {error}', 'red')


def check_balance_ERC_20_token(privatekey, tokenAddress, tokenSymbol):
    try:
        RPC = 'https://nova.arbitrum.io/rpc'
        web3 = Web3(Web3.HTTPProvider(RPC))
        contractToken = Web3.toChecksumAddress(tokenAddress)

        contract = web3.eth.contract(address=contractToken, abi=getErc20Abi())

        address = web3.eth.account.privateKeyToAccount(privatekey).address

        balance = contract.functions.balanceOf(address).call()

        decimals = contract.functions.decimals().call()

        humanReadableBalance = balance / 10**decimals

        cprint(f'{address} : has coin {tokenAddress} {tokenSymbol} with balance {humanReadableBalance}', 'yellow')

        return balance

    except Exception as error:
        cprint(f'error : {error}', 'red')


def balance_check():
    with open("private_keys.txt", "r") as f:  # поменяй путь
        keys_list = [row.strip() for row in f]

    for privatekey in keys_list:
        cprint(f'\n=============== start : {privatekey} ===============', 'white')

        check_balance(privatekey)


def balance_check_for_ERC_20_token(privatekey, tokenAddress, tokenSymbol):
    tokenBalance = check_balance_ERC_20_token(privatekey, tokenAddress, tokenSymbol)
    return tokenBalance


def getErc20Abi():
    with open("erc20_abi.json", "r") as f:
        data = json.load(f)
        str1 = str(data)
        data = eval(str1)
    f.close()
    return data
