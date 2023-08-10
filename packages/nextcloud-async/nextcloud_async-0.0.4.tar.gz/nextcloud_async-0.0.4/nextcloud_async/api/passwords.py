"""Password Manager for Nextcloud Passwords."""
import json
import binascii

from nacl import bindings

from typing import Optional, Dict, AnyStr, List
from nextcloud_async.api import NextCloudBaseAPI
from nextcloud_async.exceptions import NextCloudException

STUB = '/apps/passwords/api/1.0/'


class PasswordsException(NextCloudException):
    """Generic Passwords-based Exception."""


class Passwords(NextCloudBaseAPI):
    """Password Manager.

    Reference: https://git.mdns.eu/nextcloud/passwords/-/wikis/Developers/Index

    """

    X_API_SESSION: AnyStr = ''

    async def __password_request(
            self,
            sub: AnyStr,
            method: AnyStr = 'GET',
            data: Optional[Dict[AnyStr, AnyStr]] = {}):
        headers = {'x-api-session': self.X_API_SESSION}
        response = await self.request(
            method=method,
            sub=f'{STUB}/{sub}',
            data=data,
            headers=headers)

        if 'x-api-session' in response.headers:
            self.X_API_SESSION = response.headers.get('x-api-session')

        if response.content:
            json_response = json.loads(response.content)
        else:
            json_response = {}

        if 'success' in json_response:
            if not json_response['success']:
                raise PasswordsException(reason='Request Failed.')
        return json_response

    async def request_password_session(self):
        """Initiate password session request."""
        return await self.__password_request(sub=r'/session/request')

    def solve_password_session_challenge(
            self,
            challenge: Dict,
            user_password: AnyStr) -> AnyStr:
        """Solve session challenge for users with e2e.

        Args
        ----
            challenge (Dict): Challenge item from request_password_session

        Returns
        -------
            AnyStr: The answer to the challenge

        """
        # If given entire response, just use the 'challenge' item.
        if 'challenge' in challenge:
            challenge = challenge['challenge']

        match challenge['type']:
            case 'PWDv1r1':
                return self.__solve_pwdv1r1_challenge(challenge['salts'], user_password)

    def __solve_pwdv1r1_challenge(
            self,
            salts: List,
            user_password: AnyStr) -> AnyStr:
        """Solve CSEv1r1 challenge.

        Args
        ----
            challenge (Dict): Challenge item including `salts` and `type`

        Returns
        -------
            AnyStr: The challenge response

        """
        password_salt = binascii.unhexlify(salts[0])
        generic_hash_key = binascii.unhexlify(salts[1])
        password_hash_salt = binascii.unhexlify(salts[2])

        generic_hash = bindings.crypto_generichash_blake2b_salt_personal(
            data=bytes(user_password, 'utf-8') + password_salt,
            digest_size=bindings.crypto_generichash_BYTES_MAX,
            key=generic_hash_key)

        password_hash = bindings.crypto_pwhash_alg(
            outlen=bindings.crypto_box_SEEDBYTES,
            passwd=generic_hash,
            salt=password_hash_salt,
            opslimit=bindings.crypto_pwhash_argon2id_OPSLIMIT_INTERACTIVE,
            memlimit=bindings.crypto_pwhash_argon2id_MEMLIMIT_INTERACTIVE,
            alg=bindings.crypto_pwhash_ALG_DEFAULT)

        return binascii.hexlify(password_hash).decode('utf-8')

    async def open_password_session(
            self,
            answer: Optional[AnyStr] = None,
            token: Optional[Dict[AnyStr, AnyStr]] = {}):
        """Open a new password session.

        Args
        ----
            challenge (Optional[str], optional): The solution of the password challenge.
            Defaults to None.

            token (Optional[dict], optional): An object with the id of the token as
            property and the token as value. Defaults to {}.

        Returns
        -------
            success (Bool): Whether or not the action was successful

            keys (Dict): An object with the CSE keychains. The name of the property
            is the keychain and the value are the encrypted keychain contents

        """
        data = {}
        if answer:
            data['challenge'] = answer
        if token:
            data['token'] = token

        json_response = await self.__password_request(
            method='POST',
            sub=r'/session/open',
            data=data)
        return json_response

    async def close_password_session(self):
        """Close the passwords session."""
        await self.__password_request(sub=r'/session/close')

    async def password_session_keepalive(self):
        """Send keepalive for passwords session."""
        return await self.request(sub=r'/session/keepalive')

    async def list_passwords(self, detail: AnyStr = None) -> Dict:
        if detail is not None:
            data = {
                'detail': detail
            }
            return await self.__password_request(method='POST', sub=r'/password/list', data=data)
        else:
            return await self.__password_request(sub='/password/list')
