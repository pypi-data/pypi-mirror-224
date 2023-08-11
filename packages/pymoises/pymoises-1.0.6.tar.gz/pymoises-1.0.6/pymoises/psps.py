import requests
import logging


class Psps:
    def check_info_psp(idPsp: int):
        """
        Check info psps in moises by id.

        Params:
            idPsp (int): psps ids in moises  

        Return:
            success (boolean): success function
            message (string): result of function
            payload (dict) :
                active (int)
                endDate(str)
                idCrmPspCat (int)
                insertDate (int)
                name (str)
                visibility (int)
                settings (dict):
                    available (bool)
                    maxAmount (int)
                    mintAmount (int)
                    selectCountries (list[str])
                    availableCountries (list(int))
                    notAvailableBusinessUnit (list(int))

        """
        url = "http://webservicesnt.org:5050/get/info-psps"

        payload = {}
        payload['idPsp'] = str(idPsp)

        headers = {}
        headers['Content-Type'] = 'application/json'

        try:

            moisesResponse = requests.request("POST", url, headers=headers, json=payload)
            logging.warning('RESPONE CHECK INFO PSPS %s' % (moisesResponse.text))
            moisesResponse = moisesResponse.json()

            if not moisesResponse['result'] == 1:
                respone = {}
                respone['success'] = False
                respone['message'] = "psps not found"
                respone['payload'] = {}

                return respone

            respone = {}
            respone['success'] = True
            respone['message'] = "psp info correctly"
            respone['payload'] = moisesResponse['data']
            return respone
    
        except Exception as Err:
            respone = {}
            respone['success'] = False
            respone['message'] = str(Err)
            respone['payload'] = {}

            return respone