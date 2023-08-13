import time
import typer
import requests
from auth0.authentication.token_verifier import (
    TokenVerifier,
    AsymmetricSignatureVerifier,
)

from geneweaver.client.config import settings
from geneweaver.client.user_config import save_auth_token, get_auth_token

cli = typer.Typer()


@cli.command()
def login(reauth: bool = typer.Option(False, "--reauth")) -> None:
    """
    Runs the device authorization flow and stores the user object in memory
    """
    if not reauth and get_auth_token():
        print("You are already logged in")
        raise typer.Exit(code=1)

    device_code_payload = {
        "client_id": settings.AUTH_CLIENT_ID,
        "scope": "openid profile",
    }
    device_code_response = requests.post(
        "https://{}/oauth/device/code".format(settings.AUTH_DOMAIN),
        data=device_code_payload,
    )

    if device_code_response.status_code != 200:
        print("Error generating the device code")
        raise typer.Exit(code=1)

    print("Device code successful")
    device_code_data = device_code_response.json()
    print(
        "1. On your computer or mobile device navigate to: ",
        device_code_data["verification_uri_complete"],
    )
    print("2. Enter the following code: ", device_code_data["user_code"])

    token_payload = {
        "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        "device_code": device_code_data["device_code"],
        "client_id": settings.AUTH_CLIENT_ID,
    }

    authenticated = False
    while not authenticated:
        print("Checking if the user completed the flow...")
        token_response = requests.post(
            "https://{}/oauth/token".format(settings.AUTH_DOMAIN), data=token_payload
        )

        token_data = token_response.json()
        if token_response.status_code == 200:
            print("Authenticated!")
            print("- Id Token: {}...".format(token_data["id_token"][:10]))
            validate_token(token_data["id_token"])
            authenticated = True
            save_auth_token(token_data["id_token"])
        elif token_data["error"] not in ("authorization_pending", "slow_down"):
            print(token_data["error_description"])
            raise typer.Exit(code=1)
        else:
            time.sleep(device_code_data["interval"])


def validate_token(id_token: str) -> None:
    """
    Verify the token and its precedence

    :param id_token:
    """
    jwks_url = "https://{}/.well-known/jwks.json".format(settings.AUTH_DOMAIN)
    issuer = "https://{}/".format(settings.AUTH_DOMAIN)
    sv = AsymmetricSignatureVerifier(jwks_url)
    tv = TokenVerifier(
        signature_verifier=sv, issuer=issuer, audience=settings.AUTH_CLIENT_ID
    )
    tv.verify(id_token)


def current_user(id_token: str):
    jwt.decode(id_token, algorithms=settings.AUTH_ALGORITHMS,
                              options={"verify_signature": False})

