import firebase_admin
from firebase_admin import firestore
import re

app = firebase_admin.initialize_app()
db = firestore.client()

def get_nendoroid_by_id(nendoroid_id):
    doc_ref = db.collection('nendoroids_v2').where("id", "==", nendoroid_id).get()

    if len(doc_ref) == 0:
        match_number = re.search("[0-9][0-9]*", nendoroid_id)

        if match_number:
            int_id = int(match_number.group())
            doc_ref = db.collection('nendoroids_v2').where("int_id", "==", int_id).get()

            if len(doc_ref) == 0:
                return None
            
        else:
            return None
    
    return doc_ref[0].to_dict()
