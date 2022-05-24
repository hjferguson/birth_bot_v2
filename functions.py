def convertCarrier(carrier):
    """Converts birthday.txt carrier to carrier's SMS gateway"""
    if carrier == 'wind':
        carrier = 'txt.freedommobile.ca'
        return carrier
    elif carrier == 'bell':
        carrier = 'txt.bell.ca'
        return carrier
    elif carrier == 'telus':
        carrier = 'msg.telus.com'
        return carrier
    elif carrier == 'fido':
        carrier = 'fido.ca'
        return carrier
    elif carrier =='rogers':
        carrier = 'pcs.rogers.com'
        return carrier
    else:
        print("Sorry, that carrier is not supported.")