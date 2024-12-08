import json
import requests
import typer

cli = typer.Typer()

@cli.command()
def update():
    print('Check Vaulted relics here')
    return

@cli.command()
def query(name: str='Aya'):
    if(name=='Aya'):
        print('Which is the most profitable Aya Relic to buy?')
    else:
        print('Here are the orders for ',name, ' item.')
    return

if __name__ == '__main__':
    cli()