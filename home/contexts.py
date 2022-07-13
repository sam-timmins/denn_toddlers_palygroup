def site_contexts(request):
    """ Site variables """
    playgroup_name = 'Denn Toddlers'
    playgroup_dropped_pin = 'https://www.google.com/maps/place/3,+The+Old+Creamery,+Carrickatober,+Cross+Keys,+Co.+Cavan/@53.9187198,-7.2649662,116m/data=!3m1!1e3!4m5!3m4!1s0x485e08fcdb7a1861:0x30bb52edec147cc8!8m2!3d53.9187375!4d-7.265382'
    playgroup_phone_number = '0874116988'
    playgroup_email = 'email@email.com'
    facebook = 'https://www.facebook.com/Denn-Toddler-Playgroup-CLG-1957268074288664/?ref=page_internal'

    contexts = {
        'playgroup_name': playgroup_name,
        'playgroup_dropped_pin': playgroup_dropped_pin,
        'playgroup_phone_number': playgroup_phone_number,
        'playgroup_email': playgroup_email,
        'facebook': facebook,
    }

    return contexts
