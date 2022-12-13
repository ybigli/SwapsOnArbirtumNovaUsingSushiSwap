from web3 import Web3
import random
from termcolor import cprint
import time
from tqdm import tqdm
from check_balance import balance_check_for_ERC_20_token, getErc20Abi

RPC = "https://nova.arbitrum.io/rpc"
web3 = Web3(Web3.HTTPProvider(RPC))
sushiRouterContractAddress = Web3.toChecksumAddress('0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506')
sushiRouterABI = '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
sushiRouterContract = web3.eth.contract(address=sushiRouterContractAddress, abi=sushiRouterABI)
slippage = 1  # %

def intToDecimal(qty, decimal):
    return int(qty * int("".join(["1"] + ["0"] * decimal)))

def swapEthToTokenAndViceVersa(privatekey, to_token_address, to_symbol, gasLimit):
    try:
        swap_eth_to_tokens(privatekey, to_token_address, to_symbol, gasLimit)
        x = random.randint(61, 99)
        for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
            time.sleep(1)

        if(checkAllowance(privatekey, to_token_address) == 0):
            x = random.randint(61, 99)
            for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
                time.sleep(1)
            approve(privatekey, to_token_address, to_symbol, gasLimit)
            print(f'\n>>> after approve', 'green')

        swapTokensToEth(privatekey, to_token_address, to_symbol, gasLimit)

        print(f'\n>>> after swapTokensToEth', 'green')
    except Exception as error:
        cprint(f'\n>>> {to_symbol} | {error}', 'red')


swaps = [
    {'address': '0x750ba8b76187092B0D1E87E28daaf484d1b5273b',
     'symbol': 'USDC'},

    {'address': '0x1d05e4e72cD994cdF976181CfB0707345763564d',
     'symbol': 'WBTC'},

    {'address': '0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1',
     'symbol': 'DAI'},
]

ethTokenAddress = Web3.toChecksumAddress('0x722E8BdD2ce80A4422E880164f2079488e115365')  # WETH

def approve(privateKey, tokenToApproveAddress, symbol, gasLimit):
    web3 = Web3(Web3.HTTPProvider(RPC))
    account = web3.eth.account.privateKeyToAccount(privateKey)
    address_wallet = account.address
    tokenToApproveAddress = Web3.toChecksumAddress(tokenToApproveAddress)

    tokenToApproveContract = web3.eth.contract(address=tokenToApproveAddress, abi=getErc20Abi())

    max_amount = web3.toWei(2 ** 32 - 1, 'ether')
    nonce = web3.eth.getTransactionCount(address_wallet)

    gasPrice = intToDecimal(0.0000000001, 18)

    try:
        tx = tokenToApproveContract.functions.approve(sushiRouterContractAddress, max_amount).buildTransaction({
            'from': address_wallet,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        signed_tx = web3.eth.account.signTransaction(tx, privateKey)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        cprint(f'\n>>> {symbol} approve : https://nova.arbiscan.io/tx/{web3.toHex(tx_hash)}', 'green')

    except Exception as error:
        print(f'\n>>> {symbol} approve error | {error}', flush=True)


def checkAllowance(privateKey, tokenAddress):
    tokenAddress = Web3.toChecksumAddress(tokenAddress)
    web3 = Web3(Web3.HTTPProvider(RPC))
    account = web3.eth.account.privateKeyToAccount(privateKey)
    address_wallet = account.address

    tokenContract = web3.eth.contract(address=tokenAddress, abi=getErc20Abi())
    allowance = tokenContract.functions.allowance(address_wallet, sushiRouterContractAddress).call()

    print(f'\n>>> allowance is {allowance}', 'green')
    return allowance


def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


def swap_eth_to_tokens(privateKey,  output_token_address,  to_symbol,  gasLimit):
    output_token_address = Web3.toChecksumAddress(output_token_address)
    gasPrice = intToDecimal(0.0000000001, 18)
    account = web3.eth.account.privateKeyToAccount(privateKey)
    address_wallet = account.address
    nonce = web3.eth.get_transaction_count(address_wallet)

    random_amount = random.randint(7, 9)
    amountToSwap = round(random.uniform(0.0101, 0.0109), random_amount)

    amount_out = sushiRouterContract.functions.getAmountsOut(Web3.toWei(amountToSwap, 'ether'), [ethTokenAddress, output_token_address]).call()
    min_tokens = int(float(amount_out[1]) * (1 - slippage / 100))

    contract_txn = sushiRouterContract.functions.swapExactETHForTokens(
        min_tokens,  # amountOutMin
        [ethTokenAddress, output_token_address],
        address_wallet,  # receiver
        (int(time.time()) + 10000)  # deadline
    ).buildTransaction({
        'from': address_wallet,
        'value': web3.toWei(amountToSwap, 'ether'),
        'gas': gasLimit,
        'gasPrice': gasPrice,
        'nonce': nonce,
    })
    signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=privateKey)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    cprint(
        f'\n>>> swap {to_symbol} : https://nova.arbiscan.io/tx/{web3.toHex(tx_hash)}', 'green')

def swapTokensToEth(privateKey, from_token_address, from_symbol, gasLimit):
    account = web3.eth.account.privateKeyToAccount(privateKey)
    address_wallet = account.address

    tokenBalance = balance_check_for_ERC_20_token(privateKey, from_token_address, from_symbol)

    random_amount = random.randint(10, 12)
    amountToSwap = round(tokenBalance, random_amount)
    gasPrice = intToDecimal(0.0000000001, 18)
    nonce = web3.eth.get_transaction_count(address_wallet)

    cprint(f'amountToSwap {amountToSwap}', 'yellow')

    amount_out = sushiRouterContract.functions.getAmountsOut(amountToSwap, [from_token_address, ethTokenAddress]).call()
    min_tokens = int(float(amount_out[1]) * (1 - slippage / 100))

    contract_txn = sushiRouterContract.functions.swapExactTokensForETH(
        amountToSwap,
        min_tokens,
        [from_token_address, ethTokenAddress],
        address_wallet,  # receiver
        (int(time.time()) + 10000)  # deadline
    ).buildTransaction({
        'from': address_wallet,
        'gas': gasLimit,
        'gasPrice': gasPrice,
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.sign_transaction(
        contract_txn, private_key=privateKey)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    cprint(
        f'\n>>> swap {from_symbol} : https://nova.arbiscan.io/tx/{web3.toHex(tx_hash)}', 'green')


def doSwaps():
    with open("private_keys.txt", "r") as f:
        keys_list = [row.strip() for row in f]

    random.shuffle(keys_list)

    for privatekey in keys_list:
        # amount of swaps from ETH to any token and vice versa
        swapAmountFromEthAndViceVersa = random.randint(1, 1)
        for i in range(0, swapAmountFromEthAndViceVersa):
            random.shuffle(swaps)
            cprint(f'\n=============== start : {privatekey} ===============', 'white')

            swap = swaps[0]
            to_token_address = swap['address']
            to_symbol = swap['symbol']

            gasLimit = random.randint(400000, 600000)

            swapEthToTokenAndViceVersa(privatekey, to_token_address, to_symbol, gasLimit)

            x = random.randint(61, 99)
            for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
                time.sleep(1)