import requests
import json
import uuid
import re
class chatGPT():
    def __init__(self):
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    "Cookie": "__Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..aN87exHj5BDQRZJc.vrVhYKBqJThmPoWMJ_klVte0JSdyl1hqN3Xe4kds5iKhKO5U7mIbVtBvIF7RTRMBHcPMD_-77BaSDsfjQlWJvy1y6iU_TSDwLJ-hM6Jq4ntVAM4ldMb5UPnAIvBDLFxCIYkpZDU1Rf5r8wcV1aHpybjkVURK6jiD0FFrtwKziSwe4bR1HJ0cuEhkoRi0SLpzL1Fsxo3sH-aYkeCHG4nuaCgi1eizz36zCGMD_5dVaYYPUcRwNh4PbQoW5B5rO-Woebtufai1IsExcJR1shc_0N_f_Rkv7USUMFslkh-AKnwMQ_T4Wh2cQW-J2Tqi0A6HiLexckROOBRQ-uMj6jCaWDblspc1__ufupglwiuWCxI3I1SRfvZJerczCQj36AnmG7wYb8oO7UO2CjE4XYSDLpa-emYxq9Er98WJ43F8TQQBgyihZNGs5bveRU2UhVBmEctYZbuUGJZDG4wzSdyjXzZAovzY_ECpvIOGSUAhtQMvjZqsn4xafXo-Q4pq8oqGHkG3TF79suxAncK7waPFHlzH1S2DG91IQlemPh1d9ZxgXBlmN4tS-AEOhjf4miEOGeoBvLdMbN7dr5BAZRjqWijy5_-S8zXLt-LSQHeKF-Dz2Vq-J6e1ZF4Xt39w4vU8PuHLk3j9IurXvJRWWFgd69FIVTq-O8PfaxO8b-1l7V5eQFshWBsC2PzNW0EkhmiorgX-0hXxWg88F2CiIdS4Gf3LndSCfBbsjH0xl7leuMPJzzEZlpLUQmtpVwgx6Exr9mqRGbmK7pgQR2wWm9_DIVpGZuxq29swaYAX_D9jVA31BcFNjUAt9O5edvssZ0NTJ0cjiYHD2PcTZBdfny_-6J5f-aSBn_fSgvvPEoGabJSgDgz60Jo9_7AGsBoJsenI8TyjkZipyURkbQoIwcbpPiaxXCent1CPNzyWg0Lg7wSAY35vv5pd-GEu4BlhrbB6w4bbljuH7mM7PVWj51gDIpQjqi39j36_Z7m5vUMtQRo5BkiWg9WARQL78lwXXPCVm_6WA5f1xzKRCQVpLmZmlhOIY9j0HsHxKJk7nTHfmOsgXmLfOTWimYrOd3UF30REvlOE6_ONrpsDVbAHkc3vR4UQtyxK9M9NeSMGd-m9Eej8qd1SRkeB7KxjX7ZqYLqa9h1titeX05OYzTlAeeqcCwOLGBxLjpjtucJ3e_TJpX2zxNcaOTjJI6w2m69wdTz25ZKypIMyeNo0hbBiX_bvwqzo5ffUwPdBX4fQN5Y1YVkgRHSwb6VWHLo2iVRfZN6Rb6kRaKSUo0c2GcDy31EnP412kWp1CXH4E7_hm4hCe0GZJLyd1x9kVA8z44RApbsC3MUelsfVrMHpwYDeBGnguGx-iAvP41waDGigSZx_6Xit3jGNHqIob4IrQaVIVzdCPDg6FYykFWV8PZuegI1I-HnSWipQGv2-aTaEq3Ay0uYSni5qiMTU5Gb_3IQaEZnu3368qbv9v_gbLp5p3oSg20UFbeJe8WoQ2QTYTydm3PpJXeE0G5jxodVYk-QTTsl_0ITiIWFRkRFXDMXYmVWlfRqF2stnBNVf2rzLsN2_dceCaxr9fhuqe0QF657HwfDHYKITc7r3HfgZZhqIAKtROR_MODWAwcccoflJqJV7CKrUn-DvFZt1IFtHVDRYhHgBHp8Pev8W3z9HcAj5ZXFWAJQ3B0H9fC8V_MUbOLsGoi-vA6mkpZLbif8Iur_DSUxDBqDUQTyCKFlXvSSlSHwjpidIwvbJWSCUdz8OIk4pD-MBlUmAtMDQz1onIonjtnWwfxYiCk9D-HLOxS9QmbXFas04pMgU6iLM6rO959kP-SN7MvM8OKIxX9jPMVN5DWPAMVRPKw8oOB4jeMU5r8H3xWPY7AL5UlAa84luvyrSsUv5xuAp1ihCjrXKvvUlv1KiBatznXoIVfneOFFAWd61FgsZDPxHkiyPgFvXuVhY6aDU5Nb1sr3xNqmQsfrGUXwlbfpB8Asdr2oINcc4XODERowjEG19vIWarcDsuKhwY6By1D2Kufi4zpbbmFs-WuWAUx7L_gORgiJfPt19PYg-VIMqsGRt5eFB9-89Zohxkr25HXF8_wK-PhnpR192GXYREZ2WwkctOWE83YsuQPl3AnJ_T66dOBjL7OKadKhWxmmd3ZMomDY49ygoTWEK8X8tXkEadSlibHD216zW1spatRTCTfu0VTiw0FEFOALfPJGr-ZNiW1j6sxiuStn3qvoq56nAu14CCtaGtRBXul_iu4bqrARgZ-YJFz5SUhbUVjn2S9ri-a6YSzj9b4Rjqwf-gkjLVZh4MB8p5yazcSrBTAQg52FG9ROYRuh1qmdMbOqy_DlZpk96VXjYLlLjDSl4ZteN0vBqwFgfuEYYKu7Fh23d6H012yLbwWE7KCDrhwp7YGQug4Tm60OHO1pVQngN6-YMCmHy1MiQCXpw6-W2jwJViMYXGA8YOu_Cl2L1tuSO5zXKyHR5i5Bad_Cq6-IZ.ZQR0lF_4BbItFX7N_3txtw"
        }
        self.API_BASE_URL = "https://chat.openai.com/api"
        self.BACKEND_API_BASE_URL = "https://chat.openai.com/backend-api"
        self.session = requests.Session()
        self.conversation_id = ""
        self.initialize_cookies()
        self.auth()
    
    def initialize_cookies(self):
        response = self.session.get("https://chat.openai.com/chat", headers=self.headers)
        session_token = response.cookies["__Secure-next-auth.session-token"]
        self.headers["Cookie"] = "__Secure-next-auth.session-token=" + str(session_token) + ";"
    
    def auth(self):
        response = self.session.get(self.API_BASE_URL + "/auth/session", headers=self.headers).json()
        self.headers["Authorization"] = "Bearer " + str(response["accessToken"])
        
        #PREPARE FOR CONVERSATION
        self.headers["Content-Type"] = "application/json"
        self.headers["accept"] = "text/event-stream" 

    def reset(self):
        self.conversation_id = ""

    def conversation(self, message):
        if not self.conversation_id:
            #MEANS ITS THE FIRST MESSAGE
            body = {
                "action": "next",
                "messages": [
                    {
                        "id": str(uuid.uuid4()),
                        "role":"user",
                        "content": {
                            "content_type":"text",
                            "parts":[message]
                        }
                    }
                ],
                "parent_message_id": str(uuid.uuid4()),
                "model": "text-davinci-002-render"
            }
            response = self.session.post(self.BACKEND_API_BASE_URL + "/conversation", json=body, headers=self.headers)
            messages = re.findall('{"message": .*',response.text)
            full_message_dict = json.loads(messages[len(messages) - 1])
            self.conversation_id = full_message_dict["conversation_id"]
            self.parent_message_id = full_message_dict["message"]["id"]
            return full_message_dict["message"]["content"]["parts"][0]
        else:
            body = {
                "action": "next",
                "messages": [
                    {
                        "id": str(uuid.uuid4()),
                        "role":"user",
                        "content": {
                            "content_type":"text",
                            "parts":[message]
                        }
                    }
                ],
                "conversatioid": self.conversation_id,
                "parent_message_id": self.parent_message_id,
                "model": "text-davinci-002-render"
            }
            response = self.session.post(self.BACKEND_API_BASE_URL + "/conversation", json=body, headers=self.headers)
            messages = re.findall('{"message": .*',response.text)
            full_message_dict = json.loads(messages[len(messages) - 1])
            self.parent_message_id = full_message_dict["message"]["id"]
            return full_message_dict["message"]["content"]["parts"][0]








if __name__ == "__main__":
    print("Welcome to an unoficial implementation of chatGPT in python.")
    chat = chatGPT()
    while True:
        message = input("Input: ")
        answer = chat.conversation(message)
        print("Answer: " + answer + "\n")
        
