from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 9671629
    API_HASH = "be5c84e9dc1ca0e2b53d54b71e575124"
    # the name to display in your alive message
    ALIVE_NAME = "BiLaL"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:your_password@localhost:5432/bonme"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBu6XXAEz5QLEsomypIICZwWDcBfecchXUDrnjMASV7gkAHvBmPvcE0P-2YsHsOtkERE69HeXY0EgjO8x3naZoO0_k0JZm3Dhv7s0sNECiXToetzx-8z02PQ30Upv2F1Q7VOSvnC7A8CJVv5d4FhmxEpLAamRkWRZsq9DD2lzbETkDMgKhZCnRQuXDLR8UDttklWoNefj8ZYLzlBEzmgZ0VdRjHHzHOIly9QJv9otNnpBDzake5jLgncKjB-o0FMLxKC5T3gCi0YNgAQuJhYXA8cNip5QZ5GsCyAzEpZEmTl33PyDy_BqM1LGnLibLtRRiM6dy_EJJKBDxIEsIV8KY6Zk="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "7121027327:AAFv_m4QjrjppxFHrdtpTinhCWhp2Kk9uiU"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
