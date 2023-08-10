import ape


def deploy_ctoken_pool(
    accounts: ape.managers.accounts.AccountManager,
    ctoken_container: ape.contracts.ContractContainer,
    underlying_token_instance: ape.contracts.ContractInstance,
    comptroller_instance: ape.contracts.ContractInstance,
    rate_instance: ape.contracts.ContractInstance,
    name: str = "Compound Test Token",
    symbol: str = "cTST",
    decimals: int = 8,
) -> ape.contracts.ContractInstance:
    """Deploy a Compound pool with an underlying test token.
    See constructor arguments here > https://etherscan.io/address/0x39AA39c021dfbaE8faC545936693aC917d5E7563#code
    """
    ctoken = ctoken_container.deploy(
        underlying_token_instance,
        comptroller_instance,
        rate_instance,
        name,
        symbol,
        decimals,
        sender=accounts[0],
    )
    return ctoken
