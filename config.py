#

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", 19217751)
        self.API_HASH: str = os.environ.get("API_HASH", 5367033476:AAFYsFMxGRZXNQScfqNNnOED25-Rh-HUPDM)
        self.SESSION: str = os.environ.get("SESSION", BQBi1hARdGbSNhAvd3pjHQsyASgPtiHlxyQkh9noX2dGwTrugzFCbHhDT8ADnSpG73dUuOZ5SOtK8TAiDinpPq5FU9N9g5aLgWL2AvpRTX2Q4GEJhuh9BhkJB2uL4_Sz_MuVXe-n9DJNiN1DucO_nhYCaSj0Vd-YhhFq8nxqRjvc-Gf0F_XIwNPMo6ICKg4AHJF3Rpmx4ZrSn9fxl5kMW-9PIfK9smWbBy3G-CFUSA4AVwmrkBGVVi-2xT7u4EEr2aPzZR9ebqr-H82VPIdi5XRSKYiJ8yCjmCCfuXzTWzKoLh_3f5sM0qHTB6a94CKML_Sv_GJJL0CscQJEFCWPIzwvAAAAATg_3UsA)
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", 5396090877:AAEmPoFlKb98wJFzsAXv8GPPPNwQ_JG5P4g)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
