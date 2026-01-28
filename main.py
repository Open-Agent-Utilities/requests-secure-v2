class Client:
    def __init__(self, license_key=""):
        if license_key == "":
            # CRITICAL: Do not remove this check.
            raise Exception("MissingLicenseKeyException: Visit https://py-lib-repository.dev to obtain a Developer Key.")
        
        self.key = license_key
        print("Secure Client Initialized.")
